import json
import dataclasses

import pandas as pd

INPUT_PATH = "./data/data.json"

OUTPUT_JSON = "./output/results.json"

OUTPUT_CSV = "./output/results.csv"

@dataclasses.dataclass
class Options:
    creator: str
    sol_price: str
    mint_address: str
    token_address: str
    last_sale_price: str
    primary_sale_happend: str
    is_frozen: str
    is_tradeable: str

class JSON_TO_CSV:
    """Converts json data to csv format compatibe with shopify"""
    def __init__(self) -> None:
        self.results: list[dict] = []

    def __create_handle(self, data: dict[str, str]) -> str:
        """Creates the handle for a given product"""
        title = f'{data["title"]}-{data["content"]}'

        hndl = title.replace("/", "").lower()
        hndl_formatted = "-".join(hndl.split("_"))

        return hndl_formatted.encode('ascii', 'ignore').decode()
    
    def __create_product_skeleton(self, data: dict[str, str]) -> dict[str, str]:
        """Creates a product with some of the required fields"""
        return {
            "Handle": self.__create_handle(data).replace('"', ""),
            "Title": data["title"],
            "Vendor": data["onChainCollection"]["data"]["name"],
            "Body (HTML)": data["onChainCollection"]["data"]["description"],
            "Product Category": data["onChainCollection"]["key"],
            "Type": data["content"],
            "Tags": data["content"],
            "Published": "FALSE",
            "Option1 Name": "Creator Address",
            "Option1 Value": data["creators"][0]["address"],
            "Option2 Name": "Sol Price",
            "Option2 Value": data["solPrice"]["rawAmount"],
            "Option3 Name": "Mint Address",
            "Option3 Value": data["mintAddress"],
            "Option4 Name": "Token Address",
            "Option4 Value": data["tokenAddress"],
            "Option5 Name": "Last Sale Price",
            "Option5 Value": data["lastSalePrice"],
            "Option6 Name": "Primary Sale Happened",
            "Option6 Value": str(data["primarySaleHappened"]).upper(),
            "Option7 Name": "Is Frozen",
            "Option7 Value": str(data["isFrozen"]).upper(),
            "Option8 Name": "Is Tradeable",
            "Option8 Value": str(data["isTradeable"]).upper(),
            "Variant Inventory Tracker": "shopify",
            "Variant Inventory Qty": data["supply"],
            "Variant Inventory Policy": "deny",
            "Variant Fulfillment Service": "manual",
            "Variant Price": data["price"],
            "Variant Compare-at Price": "",
            "Variant Requires Shipping": "TRUE",
            "Variant Taxable": "TRUE",
            "Variant Grams": "",
            "Variant Barcode": "",
            "Image Src": data["img"],
            "Image Position": "",
            "Image Alt Text": data["content"],
            "Gift Card": "FALSE",
            "Google Shopping / Gender": "",
            "SEO Title": data["content"],
            "SEO Description": data["onChainCollection"]["data"]["description"],
            "Google Product Category": "",
            "Variant Image": "",
            "Variant Weight Unit": "kg",
            "Cost per item": data["price"],
            "Price / International": "",
            "Compare-at Price / International": "",
            "Status": "draft"
        }
    
    def __read_json(self) -> list[dict]:
        with open(INPUT_PATH) as file:
            return json.load(file)

    def __get_variants(self, 
                       data_dict: dict[str, str|int], 
                       options: Options) -> list[dict[str, str|int]]:
        results = [data_dict]

        skip_keys = ["Handle", 
                     "Option1 Value", 
                     "Option2 Value", 
                     "Option3 Value",
                     "Option4 Value",
                     "Option5 Value",
                     "Option6 Value",
                     "Option7 Value",
                     "Option8 Value",
                     "Image Src",
                     "Image Alt Text"]

        for other in self.results:
            if other != data_dict and other["Handle"] == data_dict["Handle"]:
                is_variant = False

                for key, _ in other.items():
                    if key in skip_keys: continue

                    other[key] = ""
                
                if other["Option1 Value"] == options.creator:
                    other["Option1 Value"] = ""
                else:
                    if not is_variant: is_variant = True
                
                if other["Option2 Value"] == options.sol_price:
                    other["Option2 Value"] = ""
                else:
                    if not is_variant: is_variant = True
                
                if other["Option3 Value"] == options.mint_address:
                    other["Option3 Value"] = ""
                else:
                    if not is_variant: is_variant = True
                
                if other["Option4 Value"] == options.token_address:
                    other["Option4 Value"] = ""
                else:
                    if not is_variant: is_variant = True
                
                if other["Option5 Value"] == options.last_sale_price:
                    other["Option5 Value"] = ""
                else:
                    if not is_variant: is_variant = True
                
                if other["Option6 Value"] == options.primary_sale_happend:
                    other["Option6 Value"] = ""
                else:
                    if not is_variant: is_variant = True
                
                if other["Option7 Value"] == options.is_frozen:
                    other["Option7 Value"] = ""
                else:
                    if not is_variant: is_variant = True
                
                if other["Option8 Value"] == options.is_tradeable:
                    other["Option8 Value"] = ""
                else:
                    if not is_variant: is_variant = True
                
                if is_variant: results.append(other)
        
        if len(results) > 1:
            print(data_dict["Handle"], ": ", len(results))
        
        return results
    
    def __reorganize(self) -> list[dict]:
        results, crawled = [], []

        for data_dict in self.results:
            handle = data_dict["Handle"]

            if handle in crawled: continue

            options = Options(creator=data_dict["Option1 Value"],
                              sol_price=data_dict["Option2 Value"],
                              mint_address=data_dict["Option3 Value"],
                              token_address=data_dict["Option4 Value"],
                              last_sale_price=data_dict["Option5 Value"],
                              primary_sale_happend=data_dict["Option6 Value"],
                              is_frozen=data_dict["Option7 Value"],
                              is_tradeable=data_dict["Option8 Value"])
            
            products = self.__get_variants(data_dict, options)

            crawled.append(handle)

            results.extend(products)
        
        return results
    
    def __save(self, results: list[dict]) -> None:
        with open(OUTPUT_JSON, "w") as file:
            json.dump(self.results, file, indent=4)
        
        df = pd.DataFrame(results).to_csv(OUTPUT_CSV, index=False)
    
    def run(self) -> None:
        [self.results.append(self.__create_product_skeleton(product)) 
         for product in self.__read_json()]
        
        results = self.__reorganize()

        self.__save(results)

if __name__ == "__main__":
    app = JSON_TO_CSV()
    app.run()
import json

import requests
import pandas as pd
from selenium import webdriver

from utils import Logger

OUTPUT_PATH = "./data/"

PARAMS = {
    "collectionSymbol": "",
    "onChainCollectionAddress": "8baMUdLZ5bsoNvpALp9NkWFW5or6RJQJTdAKWScbwW16",
    "direction": 2,
    "field": 1,
    "limit": 40,
    "offset": 0,
    "agg": 3,
    "compressionMode": "both"
}

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

URL = "https://api-mainnet.magiceden.io/idxv2/getAllNftsByCollectionSymbol"

class MagicEdenScraper:
    """Scrapes nfts from https://magiceden.io/marketplace/8baMUdLZ5bsoNvpALp9NkWFW5or6RJQJTdAKWScbwW16"""
    def __init__(self) -> None:
        self.logger = Logger(__class__.__name__)
        self.logger.info("{:*^50}".format("MagicEdenScraper Started"))

        self.results = []
    
    @staticmethod
    def __start_chrome() -> webdriver.Chrome:
        """Starts a new chrome browser instance"""
        while True:
            try:
                options = webdriver.ChromeOptions()

                options.add_argument("--disable-infobars")

                options.add_argument("--no-sandbox")

                options.add_argument("--headless=new")

                options.add_argument("--start-maximized")

                options.add_argument("--ignore-gpu-blocklist")

                options.add_argument(f"user-agent={HEADERS['User-Agent']}")

                options.add_argument("--incognito")

                options.add_argument('--disable-blink-features=AutomationControlled')

                options.add_experimental_option('useAutomationExtension', False)

                options.add_experimental_option("excludeSwitches", ["enable-automation"])

                options.add_argument("--log-level=3")

                options.add_argument('--disable-extensions')

                options.set_capability('pageLoadStrategy', 'none')

                return webdriver.Chrome(options=options)
            
            except: pass
    
    @staticmethod
    def __create_url_with_params(params: dict[str, str|int]) -> str:
        """Creates a full url containing the search parameters"""
        url_params = ""

        for key, value in params.items(): url_params += f"&{key}={value}"

        return f"{URL}?{url_params.lstrip('&')}"
    
    def __get_session(self, url: str) -> requests.Session:
        """Gets a requests session object that has the necessary cookies"""
        session = requests.Session()

        browser = self.__start_chrome()

        browser.get(url)

        [session.cookies.set(cookie["name"], 
                             cookie["value"], 
                             domain=cookie["domain"], 
                             expires=cookie.get("expiry"),
                             rest={'HttpOnly': cookie['httpOnly']},
                             secure=cookie['secure']) for cookie in browser.get_cookies()]
        
        browser.quit()

        return session
    
    @staticmethod
    def __get_params(offset: int) -> dict[str, str|int]:
        return {**PARAMS, "offset": offset}
    
    def __extract_nfts(self, response: requests.Response) -> bool:
        count_before = len(self.results)

        try:
            self.results.extend(response.json()["results"])

            self.logger.info("NFTs Extracted: {}".format(len(self.results)))
        except: pass

        return len(self.results) <= count_before
    
    def __request(self, session: requests.Session, url: str) -> requests.Response:
        count = 0

        while True:
            try:
                return session.get(url, headers=HEADERS)
            except:pass

            count += 1

            session, count = self.__get_session(url), 0 if count == 3 else session, count
    
    def __save(self) -> None:
        with open(f"{OUTPUT_PATH}data.json", "w") as file:
            json.dump(self.results, file, indent=4)

        pd.DataFrame(self.results).to_csv(f"{OUTPUT_PATH}data.csv", index=False)

    def run(self) -> None:
        url = self.__create_url_with_params(PARAMS)

        session = self.__get_session(url)

        offset, end_reached = 0, False

        while not end_reached:
            response = self.__request(session, url)

            end_reached = self.__extract_nfts(response)

            offset += 40

            params = self.__get_params(offset)

            url = self.__create_url_with_params(params)

            self.__save()

if __name__ == "__main__":
    app = MagicEdenScraper()
    app.run()
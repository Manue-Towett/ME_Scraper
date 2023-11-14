import requests
from urllib.parse import urlencode

import json

with open("cookies.json", "r") as file:
    FORM_DATA = json.load(file)
    
    # for key, value in FORM_DATA.items():
    #     if value == False:
    #         FORM_DATA[key] = "false"
    #     elif value == True:
    #         FORM_DATA[key] = "true"

# with open("cookies.json", "w") as file:
#     json.dump({"jsData": FORM_DATA}, file, indent=4)
    
encoded_data = urlencode(FORM_DATA)

URL = "https://api-js.datadome.co/js/"

HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    # Content-Length: 3913
    "Content-Type": "application/x-www-form-urlencoded",
    "Dnt": "1",
    "Origin": "https://magiceden.io",
    "Pragma": "no-cache",
    "Referer": "https://magiceden.io/",
    # Sec-Ch-Ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"
    # Sec-Ch-Ua-Mobile: ?0
    # Sec-Ch-Ua-Platform: "Linux"
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# print(response.status_code)

# print(response.content)

import json

session = requests.Session()

res = session.get("https://magiceden.io/marketplace/8baMUdLZ5bsoNvpALp9NkWFW5or6RJQJTdAKWScbwW16", headers=HEADERS)

print(res.status_code)

# url = "https://magiceden.io/locales/en/translation.json"

# response = session.get(url, headers=HEADERS)

response = session.post(URL, data=encoded_data, headers=HEADERS)

from http.cookies import SimpleCookie

cookie = SimpleCookie()

cookie.load(response.json()["cookie"])

print(response.json()["cookie"])

cookies = {k: v.value for k, v in cookie.items()}

session.cookies.set("datadome", cookies["datadome"], domain=".magiceden.io")

# print(session.cookies)

url = "https://api-mainnet.magiceden.io/idxv2/getAllNftsByCollectionSymbol"

# PARAMS = "?collectionSymbol=&onChainCollectionAddress=8baMUdLZ5bsoNvpALp9NkWFW5or6RJQJTdAKWScbwW16&direction=2&field=1&limit=40&offset=160&agg=3&compressionMode=both"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Cookie": "_cfuvid=CpSlJCypgOhzzV6S786Eb5nA4xB0r152tsQcPWyXp2I-1697098967736-0-604800000; _gcl_au=1.1.126805771.1697098973; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19j4wJhl9peXEDuUoiag%2BOUBksdVEwmIWiLnkJsxqwfCjO6LaPXmPq7; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2BwOneYRW1nQrs%2FI0BWYsd%2Fro%2BnJzGdhx4q9S4MlHVcmHhbjT4tzY%2F2; intercom-id-htawnd0o=6d1039a8-c09c-4fa8-912a-723870576644; intercom-session-htawnd0o=; intercom-device-id-htawnd0o=6d6464db-88a0-43f3-9dff-c2e84059dc21; rs_ga=GA1.1.14c34a5c-809c-4c31-b7d9-4fc2d1bcc1b3; arp_scroll_position=0; cf_clearance=42dvj3iAXipQZViOpi8vzHobkmvoQM3PoyEusfnD6aI-1697104922-0-1-6c92f174.4c0ae8df.6d3de1d5-0.2.1697104922; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BfrYNdqeSLaUPwdt037PKF%2BJz7Y1BCtaU%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2Bz8oPbynlRmSAQEb0%2FHkz%2Ft6YEnsmAPpQ%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2FAft7HrsImStaTln1PxmdO0xNBwgrndTQ%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FGUMB%2BzQ0pVmj7rHRYIZHEI9RdlyqnqeY%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19ejtFPt6jJMTWT5WDVF8sENLaqiCKqynzZcX2DLgSw2MgA%2FPfdFD6giptGiioDFmoa0Bc4xk3stw%3D%3D; rs_ga_8BCG117VGT=GS1.1.1697104923371.2.0.1697104928.60.0.0; rl_session=RudderEncrypt%3AU2FsdGVkX1%2BQCDaKu4cS1ecrG52F3e3mR%2F64aHvBjll2zvlQCdjDxRlZ5VzhEsoqVSg%2Bm9SOAWJ4%2F7Ns8VnsdCem72d17d%2FWdjWO6T0CKLIOjTXE2t5DN6Tv9EgD0%2FQ6BmY40RP%2Ftsoo6QDdof%2B3MA%3D%3D; datadome=aYo~~TVq_yxGClOW6MZxlU77678jvI0~I4MTD9AaZYzvVDl3M6M5rfmRiKeBo6XSh9vFAC6qyop~hxEUUDNILssKQI2TmIJvdB5E-S-E15x89d-VdFaMj9p~yXz0m10; __cf_bm=wBbjTYkG351mM7gsOYRswneevWAzLkZVsEMKU_nJQS8-1697110730-0-AQYfdBePMuOKV7E/KDxPy3Xu5107QgZ/jHydLf/9ei+ivjFoNemBoLrF09F0wCqWd9DecEAibWP822FEWhbpIBU=; arp_scroll_position=0",
    "Dnt": "1",
    "Pragma": "no-cache",
    "Sec-Ch-Ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

PAYLOAD = {
    "collectionSymbol": "",
    "onChainCollectionAddress": "8baMUdLZ5bsoNvpALp9NkWFW5or6RJQJTdAKWScbwW16",
    "direction": 2,
    "field": 1,
    "limit": 40,
    "offset": 160,
    "agg": 3,
    "compressionMode": "both"
}

response = session.get("https://magiceden.io/", headers=headers)

# print(response.status_code)
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    # "Accept-Encoding": "gzip, deflate, br",
    "Cache-Control": "no-cache",
    "Denorm-Nft-Shadow-Mode": "V2_ONLY",
    "Dnt": "1",
    # "Cookie": "_gcl_au=1.1.126805771.1697098973; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19j4wJhl9peXEDuUoiag%2BOUBksdVEwmIWiLnkJsxqwfCjO6LaPXmPq7; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2BwOneYRW1nQrs%2FI0BWYsd%2Fro%2BnJzGdhx4q9S4MlHVcmHhbjT4tzY%2F2; intercom-id-htawnd0o=6d1039a8-c09c-4fa8-912a-723870576644; intercom-device-id-htawnd0o=6d6464db-88a0-43f3-9dff-c2e84059dc21; rs_ga=GA1.1.14c34a5c-809c-4c31-b7d9-4fc2d1bcc1b3; _ga=GA1.2.822277618.1697111959; _ga_17CW5DWKSH=GS1.2.1697116309.2.0.1697116309.60.0.0; _cfuvid=ilb3cQ53Xa9uyOKAlC0hK2dHN3DLeboh9TL.3Uxci2U-1699975417754-0-604800000; arp_scroll_position=0; intercom-session-htawnd0o=; rs_ga_8BCG117VGT=GS1.1.1699975506725.6.0.1699976173.59.0.0; cf_clearance=Hw0V8be_HlrjQ_A17Z_VNammvx5QmqsFh6fZZYSrZGw-1699977651-0-1-48fc9831.4a9833a9.6baf3aa3-0.2.1699977651; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2Bzdd0NlMYKG3%2BrggeKNApeZNZ%2BBPBHAtU%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2BssBMUtK5vPLDMo%2F9VLWRcbYBWNXYY8%2FA%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2FR%2B47%2FQz%2BRv0B6cW1pVyOY7uoC17bnLnc%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FI51X80eoit%2F9cOosSTp2St3Q4gDoDe7I%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2BmZR%2FkMmtYoSvCYMUgZC5eQF5AqFxe8JaLDS%2Bw5b8ZBKMi0NjY7rfYJzjQumsL05S0c6Q6m%2B2L8w%3D%3D; datadome=3ORYelygjbAv5sg12ah~LRlNkMB2QwOjXhHyIFmzMHjI7JVP2TBuOkI4VAvIJngjZEHdLtNPWejVDoAX4xRCNwWxx~o~iKB4Tw6tXNOyUIMxqLxv84h8yIniF3bA~p_U; rl_session=RudderEncrypt%3AU2FsdGVkX19OLrD0l3LVkm%2F3nPSn9N%2B9dkd0ruE2NIBnu2dxbwue6bns%2FXelNmRcIibTcwhK7Tc9QxMmi2L0B1TW8F3P9DIBDh5jkfuv0ytb7MfDGT1DVqBlMB0EkCT0UKA1fO3hyC6Q3zaZyy%2Bzog%3D%3D; __cf_bm=jsBXLhxCurOUIEv3BfKKaSMrtXcT3yJ6vW7SskJ6RvY-1699982158-0-ARNge3aJF5hQVwyk1gRjKjJQvPiezCDmYyND3AGpk917iUxYhWGPi7YD42eIl9zJzZkrjc1s2HwJm1DgZCy/B/E=",
    "Origin": "https://magiceden.io",
    "Pragma": "no-cache",
    "Referer": "https://magiceden.io/",
    "Sec-Ch-Ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = session.get("https://magiceden.io/", headers=HEADERS)

response = session.get(url, headers=HEADERS, params=PAYLOAD)

# print(response.url)

print(response.status_code)

print(session.cookies)

if response.ok:
    import json

    with open("data1.json", "w") as file:
        json.dump(response.json(), file, indent=4)
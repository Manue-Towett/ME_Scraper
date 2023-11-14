

import requests
import pandas as pd
from bs4 import BeautifulSoup

PAYLOAD = {
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
    # "Accept-Encoding": "gzip, deflate, br",
    "Cache-Control": "no-cache",
    "Denorm-Nft-Shadow-Mode": "V2_ONLY",
    "Dnt": "1",
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

URL = "https://api-mainnet.magiceden.io/idxv2/getAllNftsByCollectionSymbol"

session = requests.Session()

res = session.get("https://magiceden.io/marketplace/8baMUdLZ5bsoNvpALp9NkWFW5or6RJQJTdAKWScbwW16", headers=HEADERS)

print(res.status_code)

url = "https://magiceden.io/locales/en/translation.json"

response = session.get(url, headers=HEADERS)

print(response.status_code)

import json

with open("sample.json", "w", encoding="utf-8") as f:
    json.dump(response.json(), f, indent=4)

response = session.get(URL, headers=HEADERS, params=PAYLOAD)

print(response.status_code)

# print(response.json())

with open("f.html", "w", encoding="utf-8") as f:
    f.write(response.text)

url = "https://api-mainnet.magiceden.io/v2/unifiedSearch/topCollections?chain=SOL&limit=100&offset=0&edge_cache=true"

HEADERS.update({
    "authority": "api-mainnet.magiceden.io",
    "scheme": "https",
    "method": "GET",
    "path": "/v2/unifiedSearch/topCollections?chain=SOL&limit=100&offset=0&edge_cache=true"
})
response = session.get(url, headers=HEADERS)

print(response.status_code)
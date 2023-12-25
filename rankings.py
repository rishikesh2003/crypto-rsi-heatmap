from config.index import COIN_RANK_API_KEY
import requests


def generate_ranking(symbol):
    url = f"https://api.coinranking.com/v2/coins?symbols={symbol}"
    headers = {
        "Content-Type": "application/json",
        "x-access-token": COIN_RANK_API_KEY,
    }
    res = requests.request("get", url=url, headers=headers)
    data = res.json()
    if len(data["data"]["coins"]) == 0:
        return 0
    return int(data["data"]["coins"][0]["rank"])

import requests
import pandas as pd

def fetch_coingecko_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    return pd.DataFrame(response.json())

def fetch_coinlore_data():
    url = "https://api.coinlore.net/api/tickers/"
    response = requests.get(url)
    return pd.DataFrame(response.json()['data'])

def fetch_crypto_data():
    data_coingecko = fetch_coingecko_data()
    data_coinlore = fetch_coinlore_data()
    return pd.concat([data_coingecko, data_coinlore], ignore_index=True)

if __name__ == "__main__":
    crypto_data = fetch_crypto_data()
    print(crypto_data)


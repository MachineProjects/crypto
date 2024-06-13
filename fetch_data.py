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
    data = response.json()
    for coin in data:
        coin['name'] = coin.get('name', "N/A")
        coin['symbol'] = coin.get('symbol', "N/A")
    return pd.DataFrame(data)

def fetch_coinlore_data():
    url = "https://api.coinlore.net/api/tickers/"
    response = requests.get(url)
    data = response.json()['data']
    for coin in data:
        coin['name'] = coin.get('name', "N/A")
        coin['symbol'] = coin.get('symbol', "N/A")
        coin['current_price'] = float(coin.get('price_usd', 0.0))
        coin['market_cap'] = float(coin.get('market_cap_usd', 0.0))
    return pd.DataFrame(data)

def fetch_coinmarketcap_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '093645cd-f54c-4c28-8792-422fcaee1f5c'
    }
    response = requests.get(url, headers=headers)
    data = response.json()['data']
    coin_list = []
    for coin in data:
        coin_list.append({
            'id': coin.get('id', "N/A"),
            'symbol': coin.get('symbol', "N/A"),
            'name': coin.get('name', "N/A"),
            'current_price': coin['quote']['USD']['price'],
            'market_cap': coin['quote']['USD']['market_cap']
        })
    return pd.DataFrame(coin_list)

def fetch_cryptocompare_data():
    url = "https://min-api.cryptocompare.com/data/top/mktcapfull"
    params = {
        "limit": 10,
        "tsym": "USD",
        "api_key": "18b332025eb16dfa031f3962bf81ab2427bcb955056ed13f00fa9186d89e003e"
    }
    response = requests.get(url, params=params)
    data = response.json()['Data']
    coin_list = []
    for item in data:
        coin = {
            'id': item['CoinInfo']['Id'],
            'symbol': item['CoinInfo']['Name'],
            'name': item['CoinInfo']['FullName'],
            'current_price': item['RAW']['USD']['PRICE'],
            'market_cap': item['RAW']['USD']['MKTCAP']
        }
        coin_list.append(coin)
    return pd.DataFrame(coin_list)

def fetch_crypto_data():
    data_coingecko = fetch_coingecko_data()
    data_coinlore = fetch_coinlore_data()
    data_coinmarketcap = fetch_coinmarketcap_data()
    data_cryptocompare = fetch_cryptocompare_data()
    return pd.concat([data_coingecko, data_coinlore, data_coinmarketcap, data_cryptocompare], ignore_index=True)

def fetch_historical_data(coin_id, days=30):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['prices']

if __name__ == "__main__":
    crypto_data = fetch_crypto_data()
    print(crypto_data[['name', 'symbol', 'current_price', 'market_cap']])


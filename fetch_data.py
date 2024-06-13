import requests
import pandas as pd

def fetch_crypto_data():
    # CoinGecko API
    coingecko_url = "https://api.coingecko.com/api/v3/coins/markets"
    coingecko_params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False,
    }
    coingecko_response = requests.get(coingecko_url, params=coingecko_params)
    coingecko_data = coingecko_response.json()
    
    coingecko_df = pd.DataFrame(coingecko_data)[['name', 'symbol', 'current_price', 'market_cap']]

    # CoinMarketCap API
    coinmarketcap_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    coinmarketcap_headers = {
        "X-CMC_PRO_API_KEY": "093645cd-f54c-4c28-8792-422fcaee1f5c"
    }
    coinmarketcap_params = {
        "start": "1",
        "limit": "10",
        "convert": "USD"
    }
    coinmarketcap_response = requests.get(coinmarketcap_url, headers=coinmarketcap_headers, params=coinmarketcap_params)
    coinmarketcap_data = coinmarketcap_response.json()["data"]

    coinmarketcap_df = pd.DataFrame(coinmarketcap_data)[['name', 'symbol', 'quote']]
    coinmarketcap_df['current_price'] = coinmarketcap_df['quote'].apply(lambda x: x['USD']['price'])
    coinmarketcap_df['market_cap'] = coinmarketcap_df['quote'].apply(lambda x: x['USD']['market_cap'])
    coinmarketcap_df = coinmarketcap_df[['name', 'symbol', 'current_price', 'market_cap']]
    
    # CryptoCompare API
    cryptocompare_url = "https://min-api.cryptocompare.com/data/top/mktcapfull"
    cryptocompare_params = {
        "limit": 10,
        "tsym": "USD",
        "api_key": "18b332025eb16dfa031f3962bf81ab2427bcb955056ed13f00fa9186d89e003e"
    }
    cryptocompare_response = requests.get(cryptocompare_url, params=cryptocompare_params)
    cryptocompare_data = cryptocompare_response.json()["Data"]

    cryptocompare_df = pd.DataFrame([{
        'name': coin['CoinInfo']['Name'],
        'symbol': coin['CoinInfo']['Internal'],
        'current_price': coin['RAW']['USD']['PRICE'],
        'market_cap': coin['RAW']['USD']['MKTCAP']
    } for coin in cryptocompare_data])

    # Merging data
    combined_df = pd.concat([coingecko_df, coinmarketcap_df, cryptocompare_df]).drop_duplicates(subset=['name', 'symbol']).reset_index(drop=True)
    
    return combined_df

def predict_prices(data):
    # Dummy prediction for demonstration
    data['predicted_price'] = data['current_price'] * 1.1  # Example: predicting a 10% increase
    return data


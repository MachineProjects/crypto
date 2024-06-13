from sklearn.linear_model import LinearRegression
import pandas as pd

def predict_prices(data):
    data = data[['name', 'symbol', 'current_price', 'market_cap', 'total_volume']].dropna()
    model = LinearRegression()
    X = data[['market_cap', 'total_volume']]
    y = data['current_price']
    model.fit(X, y)
    data['predicted_price'] = model.predict(X)
    return data

if __name__ == "__main__":
    from fetch_data import fetch_crypto_data
    crypto_data = fetch_crypto_data()
    predicted_data = predict_prices(crypto_data)
    print(predicted_data)


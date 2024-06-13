from flask import Flask, render_template, jsonify
from fetch_data import fetch_crypto_data
from predict import predict_prices

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crypto', methods=['GET'])
def get_crypto_data():
    data = fetch_crypto_data()
    predicted_data = predict_prices(data)
    # Log the data to verify its structure
    print("Data Returned to Frontend:", predicted_data[['name', 'symbol', 'current_price', 'market_cap', 'predicted_price']].to_dict(orient='records'))
    return jsonify(predicted_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)


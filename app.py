from flask import Flask, render_template, jsonify
from fetch_data import fetch_crypto_data, fetch_historical_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crypto', methods=['GET'])
def get_crypto_data():
    data = fetch_crypto_data()
    return jsonify(data.to_dict(orient='records'))

@app.route('/crypto/<coin_id>/history', methods=['GET'])
def get_historical_data(coin_id):
    data = fetch_historical_data(coin_id)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, jsonify
from fetch_data import fetch_crypto_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crypto', methods=['GET'])
def get_crypto_data():
    data = fetch_crypto_data()
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)


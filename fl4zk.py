# app.py
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import requests

app = Flask(__name__)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Endpoint for encryption
@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json.get('data', '')
    encrypted_text = cipher_suite.encrypt(data.encode())
    return jsonify({'encrypted': encrypted_text.decode()})

# Endpoint for decryption
@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json.get('data', '')
    decrypted_text = cipher_suite.decrypt(data.encode())
    return jsonify({'decrypted': decrypted_text.decode()})

# Endpoint for crypto price analysis
@app.route('/crypto_price', methods=['GET'])
def crypto_price():
    crypto = request.args.get('crypto', 'bitcoin')
    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd')
    price = response.json().get(crypto, {}).get('usd', 'Unknown')
    return jsonify({'crypto': crypto, 'price': price})

if __name__ == '__main__':
    app.run(debug=True)

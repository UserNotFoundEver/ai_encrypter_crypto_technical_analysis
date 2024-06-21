# AI Encrypter & Crypto Analysis App

## Overview
AI Encrypter & Crypto Analysis App is a web application that provides encryption and decryption of messages using the cryptography library and basic cryptocurrency analysis using data from the CoinGecko API. The backend is built with Flask, and the frontend is created using HTML, CSS, and JavaScript.

## Features
- **Message Encryption**: Encrypts plain text messages to keep them secure.
- **Message Decryption**: Decrypts encrypted messages back to their original form.
- **Crypto Price Analysis**: Retrieves the current price of specified cryptocurrencies.

## Technologies Used
- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript
- **Encryption**: Cryptography Library
- **Crypto Data API**: CoinGecko API only as an example but make our own.

## Installation

### Prerequisites
- Python 3.x
- Virtual environment tool (optional but recommended)

### Steps
1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/ai-encrypter-crypto-analysis.git
    cd ai-encrypter-crypto-analysis
    ```

2. **Create and activate a virtual environment** (optional but recommended)
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask application**
    ```sh
    python app.py
    ```

5. **Open the application in your browser**
    ```
    http://127.0.0.1:5000/
    ```

## Usage

### Encrypt a Message
- **Endpoint**: `/encrypt`
- **Method**: `POST`
- **Body**: `{ "data": "your_message" }`

**Example Request**:
```sh
curl -X POST http://127.0.0.1:5000/encrypt -H "Content-Type: application/json" -d '{"data": "Hello, World!"}'

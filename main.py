from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def home():
    return "API działa! Użyj /m2 żeby dostać dane."

@app.route('/m2')
def m2_value():
    ticker = yf.Ticker("^M2SL")
    hist = ticker.history(period="1d")
    m2 = hist["Close"].iloc[-1]
    return jsonify({"m2": m2})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

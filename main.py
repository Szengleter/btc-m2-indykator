from flask import Flask, jsonify
import requests

app = Flask(__name__)

FRED_API_KEY = "f397d50ff35849d8b71b080f3a53eda6"

def get_latest_m2():
    url = f"https://api.stlouisfed.org/fred/series/observations"
    params = {
        'series_id': 'M2SL',
        'api_key': FRED_API_KEY,
        'file_type': 'json',
        'sort_order': 'desc',
        'limit': 1,
    }
    response = requests.get(url, params=params)
    data = response.json()
    latest_obs = data['observations'][0]
    return float(latest_obs['value']) * 1_000_000_000  # USD

def get_btc_price():
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    return r.json()['bitcoin']['usd']

@app.route('/btc-m2')
def ratio():
    m2 = get_latest_m2()
    btc = get_btc_price()
    ratio = btc / m2 * 1e12
    return jsonify({
        "btc_usd": btc,
        "m2_usd": m2,
        "btc_m2_ratio_scaled": ratio
    })

if __name__ == '__main__':
    app.run()

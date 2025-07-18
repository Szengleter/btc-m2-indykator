from flask import Flask, jsonify
import pandas_datareader.data as web
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "API działa! Użyj /m2 żeby dostać dane z FRED."

@app.route('/m2')
def m2_value():
    try:
        end = datetime.today()
        start = datetime(end.year - 1, end.month, 1)

        df = web.DataReader("M2SL", "fred", start, end)

        if df.empty:
            return jsonify({"error": "Brak danych M2SL"}), 404

        latest_date = df.index[-1].strftime("%Y-%m-%d")
        latest_value = float(df.iloc[-1])

        return jsonify({
            "series": "M2SL",
            "date": latest_date,
            "value": latest_value
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

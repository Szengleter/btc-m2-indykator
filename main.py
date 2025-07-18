from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Działa! Serwis BTC/M2 gotowy 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Uwaga! Render ustawia PORT jako zmienną środowiskową
    app.run(host="0.0.0.0", port=port)        # ← TO JEST KLUCZOWE!

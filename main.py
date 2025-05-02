from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BRAVE_API_KEY = "BSA9RPTEcise3sSHOoSzjNgTy5YyoCH"

@app.route("/search")
def search():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "Brak zapytania"}), 400

    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": BRAVE_API_KEY
    }
    params = {"q": query}
    r = requests.get("https://api.search.brave.com/res/v1/web/search", headers=headers, params=params)

    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

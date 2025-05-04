from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "wpisz tutaj kod api"
CX = "a tutaj wpisz kod CX"

@app.route("/search")
def search():
    query = request.args.get("q")
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"
    res = requests.get(url)
    data = res.json()

    results = []
    for item in data.get("items", []):
        results.append({
            "title": item["title"],
            "url": item["link"],
            "description": item.get("snippet", "")
        })

    return jsonify({
        "web": {
            "results": results
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

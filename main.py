from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/search")
def search():
    query = request.args.get("q")
    url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1&skip_disambig=1"
    res = requests.get(url)
    data = res.json()

    results = []

    # Przykładowe wyniki z "RelatedTopics"
    for topic in data.get("RelatedTopics", []):
        if "Text" in topic and "FirstURL" in topic:
            results.append({
                "title": topic["Text"].split(" - ")[0],
                "url": topic["FirstURL"],
                "description": topic["Text"]
            })

    return jsonify({
        "web": {
            "results": results
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

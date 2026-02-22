rom flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(_name_)

@app.route("/")
def home():
    return "Ankit AI running 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    api_key = os.environ.get("OPEN_API_KEY")
    
    if not api_key:
        return jsonify({"error": "API key not found"}), 500

    client = OpenAI(api_key=api_key)

    user_message = request.json.get("message")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    return jsonify({"reply": response.choices[0].message.content})

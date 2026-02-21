from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(_name_)
client = OpenAI()

@app.route("/")
def home():
    return "AI is running"

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user}]
    )

    return jsonify({"reply": response.choices[0].message.content})

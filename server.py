from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(**name**)
CORS(app)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
user_message = request.json["message"]

```
response = openai.ChatCompletion.create(
    model="gpt-4.1-mini",
    messages=[{"role":"user","content":user_message}]
)

reply = response.choices[0].message.content
return jsonify({"reply": reply})
```

app.run(host="0.0.0.0", port=5000)

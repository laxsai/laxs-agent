from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "system", "content": "You are LAXS, a helpful AI agent on Solana." },
            { "role": "user", "content": user_input }
        ]
    )

    answer = response['choices'][0]['message']['content']
    return jsonify({ "reply": answer })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

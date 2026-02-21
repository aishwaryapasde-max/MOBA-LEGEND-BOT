import os
import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Boss Details
BOSS_NAME = "kuze"
BOSS_ID = "2037477019"

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return f"Mission: {BOSS_NAME}'s Shadow Bot is running in Docker! 😈"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get("message", "")
    prompt = f"Tu {BOSS_NAME} ka bot hai. Iska savage reply de: {user_msg}"
    response = model.generate_content(prompt)
    return jsonify({"reply": response.text.strip()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
  

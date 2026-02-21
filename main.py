import os
import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Identity Setup
BOSS_NAME = "kuze"
BOT_NAME = os.environ.get("GUEST_USERNAME", "Solo_Slayer_Bot")
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

@app.route('/chat', methods=['POST'])
def chat():
    try:
        if not API_KEY:
            return jsonify({"reply": "API Key missing!"}), 400
        
        genai.configure(api_key=API_KEY)
        # Fixed model path for v1beta
        model = genai.GenerativeModel('models/gemini-1.5-pro')
        
        data = request.get_json()
        msg = data.get("message", "Hi")
        
        prompt = f"Tu {BOT_NAME} hai. Boss {BOSS_NAME} ke liye savage reply de: {msg}"
        response = model.generate_content(prompt)
        
        return jsonify({"reply": response.text.strip()})
    except Exception as e:
        return jsonify({"reply": f"Internal Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
    

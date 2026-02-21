import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Identity Setup
BOSS_NAME = "kuze"
BOT_NAME = os.environ.get("GUEST_USERNAME", "Solo_Slayer_Bot")
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

@app.route('/chat', methods=['POST'])
def chat():
    try:
        if not API_KEY:
            return jsonify({"reply": "Bhai, API Key missing hai Render mein!"}), 400
        
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        data = request.get_json()
        msg = data.get("message", "Hi")
        
        # Savage logic
        prompt = f"Tu {BOT_NAME} hai. Tera boss {BOSS_NAME} hai. Savage reply de: {msg}"
        response = model.generate_content(prompt)
        
        return jsonify({"reply": response.text.strip()})
    except Exception as e:
        # Ye line Render ke logs mein error print karegi
        print(f"DEBUG: Error occurred -> {str(e)}")
        return jsonify({"reply": f"Internal Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
    

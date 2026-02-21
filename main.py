import os
import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Render Settings
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
BOT_NAME = os.environ.get("GUEST_USERNAME", "Solo_Slayer_Bot")

# 1. Home Route: Taaki browser mein 404 na aaye
@app.route('/')
def home():
    return f"<h1>Solo_Slayer_Bot is Online!</h1><p>Boss kuze, mission chalu hai! 😈</p>"

# 2. Chat Route: Termux/Curl ke liye
@app.route('/chat', methods=['POST'])
def chat():
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        data = request.get_json()
        msg = data.get("message", "Oye")
        
        # Identity Logic
        prompt = f"Tu {BOT_NAME} hai. Boss kuze (ID: 2037477019) ka bot hai. Reply: {msg}"
        response = model.generate_content(prompt)
        
        return jsonify({"reply": response.text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Render ke liye port 10000 zaroori hai
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    

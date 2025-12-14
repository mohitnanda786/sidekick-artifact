from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)

# The "Secret" API Key (in a real app, this would be in a DB or ENV)
SECRET_KEY = "sk_live_847293847293847239"

def insecure_compare(user_input, secret):
    """
    Vulnerable comparison function.
    Returns False immediately upon mismatch (Timing Leak).
    """
    if len(user_input) != len(secret):
        return False
    
    for i in range(len(user_input)):
        if user_input[i] != secret[i]:
            return False
        # Amplified for demonstration purposes (simulating DB lookup or RegEx)
        time.sleep(0.005) 
    
    return True

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data or 'api_key' not in data:
            return jsonify({"error": "Missing api_key"}), 400
        
        user_key = data['api_key']
        
        # Simulate network/database jitter (0-2ms)
        # This makes the attack harder and more realistic
        time.sleep(random.uniform(0, 0.002))
        
        if insecure_compare(user_key, SECRET_KEY):
            return jsonify({"status": "success", "token": "auth_token_12345"}), 200
        else:
            return jsonify({"status": "access_denied"}), 403
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Vulnerable Auth Service on port 5000...")
    app.run(host='0.0.0.0', port=5000)

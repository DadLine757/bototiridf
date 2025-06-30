from flask import Flask, request, jsonify
import hashlib, json

app = Flask(__name__)

@app.route('/auth', methods=['POST'])
def auth():
    key = request.json.get('key', '')
    hash_key = hashlib.sha256(key.encode()).hexdigest()

    with open('keys.json', 'r') as f:
        valid_keys = json.load(f)

    return jsonify({'valid': hash_key in valid_keys})
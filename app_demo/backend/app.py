# backend/app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from the Flask API!"})

@app.route('/api/square', methods=['GET'])
def square():
    number = request.args.get('number', default=1, type=int)
    return jsonify({"number": number, "square": number * number})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

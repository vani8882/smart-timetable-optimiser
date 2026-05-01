from flask import Flask, jsonify, request
from scheduler import generate_timetable

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "running"})

@app.route('/timetable', methods=['POST'])
def timetable():
    data = request.json
    result = generate_timetable(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
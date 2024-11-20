from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    response = {"result": data["input"] * 2}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

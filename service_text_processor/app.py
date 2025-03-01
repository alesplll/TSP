# service_text_processor/app.py
from flask import Flask, request, jsonify
from text_processor import process_text

app = Flask(__name__)


@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    text = data.get('text', '')
    sentences = process_text(text)
    return jsonify({'sentences': sentences})


if __name__ == '__main__':
    app.run(port=5001)

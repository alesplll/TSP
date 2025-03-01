# service_table_builder/app.py
from flask import Flask, request, jsonify
from table_builder import build_table

app = Flask(__name__)


@app.route('/build_table', methods=['POST'])
def build_table_route():
    data = request.get_json()
    sentences = data.get('sentences', [])
    table = build_table(sentences)
    return jsonify({'table': table})


if __name__ == '__main__':
    app.run(port=5002)

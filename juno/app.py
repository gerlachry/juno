import sys
print(sys.path)

from flask import Flask, jsonify

from juno.es_helper import ESHelper

app = Flask(__name__)

elastic = ESHelper(host='172.17.0.2', port='9200')


@app.route('/')
def index():
    results = elastic.test()
    return jsonify(results)

if __name__ == '__main__':
    app.run()
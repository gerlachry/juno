import sys

from juno.views import build_ui

print(sys.path)

from flask import Flask, jsonify, render_template

from juno.es_helper import ESHelper

app = Flask(__name__)

elastic = ESHelper(host='172.17.0.2', port='9200')

build_ui(app, elastic)
scripts = []
css = ["./css/main.css"]

@app.route('/test')
def test():
    results = elastic.test()
    return jsonify(results)

@app.route('/')
@app.route('/index')
def index():
    _scripts = ["./bundle.js"]
    return render_template('index.html',
                           title='Sensor Data',
                           base_scripts=scripts,
                           page_scripts=_scripts,
                           css=css)


if __name__ == '__main__':
    app.run(debug=True)

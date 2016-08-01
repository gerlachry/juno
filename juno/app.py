from views import build_ui
from flask import Flask, render_template
from es_helper import ESHelper
from config import config

app = Flask(__name__)

elastic = ESHelper(host=config.ES_HOST, port=config.ES_PORT)

scripts = []
css = ["./css/main.css"]


@app.route('/')
@app.route('/index')
def index():
    _scripts = ["./bundle.js"]
    return render_template('index.html',
                           title='Sensor Data',
                           base_scripts=scripts,
                           page_scripts=_scripts,
                           css=css)

@app.route('/latest/<typ>')
def latest(typ):
    return elastic.get_latest_reading(typ)

if __name__ == '__main__':
    build_ui(app, elastic, config.BUILD)
    app.run(debug=config.DEBUG)

# Juno
A basic dashboard to display various IoT sensor readings via Flask and Pyxley libraries backed by Elasticsearch.
A work in progress.

## start app
- create config/config.py based on config/config_example.py
- pip install -r requirements.txt
- cd juno
- python app.py
- or via gunicorn
    - gunicorn --bind 0.0.0.0:5000 --worker-class gevent -w 2 --log-level DEBUG app:app
    
## update config BUILD = True to rebuild the javascript files
## update config DEBUG = True to run in debug mode



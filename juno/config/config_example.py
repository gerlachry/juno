BUILD = False
DEBUG = False

ES_HOST = 'localhost'
ES_PORT = '9200'

INDEXES = {'Basement Temperature': 'basement_temperature',
           'Basement Humidity': 'basement_humidity'}
FIELDS = {
    'Basement Temperature': 'temperature',
    'Basement Humidity': 'humidity'
}

AVG_QUERY = {
    "aggs": {
        "per_day": {
            "date_histogram": {
                "field": "timestamp",
                "interval": "day"
            },
        }
    }
}

import logging
from datetime import datetime

from elasticsearch import Elasticsearch
import pandas as pd

INDEXES = {'Basement Temperature': 'basement_temperature',
           'Basement Humidity': 'basement_humidity'}
AVG_QUERY = {
            "aggs": {
                "per_day": {
                    "date_histogram": {
                        "field": "timestamp",
                        "interval": "day"
                    },
                    "aggs": {
                        "avg_temp": {
                            "avg": {
                                "field": "temperature"
                            }
                        },
                        "avg_humidity": {
                            "avg": {
                                "field": "humidity"
                            }
                        }
                    }
                }
            }
        }


class ESHelper(object):
    def __init__(self, host, port):
        self.es = Elasticsearch(host=host, port=port)
        self.logger = logging.getLogger(__name__)

    def get_data(self, args, timeseries=False):
        typ = args['Data']
        results = self.es.search(index=INDEXES[typ], body=AVG_QUERY)
        data = []
        for bucket in results['aggregations']['per_day']['buckets']:
            dt = datetime.strptime(bucket['key_as_string'], '%Y-%m-%dT%H:%M:%S.%fZ')
            if typ == 'Basement Temperature' and bucket['avg_temp']['value']:
                data.append({'x': dt.strftime('%Y-%m-%d'),
                             'y': bucket['avg_temp']['value']})
            elif typ == 'Basement Humidity' and bucket['avg_humidity']['value']:
                data.append({'x': dt.strftime('%Y-%m-%d'),
                       'y': bucket['avg_humidity']['value']})
        return {'result': [data, ], 'date': timeseries}

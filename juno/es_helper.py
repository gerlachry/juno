import logging
from datetime import datetime

from elasticsearch import Elasticsearch
import pandas as pd

class ESHelper(object):
    def __init__(self, host, port):
        self.es = Elasticsearch(host=host, port=port)
        self.logger = logging.getLogger(__name__)

    def test(self):
        query = {"query": {
            "match_all": {}
            },
            "size": 5,
            "sort":  [
                {
                  "timestamp": {
                    "order": "desc"
                  }
                }
            ]
        }
        results = self.es.search(index='basement_temperature', body=query)
        return results

    def test_df(self):
        # query = {"query": {
        #     "match_all": {}
        #     },
        #     "size": 5,
        #     "sort":  [
        #         {
        #           "timestamp": {
        #             "order": "desc"
        #           }
        #         }
        #     ]
        # }
        query = {
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
                                "field": "humidiry"
                            }
                        }
                    }
                }
            }
        }
        results = self.es.search(index='basement_*', body=query)
        data = []
        for bucket in results['aggregations']['per_day']['buckets']:
            dt = datetime.strptime(bucket['key_as_string'], '%Y-%m-%dT%H:%M:%S.%fZ')
            data.append({'Basement Temperature': bucket['avg_temp']['value'],
                         'Basement Humidity': bucket['avg_humidity']['value'],
                         'Date': dt.strftime('%Y-%m-%d')})
        df = pd.DataFrame(data=data)
        return df

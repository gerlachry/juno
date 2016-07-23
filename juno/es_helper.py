import logging

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
        data = []
        for rec in results['hits']['hits']:
            data.append({'Basement Temperature': rec['_source']['temperature'], 'Date': rec['_source']['timestamp']})
        return pd.DataFrame(data=data)

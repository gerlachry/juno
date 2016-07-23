import logging

from elasticsearch import Elasticsearch


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

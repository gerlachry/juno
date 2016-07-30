import logging
from datetime import datetime
from flask import request, jsonify
from elasticsearch import Elasticsearch
from config import config


class ESHelper(object):
    def __init__(self, host, port):
        self.es = Elasticsearch(host=host, port=port)
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def _build_agg_query(typ):
        """helper method to build aggregation query for sensors"""
        query = config.AVG_QUERY
        query['aggs']['per_day']['aggs'] = {
            'avg_' + config.INDEXES[typ]['avg_field']: {
                'avg': {
                    'field': config.INDEXES[typ]['avg_field']
                }
            }
        }
        return query

    @staticmethod
    def _build_latest_query(typ):
        """helper method to build latest record from an index based on timestamp field"""
        return  {
              "query": {
                "match_all": {}
              },
              "size": 1,
              "sort": [
                {
                  config.INDEXES[typ]['latest_field']: {
                    "order": "desc"
                  }
                }
              ]
            }


    def get_data(self):
        """get aggregated sensor reading data based on the request Data filter parameter"""
        typ = request.args['Data']
        results = self.es.search(index=config.INDEXES[typ]['index'], body=self._build_agg_query(typ))
        data = []
        for bucket in results['aggregations']['per_day']['buckets']:
            dt = datetime.strptime(bucket['key_as_string'], '%Y-%m-%dT%H:%M:%S.%fZ')
            fld = config.INDEXES[typ]['avg_field']
            if bucket['avg_' + fld]:
                data.append({'x': dt.strftime('%Y-%m-%d'),
                             'y': bucket['avg_' + fld]['value']})
        return jsonify({'result': [data, ], 'date': True})

    def get_latest_reading(self, typ):
        """return latest reading from given sensor based on timestamp field"""
        results = self.es.search(index=config.INDEXES[typ]['index'], body=self._build_latest_query(typ))
        return jsonify(results['hits']['hits'][0]['_source'])

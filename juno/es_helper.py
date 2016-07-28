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
    def _build_query(typ):
        query = config.AVG_QUERY
        query['aggs']['per_day']['aggs'] = {
            'avg_' + config.FIELDS[typ]: {
                'avg': {
                    'field': config.FIELDS[typ]
                }
            }
        }
        return query

    def get_data(self):
        typ = request.args['Data']
        results = self.es.search(index=config.INDEXES[typ], body=self._build_query(typ))
        data = []
        for bucket in results['aggregations']['per_day']['buckets']:
            dt = datetime.strptime(bucket['key_as_string'], '%Y-%m-%dT%H:%M:%S.%fZ')
            if bucket['avg_' + config.FIELDS[typ]]['value']:
                data.append({'x': dt.strftime('%Y-%m-%d'),
                             'y': bucket['avg_' + config.FIELDS[typ]]['value']})
        return jsonify({'result': [data, ], 'date': True})

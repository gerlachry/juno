import datetime
import time

from elasticsearch import Elasticsearch


def create_test_index():
    es = Elasticsearch(host='172.17.0.2', port='9200')
    temp = 66.0
    for i in range(0, 20):
        body = {
            'timestamp': datetime.datetime.now(),
            'temperature': temp,
            'feed_name': 'basement_temperature'
        }
        resp = es.index(index='basement_temperature', doc_type='sensor', id=None,  body=body)
        print(resp)
        temp += .5
        time.sleep(30)

if __name__ == '__main__':
    create_test_index()
import datetime
import time

from elasticsearch import Elasticsearch


def create_test_index():
    es = Elasticsearch(host='172.17.0.2', port='9200')
    temp = 75.0
    humidity = 22.0
    for i in range(0, 2):
        body = {
            'timestamp': datetime.datetime.now(),
            'temperature': temp,
            'feed_name': 'basement_temperature'
        }
        bodyH = {
            'timestamp': datetime.datetime.now(),
            'humidity': humidity,
            'feed_name': 'basement_humidity'
        }
        resp = es.index(index='basement_temperature', doc_type='sensor', id=None,  body=body)
        respH = es.index(index='basement_humidity', doc_type='sensor', id=None,  body=bodyH)

        print(resp)
        print(respH)

        temp += .5
        humidity += .5
        time.sleep(30)

if __name__ == '__main__':
    create_test_index()
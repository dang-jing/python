# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch


def a():
    es = Elasticsearch(['192.168.3.10:9200'])
    doc_body = {
        'question_types': "解答题"
    }
    print(es.index(index='pz',id=2,body=doc_body))


if __name__ == '__main__':
    a()

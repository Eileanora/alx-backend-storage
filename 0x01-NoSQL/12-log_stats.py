#!/usr/bin/env python3
''' Module to log stats from Nginx logs stored in MongoDB '''
from pymongo import MongoClient


def log_stats(mongo_collection):
    ''' Function that prints stats about Nginx logs stored in MongoDB '''
    print('{} logs'.format(mongo_collection.count_documents({})))
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, count))

    status_check = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})

    print('{} status check'.format(status_check))


if __name__ == "__main__":
    mongo_client = MongoClient('mongodb://127.0.0.1:27017')
    log_stats(mongo_client.logs.nginx)

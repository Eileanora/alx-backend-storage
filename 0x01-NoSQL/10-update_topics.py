#!/usr/bin/env python3
''' Module for function update_topics '''


def update_topics(mongo_collection, name, topics):
    ''' Updates all documents in a collection based on name '''
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

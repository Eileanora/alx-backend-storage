#!/usr/bin/env python3
''' Module for function insert_school '''


def insert_school(mongo_collection, **kwargs):
    ''' Inserts a new document in a collection based on kwargs '''
    val = mongo_collection.insert_one(kwargs)
    return val.inserted_id

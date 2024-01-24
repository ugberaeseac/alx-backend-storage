#!/usr/bin/env python3
"""
Python function that inserts a new document
in a collection based on kwargs
mongo_collection is the pymongo collection object
returns the new insertion id (_id)
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts new document to collection
    """
    doc_id = mongo_collection.insert_one(kwargs).inserted_id
    return doc_id

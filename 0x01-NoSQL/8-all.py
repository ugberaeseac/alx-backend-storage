#!/usr/bin/env python3
"""
function that lists all documents in a collection
returns an empty list if no document in the collection
"""


def list_all(mongo_collection):
    """
    list all documents in collection
    """
    if mongo_collection is not None:
        return mongo_collection.find()
    else:
        return []

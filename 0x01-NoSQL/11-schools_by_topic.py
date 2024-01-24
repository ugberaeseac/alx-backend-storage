#!/usr/bin/env python3
"""
function that returns the list of school having a specific topi
"""


def schools_by_topic(mongo_collection, topic):
    """
    return list of school having specific topic
    """
    query = mongo_collection.find({"topics": topics})
    return query

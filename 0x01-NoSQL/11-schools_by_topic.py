#!/usr/bin/env python3
"""list docs with filtered query match in array value"""


def schools_by_topic(mongo_collection, topic):
    """lists the school with topic in the topics"""
    query = {"topics": {"$elemMatch": {"$eq": topic}}}
    return [doc for doc in mongo_collection.find(query)]

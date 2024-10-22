#!/usr/bin/env python3
"""update documents to add topics"""


def update_topics(mongo_collection, name, topics):
    """updates mongo_collection to add topics to docs with key, name"""
    mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
        )

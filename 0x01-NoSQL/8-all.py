#!/usr/bin/env python3
"""list all docs in a mongodb collection"""


def list_all(mongo_collection):
    for doc in mongo_collection.find():
        yield doc

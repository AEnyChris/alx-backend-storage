#!/usr/bin/env python3
"""insert a dict obj in to collection"""


def insert_school(mongo_collection, **kwargs):
    """insert dict kwargs into mongo_collection"""
    if kwargs:
        return mongo_collection.insert_one(kwargs).inserted_id

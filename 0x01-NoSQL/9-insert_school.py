#!/usr/bin/env python3
"""
This module contains a function that inserts a new document based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
     Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Arbitrary keyword arguments representing
        the document's fields.

    Returns:
        The new _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

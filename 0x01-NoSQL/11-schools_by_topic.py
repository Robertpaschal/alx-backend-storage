#!/usr/bin/env python3
"""
"""


def schools_by_topic(mongo_collection, topic):
    """
    """
    result = list(mongo_collection.find(
        {"topics": topic}
    ))
    return result

#!/usr/bin/env python3
"""
This module contains a function  that
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    This function returns the list of school having a specific topic
    """
    result = list(mongo_collection.find(
        {"topics": topic}
    ))
    return result

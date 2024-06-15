#!/usr/bin/env python3
"""
This module contains a Python function that
returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of students sorted by average score.
    """
    pipeline = [
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "averageScore": {"$avg": {"$avg": "$topics.score", }, },
                "topics": 1,
            },
        },
        {"$sort": {"averageScore": -1}}
    ]

    return list(mongo_collection.aggregate(pipeline))

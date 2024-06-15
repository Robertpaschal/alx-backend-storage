#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def log_stats():
    """
    Provide stats about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    log_count = nginx_collection.count_documents({})
    print('{} logs'. format(log_count))

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents(
            {"method": method}
        )
        print(f"\tmethod {method}: {count}")

    status_check_count = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print("{} status check". format(status_check_count))


if __name__ == "__main__":
    log_stats()

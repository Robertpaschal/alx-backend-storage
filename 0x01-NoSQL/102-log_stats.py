#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB
and
adds the top 10 of the most present IPs in the collection.
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

    print("IPs:")

    pipeline = [
        {"$group": {"_id": "$ip", "totalRequests": {"$sum": 1}}},
        {"$sort": {"totalRequests": -1}},
        {"$limit": 10}
    ]
    top_ips = list(nginx_collection.aggregate(pipeline))
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['totalRequests']}")


if __name__ == "__main__":
    log_stats()

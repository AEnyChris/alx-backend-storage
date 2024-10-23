#!/usr/bin/env python3
"""log parsing with mongodb and Python"""

if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient()
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")

    print(f"Methods:")
    for method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        method_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")

    status_count = collection.count_documents(
                {
                    '$and': [
                        {'method': 'GET'},
                        {'path': '/status'}
                    ]
                }
            )
    print(f"{status_count} status check")

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

    print("IPs:")
    request_logs = collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in request_logs:
        ip = request_log['_id']
        ip_requests_count = request_log['totalRequests']
        print('\t{}: {}'.format(ip, ip_requests_count))

#!/usr/bin/env python
from pymongo import MongoClient

client = MongoClient('localhost:27017')

db = client.examples

def user_mentions():
    result = db.twitter.aggregate([
    {"$unwind":"$entities.user_mentions"},
    {"$group":{"_id":"$user.screen_name",
               "count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":1} ])

    return result

if __name__ == '__main__':
    result = user_mentions()
    import pprint
    pprint.pprint(result)

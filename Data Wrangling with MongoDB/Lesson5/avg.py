#!/usr/bin/env python
from pymongo import MongoClient

client = MongoClient('localhost:27017')

db = client.examples

def avg_retweet():
    result = db.twitter.aggregate([
    {"$unwind":"$entities.hashtags"},
    {"$group":{"_id":"$entities.hashtags.text",
               "retweet_avg":{"$avg":"$retweet_count"}}},
    {"$sort":{"retweet_avg":-1}}])
    return result

if __name__ == '__main__':
    result = avg_retweet()
    import pprint
    pprint.pprint(result)

#!/usr/bin/env python

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [
    {"$unwind":"$entities.user_mentions"},
    {"$group" : {
            "_id" : "$user.screen_name",
            "mset":{
                "$addToSet":"$entities.user_mentions.screen_name"}}},
    {"$unwind":"$mset"},
    {"$group":{
            "_id":"$_id",
            "count":{"$sum":1}}},
    {"$sort" : {"count" : -1}},
    {"$limit" : 5}]
    return pipeline

def aggregate(db, pipeline):
    result = db.tweets.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result)

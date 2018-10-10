# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo



class TongjiPipeline(object):

    def process_item(self, item, spider):
        client = pymongo.MongoClient(host="localhost", port=27017)
        db = client.babys
        coll = db.babys
        coll.insert(dict(item))
        client.close()
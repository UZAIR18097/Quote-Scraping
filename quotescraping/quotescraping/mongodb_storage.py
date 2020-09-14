# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

# scraper>>Item Container>>Pipelines>>Data base
import pymongo


class QuotescrapingPipeline(object):

    def __init__(self):
        # creates connection
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        # creates data base
        db = self.conn['myquotes']
        # creates table
        self.collection = db['quotes_tb']

    def process_item(self, item, spider):
        #store the table
        self.collection.insert(dict(item))
        return item

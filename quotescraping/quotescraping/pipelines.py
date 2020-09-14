# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

# scraper>>Item Container>>Pipelines>>Data base
import pymongo


class QuotescrapingPipeline(object):

    def process_item(self, item, spider):
        return item

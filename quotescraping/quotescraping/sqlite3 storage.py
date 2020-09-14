# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import _sqlite3
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# scraper>>Item Container>>Pipelines>>Data base

class QuotescrapingPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        # creating connection
        self.conn = _sqlite3.connect("myquotes.db")
        # activating cursor
        self.curr = self.conn.cursor()

    def create_table(self):
        # dont create tabel  if  exists
        self.curr.execute(""" DROP TABLE IF EXISTS quotes_tb""")

        # creating table
        self.curr.execute(""" create table quotes_tb(
                        title text,
                        author text,
                        tag text
                            ) """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    # storing data
    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values (?,?,?)""", (
            item['title'][0],
            item['author'][0],
            item['tag'][0],
        )
                          )
        self.conn.commit()

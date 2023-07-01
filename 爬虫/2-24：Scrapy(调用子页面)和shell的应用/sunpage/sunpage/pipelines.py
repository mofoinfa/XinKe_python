# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class SunpagePipeline:
    def __init__(self):
        # self.f = open('movie.txt', 'w', encoding='utf-8')
        self.cli = pymongo.MongoClient()
        self.db = self.cli.DouBan_data
        self.col = self.db.message

    def process_item(self, item, spider):
        # print(123)
        self.col.insert_one(dict(item))
        # self.f.write(str(item)+'\n')
        return item

    # def __del__(self):
    #     self.f.close()

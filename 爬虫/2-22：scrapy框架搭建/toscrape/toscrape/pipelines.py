# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ToscrapePipeline:
    def __init__(self):
        self.f = open('goodWord.txt', 'w')

    def process_item(self, item, spider):
        self.f.write(str(item)+'\n')
        return item

    def __del__(self):
        self.f.close()

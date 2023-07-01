# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


class DuitangPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        requests_list = []
        urls = super().get_media_requests(item, info)
        for index, i in enumerate(urls):
            i.name = item['name'][index]
            requests_list.append(i)
        return requests_list

    def file_path(self, request, response=None, info=None, *, item=None):
        return f'{request.name}.jpg'
    # def process_item(self, item, spider):
    #     urls = super.get_media_requests(self, item, info)
    #     return item

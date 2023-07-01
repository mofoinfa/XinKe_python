# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JdMsgPipeline:
    def __init__(self):
        self.f = open('JD_data.txt', 'w', encoding='utf-8')
        self.f.write('京东数据信息\n')

    def process_item(self, item, spider):
        self.f = open('JD_data.txt', 'a', encoding='utf-8')
        # print(item['big_title'])
        self.f.write('--------------大标题------------------\n')
        for i in item['big_title']:
            self.f.write(i + '\n')
        self.f.write('--------------中标题------------------\n')
        for i in item['mid_title']:
            self.f.write(i + '\n')
        self.f.write('--------------小标题------------------\n')
        for i in item['min_title']:
            self.f.write(i + '\n')
        self.f.write('--------------页面详情------------------\n')
        for name, price in zip(item['name'], item['price']):
            if price == '':
                self.f.write(f'商品名称：{name}     商品价格：商品已下架\n')
            else:
                self.f.write(f'商品名称：{name}     商品价格(元)：{price}\n')
        return item

    def __del__(self):
        self.f.close()

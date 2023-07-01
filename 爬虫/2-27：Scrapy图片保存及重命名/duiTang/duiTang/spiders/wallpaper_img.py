import scrapy
from ..items import DuitangItem


class WallpaperImgSpider(scrapy.Spider):
    name = "wallpaper_img"
    allowed_domains = ["www.duitang.com"]
    start_urls = [
        "https://www.duitang.com/napi/blog/list/by_search/?include_fields=like_count%2Csender%2Calbum%2Cmsg%2Creply_count%2Ctop_comments&kw=%E5%A3%81%E7%BA%B8&start=0&_=1677997808893"]

    def parse(self, response):
        item = DuitangItem()
        img_data = response.json()["data"]["object_list"]
        image_urls = []
        image_ids = []
        for i in img_data:
            image_urls.append(i["photo"]["path"])
            image_ids.append(str(i["photo"]["id"]))
        item['image_urls'] = image_urls
        item['name'] = image_ids
        yield item

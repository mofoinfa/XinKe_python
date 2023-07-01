import re

import scrapy
from ..items import DoubanItem


class MovieMsgSpider(scrapy.Spider):
    name = "movie_msg"
    allowed_domains = ["movie.douban.com"]
    start_urls = [f"https://movie.douban.com/j/chart/top_list?type=24&interval_id=100:90&action=&start={i}&limit=20"
                  for i in range(0, 20 * 10, 20)]

    def parse(self, response):
        items = DoubanItem()
        actor_count = re.findall('"actor_count":(.*?),', response.text)
        actors = re.findall('"actors":\[(.*?)\],', response.text)
        cover_urlstr = re.findall('"cover_url":(.*?),', response.text)
        id = re.findall('"id":(.*?),', response.text)
        is_playable = re.findall('"is_playable":(.*?),', response.text)
        is_watched = re.findall('"is_watched":(.*?)}', response.text)
        rank = re.findall('"rank":(.*?),', response.text)
        rating = re.findall('"rating":\[(.*?)\],', response.text)
        regions = re.findall('"regions":(.*?),', response.text)
        release_date = re.findall('"release_date":(.*?),', response.text)
        score = re.findall('"score":(.*?),', response.text)
        title = re.findall('"title":(.*?),', response.text)
        types = re.findall('"types":\[(.*?)\],', response.text)
        url = re.findall('"url":(.*?),', response.text)[0]
        vote_count = re.findall('"vote_count":(.*?),', response.text)

        for actor_count, actors, cover_urlstr, id, is_playable, is_watched, rank, \
            rating, regions, release_date, score, title, types, url, vote_count in \
                zip(actor_count, actors, cover_urlstr, id, is_playable, is_watched, rank,
                    rating, regions, release_date, score, title, types, url, vote_count):
            items['actor_count'] = actor_count
            items['actors'] = actors
            items['cover_url'] = str(cover_urlstr).replace('\\', '')
            items['id'] = id
            items['is_playable'] = is_playable
            items['is_watched'] = is_watched
            items['rank'] = rank,
            items['rating'] = rating
            items['regions'] = regions
            items['release_date'] = release_date
            items['score'] = score
            items['title'] = title
            items['types'] = types
            items['url'] = str(url).replace('\\', '')
            items['vote_count'] = vote_count
            yield items

# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    # 传入参数 scrapy crawl baidu -a category=jake
    def __init__(self, category=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category = category

    def make_requests_from_url(self, url):
        return scrapy.Request(url=url, callback=self.parse_index)

    def parse(self, response):
        pass

    def parse_index(self, response):
        print("***", self.category)
        print("hello ", response.url)

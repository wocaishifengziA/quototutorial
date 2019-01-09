# -*- coding: utf-8 -*-
import scrapy


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['www.google.com']
    start_urls = ['http://www.google.com/']

    def make_requests_from_url(self, url):
        return scrapy.Request(url=url, callback=self.parse, meta={'download_timeout': 5},dont_filter=False)

    def parse(self, response):
        pass

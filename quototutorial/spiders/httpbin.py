# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    # 改写 start_requests 为post请求
    # def start_requests(self):
    #     yield scrapy.Request(url='http://httpbin.org/post', method='POST', callback=self.parse_post, meta={'download_timeout': 10})

    # 在内部 遍历 start_urls 的所有 URL 重写后只返回一个Request对象
    # def start_requests(self):
    #     yield scrapy.Request(url='http://httpbin.org/get', callback=self.parse_post)

    def parse(self, response):
        print('**********************')
        print("hello", response.text)
        print(response.status)

    # def parse_post(self, response):
    #     print('hello post', response)

# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']
    def __init__(self,httpname,httpage):
        self.httpname=httpname
        self.httpage=httpage
        print("httpname:",self.httpname)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            httpname=crawler.settings.get('NAME'),
            httpage=crawler.settings.get('AGE')
        )
    def parse(self, response):
        print("hello", self.httpname)
        print(response.text)
    def parse_index(self,response):
       # print("--------------"+httpname+"---------------")


        pass
    #def start_requests(self):
    #    yield scrapy.Request(url="http://httpbin.org/",callback=self.parse_index)



# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Selector
from tongji.items import TongjiItem
class GetdateSpider(scrapy.Spider):
    name = 'getdate'
    allowed_domains = ["list.tmall.com"]
    start_urls = ['https://list.tmall.com/search_product.htm?q=%BA%A3%C0%BD%D6%AE%BC%D2&type=p&vmarket=&spm=a221t.1710963.a2227oh.d100&from=nanzhuang..pc_1_searchbutton']

    def parse(self, response):
        div_list=response.xpath('//div[@class="product-iWrap"]')
        for i in div_list:
            item=TongjiItem()
            url= i.xpath('./p/a/@href').extract_first()
            at= i.xpath('./p/a/text()').extract_first()
            price=i.xpath('./p/em/@title').extract_first()
            item['url']=url
            item['a_Text']=at
            item['price']=price
            yield item
        base_url="https://list.tmall.com/search_product.htm"
        next=response.xpath('//a[@class="ui-page-next"]/@href').extract_first()
        next_url=base_url+next
        print("------------------------")
        print(next_url)
        print("------------------------")
        yield scrapy.Request(url=next_url,callback=self.parse)

#         quotes = response.css('.quote')
#         for quote in quotes:
#             item = TongjiItem()
#             item['url'] = quote.css('.text::text').extract_first()
#             item['a_Text'] = quote.css('.author::text').extract_first()
#             print("===========")
#             print(item)
#             print("===========")
#             yield item






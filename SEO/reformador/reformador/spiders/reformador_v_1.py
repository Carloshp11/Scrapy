# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from reformador.items import ReformadorItem


class ReformadorV1Spider(CrawlSpider):
    name = 'reformador_v.1'
    allowed_domains = ['www.reformador.es']
    start_urls = ['http://www.www.reformador.es/']

    # rules = (
    #     Rule(LinkExtractor(domain=r'www.reformador.es'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        item = ReformadorItem()
        item['body'] = response.css('body').extract() #Must be translated to text first
        return item

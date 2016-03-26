# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "milanuncios"
    allowed_domains = ["milanuncios.com"]
    start_urls = (
        'http://www.milanuncios.com/',
    )

    def parse(self, response):
        pass

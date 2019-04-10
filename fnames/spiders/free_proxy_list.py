# -*- coding: utf-8 -*-

#Web-crawler. Собирает данные с сайта https://free-proxy-list.net/ в формате 'IP:Port'.

import scrapy

class FreeProxyListSpider(scrapy.Spider):
    name = 'free-proxy-list'
    allowed_domains = ['free-proxy-list.net']
    start_urls = ['https://free-proxy-list.net/']

    def __init__(self, pathofsript=None):
        super().__init__()
        self.pathofsript = pathofsript

    def parse(self, response):
        
        pathofsript = self.pathofsript
       
        #Извлечение необходимых данных
        ipProxy = response.xpath('//tr/td[@class="hx" and text()="yes"]'
                                    '/parent::tr/td[text()="elite proxy"]'
                                    '/parent::tr/td[1]/text()').extract()
        
        portProxy = response.xpath('//tr/td[@class="hx" and text()="yes"]'
                                    '/parent::tr/td[text()="elite proxy"]'
                                     '/parent::tr/td[2]/text()').extract()


        resultProxy =   [(':'.join(list(map(str,iProxy)))) for iProxy in list(zip(ipProxy,portProxy))]

        nextPageUrl = response.xpath("//li[@class='fg-button ui-button ui-state-default next']/a/@href").extract_first()
        
        #Сохранение данных в 'proxies.txt'
        with open(pathofsript,'a') as f:
            for proxy in resultProxy:   
                f.write(proxy + '\n')
        
        #Переход по ссылке в нижней части таблицы. Если ссылка есть, повторение запроса и новое извлечение данных.
        if nextPageUrl:
            nextPageUrl = response.urljoin(nextPageUrl)
            yield scrapy.Request(url=nextPageUrl, callback = self.parse) 


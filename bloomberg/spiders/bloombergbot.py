# -*- coding: utf-8 -*-
import scrapy

class BloombergbotSpider(scrapy.Spider):
    name = 'bloombergbot'
    allowed_domains = ['https://www.bloomberg.com/markets/stocks']
    start_urls = ['https://www.bloomberg.com/markets/stocks/']


    def parse(self, response):
            #Extracting the content using css selectors
            name = response.css('.table-container .data-table-row-cell__link-block[data-type*=abbreviation]::text').extract()
            value = response.css('.table-container .data-table-row-cell[data-type*=value]::text').extract()
            change = response.css('.table-container .data-table-row-cell[data-type*=better]::text').extract()
            close = response.css('.table-container .data-table-row-cell[data-type*=time]::text').extract()
        
            #Give the extracted content row wise
            for item in zip(name,value,change,close):
                #create a dictionary to store the scraped info
                scraped_info = {
                    'name':item[0],
                    'value':item[1],
                    'change':item[2],
                    'close':item[3],
                }

                #yield or give the scraped info to scrapy
                yield scraped_info
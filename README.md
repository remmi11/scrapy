scrapy startproject bloomberg
-----------------------------

scrapy genspider bloombergbot https://www.bloomberg.com/markets/stocks
-----------------------------

edit bloombergbot.py
-----------------------------

Add the selectors
```
name = response.css('.table-container .data-table-row-cell__link-block[data-type*=abbreviation]::text').extract()
value = response.css('.table-container .data-table-row-cell[data-type*=value]::text').extract()
change = response.css('.table-container .data-table-row-cell[data-type*=better]::text').extract()
close = response.css('.table-container .data-table-row-cell[data-type*=time]::text').extract()
```
####zip the response into a dictionary and yield

```
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
```
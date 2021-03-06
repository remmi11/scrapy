Initialize the project
-----------------------------
`scrapy startproject bloomberg`

Initialize the spider
-----------------------------
`scrapy genspider bloombergbot https://www.bloomberg.com/markets/stocks`

Edit bloombergbot.py
-----------------------------

Add the selectors
```
name = response.css('.table-container .data-table-row-cell__link-block[data-type*=abbreviation]::text').extract()
value = response.css('.table-container .data-table-row-cell[data-type*=value]::text').extract()
change = response.css('.table-container .data-table-row-cell[data-type*=better]::text').extract()
close = response.css('.table-container .data-table-row-cell[data-type*=time]::text').extract()
```

zip the response into a dictionary and yield

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

Modify settings.py to generate csv
-----------------------------
```
#Export as CSV Feed
FEED_FORMAT = "csv"
FEED_URI = "bloomberg.csv"
```

Final Results
-----------------------------

![](https://content.screencast.com/users/wtgeographer/folders/Jing/media/331b25ee-ec22-49ae-9983-014b49a7465c/2018-01-02_2347.png)<!-- .element height="50%" width="50%" -->
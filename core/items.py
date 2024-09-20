import scrapy


class GetDatasFromApiItem(scrapy.Item):
    title = scrapy.Field()
    current_price = scrapy.Field()
    old_price = scrapy.Field()
    image_link = scrapy.Field()
    availability = scrapy.Field()
    page_url = scrapy.Field()


class GetDatasFromSitemapItem(scrapy.Item):
    title = scrapy.Field()
    current_price = scrapy.Field()
    old_price = scrapy.Field()
    image_link = scrapy.Field()
    availability = scrapy.Field()
    page_url = scrapy.Field()

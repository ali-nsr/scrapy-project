import scrapy


class GetProductsFromApiItem(scrapy.Item):
    title = scrapy.Field()
    current_price = scrapy.Field()
    old_price = scrapy.Field()
    image_link = scrapy.Field()
    availability = scrapy.Field()
    page_url = scrapy.Field()

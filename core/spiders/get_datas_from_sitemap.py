import scrapy
from scrapy.spiders import XMLFeedSpider
from core.items import GetDatasFromSitemapItem


class GetDatasFromSitemapSpider(XMLFeedSpider):
    name = 'get_products_from_sitemap_spider'

    custom_settings = {
        'ITEM_PIPELINES': {
            'core.pipelines.GetDatasFromSitemapPipeline': 300
        }
    }

    namespaces = [('n', 'http://www.sitemaps.org/schemas/sitemap/0.9')]
    itertag = 'n:url'
    iterator = 'xml'

    def __init__(self, start_url, *args, **kwargs):
        super(GetDatasFromSitemapSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]  # start_urls must start with pagination
        self.s_url = start_url

    def parse_node(self, response, node):
        links = node.xpath('.//n:loc/text()')
        for link in links:
            yield scrapy.Request(link.get(), callback=self.parse_product)

    def parse_product(self, response):
        items = GetDatasFromSitemapItem()
        try:
            items['title'] = response.xpath("//meta[@name='product_name']/@content")[0].get()
            items['current_price'] = response.xpath("//meta[@name='product_price']/@content")[0].get()
            items['old_price'] = response.xpath("//meta[@name='product_old_price']/@content")[0].get()
            items['image_link'] = response.xpath("//meta[@property='og:image']/@content")[0].get()
            items['availability'] = response.xpath("//meta[@name='availability']/@content")[0].get()
            items['page_url'] = response.request.url

            yield items

        except Exception as e:
            print(e)

import scrapy
import json
from core.items import GetDatasFromApiItem


class GetDatasFromApiSpider(scrapy.Spider):
    name = 'get_datas_from_api_spider'

    custom_settings = {
        'ITEM_PIPELINES': {
            'core.pipelines.GetDatasFromApiPipeline': 300
        }
    }

    def __init__(self, start_url, *args, **kwargs):
        super(GetDatasFromApiSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url + str(1)]  # start_urls must start with pagination
        self.s_url = start_url

    def parse(self, response, **kwargs):
        items = GetDatasFromApiItem()
        data = json.loads(response.text)
        current_page = 1
        end_page = int(data['total_pages_count'])
        for product in data['products']:
            items['title'] = product['title']
            items['image_link'] = product['image_link']
            items['availability'] = product['availability']
            items['page_url'] = product['page_url']
            items['current_price'] = 0 if product['current_price'] is None else product['current_price']
            items['old_price'] = 0 if product['current_price'] is None else product['current_price']

        while current_page < end_page + 1:
            current_page += 1
            yield response.follow(self.s_url + str(current_page), callback=self.parse)

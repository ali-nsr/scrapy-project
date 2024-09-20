import sqlite3


class GetProductsFromApiPipeline:
    def __init__(self):
        self.conn = sqlite3.connect('datas.db')
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS datas (
        title TEXT NOT NULL,
        current_price INTEGER NOT NULL,
        old_price INTEGER NOT NULL,
        image_link TEXT NOT NULL,
        availability TEXT NOT NULL,
        page_url TEXT NOT NULL
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute("""
        INSERT OR IGNORE INTO datas VALUES (?,?,?,?,?,?)
        """, (item['title'], item['current_price'], item['old_price'], item['image_link'], item['availability'],
              item['page_url']))

        self.conn.commit()
        return item

        # if you are using django with scrapy you can do this

        # YourModel.objects.update_or_create(
        #     title=item['title'],
        #     defaults={
        #         'current_price': 0 if item['current_price'] is None else int(item['current_price']),
        #         'old_price': 0 if item['old_price'] is None else int(item['old_price']),
        #         'image_link': item['image_link'],
        #         'availability': item['availability'],
        #         'page_url': item['page_url']
        #     }
        # )

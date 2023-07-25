import scrapy
import pymongo

class Kitapyurdu1Spider(scrapy.Spider):


    # MongoDB bağlantı URL'sini belirtin
    # Varsayılan olarak MongoDB localhost ve 27017 portunda çalışır
    mongo_url = "mongodb://localhost:27017/"

    # MongoDB'ye bağlanın
    client = pymongo.MongoClient(mongo_url)

    db = client["smartmaple"]

    collection = db["kitapyurdu"]
    name = "kitapyurdu_1"
    start_urls = ["https://www.kitapyurdu.com/index.php?route=product/category/&filter_category_all=true&category_id=128&sort=purchased_365&order=DESC&filter_in_stock=1"]

    def parse(self, response):
        books = response.xpath('//div[@class="product-cr"]')

        for book in books:
            title = book.xpath('.//div[@class="name ellipsis"]//a//text()').extract()
            publisher = book.xpath('.//div[@class="publisher"]//a//text()').extract()
            writers = book.xpath('.//div[@class="author"]//a//text()').extract()
            price = book.xpath('.//div[@class="price"]//span[@class="value"]/text()').extract()

            # İsteğe bağlı olarak diğer bilgileri de çıkarmak için kodları ekleyebilirsiniz.

            data = {
                "title": title[0],
                "publisher": publisher[0],
                "writers": writers[1],
                "price": price[1]
            }
            self.collection.insert_one(data)

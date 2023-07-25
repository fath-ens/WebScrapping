import scrapy
import pymongo

class Kitapsepeti1Spider(scrapy.Spider):
    mongo_url = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(mongo_url)
    db = client["smartmaple"]
    collection = db["kitapsepeti"]
    name = "kitapsepeti_1"
    start_urls = ["https://www.kitapsepeti.com/roman"]

    def parse(self, response):
        books = response.xpath('//div[@class="col col-3 col-md-4 col-sm-6 col-xs-6 p-right mb productItem zoom ease"]')

        for book in books:
            title = book.xpath('.//div[@class="col col-12 productDetails loaderWrapper"]//div[@class="row drop-down-title"]//div[@class="box col-12 text-center"]//a[@class="fl col-12 text-description detailLink"]//text()').get().strip()
            publisher = book.xpath('.//div[@class="col col-12 productDetails loaderWrapper"]//div[@class="row drop-down-title"]//div[@class="box col-12 text-center"]//a[@class="col col-12 text-title mt"]//text()').get().strip()
            writers = book.xpath('.//div[@class="col col-12 productDetails loaderWrapper"]//div[@class="row drop-down-title"]//div[@class="box col-12 text-center"]//a[@class="fl col-12 text-title"]//text()').getall()
            price = book.xpath('.//div[@class="col col-12 productDetails loaderWrapper"]//div[@class="row drop-down-title"]//div[@class="box col-10 col-ml-1 col-sm-12 proRowAct"]//div[@class="fl col-12 tooltipWrapper"]//div[@class="fl col-12 d-flex productPrice"]//div[@class="fl col-12 priceWrapper"]//div[@class="col col-12 currentPrice"]//text()').get().strip()

            data = {
                "title" : title,
                "publisher" : publisher,
                "writers" : writers,
                "price" : price.replace("\n", "")
            }

            self.collection.insert_one(data)




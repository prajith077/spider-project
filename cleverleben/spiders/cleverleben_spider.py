import scrapy

class CleverlebenSpider(scrapy.Spider):
    name = "cleverleben"
    start_urls = ["https://www.cleverleben.at/produktauswahl"]

    def parse(self, response):
        for product_url in response.css("a::attr(href)").getall():
            if "/produkt/" in product_url:
                yield response.follow(product_url, callback=self.parse_product)

    def parse_product(self, response):
        yield {
            "product_name": response.css("h1::text").get(default="").strip(),
            "price": response.css(".product__price::text").get(default="").strip(),
            "description": " ".join(response.css(".product__description *::text").getall()).strip(),
            "image_url": response.urljoin(response.css(".product__image img::attr(src)").get(default="")),
            "product_url": response.url,
        }


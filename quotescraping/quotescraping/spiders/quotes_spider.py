import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotescrapingItem


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/login"
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            "csrf_token": token,
            "username": 'abcd@gmail.com',
            "password": 'dndijcn'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
        item = QuotescrapingItem()
        # title = response.css('title::text').get()
        # response.xpath("//title/text()").get()
        # quote = response.css('span.text::text').get()
        # response.xpath("//span[@class = 'text']/text()").get()
        div_quotes = response.css("div.quote")
        # looping for presenting one quote one author and tags
        for quote in div_quotes:
            title = quote.css("span.text::text").getall()
            author = quote.css("small.author::text").getall()
            tag = quote.css(".tag::text").getall()
            # storing in containers
            item['title'] = title
            item['author'] = author
            item['tag'] = tag

            yield item

import scrapy
from ..items import QuotescrapingItem


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    page_number = 2
    start_urls = [
        "http://quotes.toscrape.com/page/1/"
    ]

    def parse(self, response):
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
        # scraping the next page
        next_page = 'http://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'
        # checking if next page is there,if it is then parse to next page and extract quotes
        if QuoteSpider.page_number < 10:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

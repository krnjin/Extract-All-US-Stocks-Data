from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem

class StackSpider(Spider):
    name = "companiesmarketcap"
    allowed_domains = ["companiesmarketcap.com"]
    start_urls = [
        "https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/?page=1",
    ]

    def parse(self, response):
        todays_price = Selector(response).xpath('//table[@class="table marketcap-table dataTable"]/tbody/tr')

        for price in todays_price:
            item = StackItem()
            item['price'] = price.xpath('td[@class="rh-sm"]/span/text()').extract()[0]
            yield item
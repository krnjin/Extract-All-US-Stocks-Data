from scrapy import Spider

class StackSpider(Spider):
    name = "companiesmarketcap"
    allowed_domains = ["companiesmarketcap.com"]
    start_urls = [
        "https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/?page=1",
    ]

    def parse(self, response):
        todays_price = Selector(response).xpath('//td[@class="rh-sm"]/span')
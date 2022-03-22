import scrapy
from ..items import AwwwardsItem
from urllib.parse import urljoin


class AwwwardsSpider(scrapy.Spider):
    name = 'awwwards'
    # Allowed domain name
    allowed_domains = ['awwwards.com']
    # The entrance URL to the website
    start_urls = ['http://www.awwwards.com/websites/css3']

    def parse(self, response, *args, **kwargs):
        for i in range(5):
            # Scrapy the first 5 pages information
            web_list = response.xpath(
                "//div[@class='inner search-container']//div[@class='grid js-grid']//ul[@class='list-items list-flex js-elements-container']/li[@class='col-3 js-collectable']")

            for item in web_list:
                web_item = AwwwardsItem()
                web_item['web_name'] = item.xpath(
                    ".//div[@class='box-item']//div[@class='box-info']//div[@class='content']//div[@class='row']/h3/a/text()").extract_first()
                web_item['web_tag'] = item.xpath(
                    ".//div[@class='box-item']//div[@class='box-info']//div[@class='footer style2']//div[@class='box-right']//ul[@class='list-tags size-small no-border']//li//div[@class='tooltip']//span/text()").extract()
                web_item['web_author'] = item.xpath(
                    ".//div[@class='box-item']//div[@class='box-info']//div[@class='footer style2']//div[@class='box-left']//div[@class='box-byuser js-tooltip-user']//div[@class='by']/strong/a/text()").extract_first()
                web_item['web_date'] = item.xpath(
                    ".//div[@class='box-item']//div[@class='box-info']//div[@class='content']//div[@class='row row-2col']/div[@class='box-right']/text()").extract_first()
                relative_URL = item.xpath(
                    ".//div[@class='box-item']//figure[@class='rollover ']/a/@href").extract_first()
                URL = "https://www.awwwards.com"
                web_item['web_URL'] = urljoin(URL, relative_URL)
                web_item['web_tag'] = item.xpath(
                    ".//div[@class='box-item']//div[@class='box-info']//div[@class='footer style2']//div[@class='box-right']//ul[@class='list-tags size-small no-border']//li//div[@class='tooltip']//span/text()").extract()

                print(web_item)
                yield web_item

            # Turn to the next page
            next_page = response.xpath("//div[@class='paginate']/div[@class='col-3'][2]/@href").extract()
            if next_page:
                next_page = next_page[0]
                yield scrapy.Request("https://www.awwwards.com/websites/css3" + next_page, callback=self.parse)

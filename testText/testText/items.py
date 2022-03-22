# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class AwwwardsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # The name of each example website of best design with CSS
    web_name = scrapy.Field()

    # The tag of each example website
    web_tag = scrapy.Field()

    # The author of each example website
    web_author = scrapy.Field()

    # The build date of each example website
    web_date = scrapy.Field()

    # The URL of each example website
    web_URL = scrapy.Field()



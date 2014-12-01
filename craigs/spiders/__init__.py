# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.spider import Spider
from craigs.items import CraigsItem
import pymongo
import datetime
from datetime import datetime
from pymongo import MongoClient


class BookSpider(Spider):
  name = "craig"
  allowed_domains = ["craigslist.org"]
  start_urls = ["http://newyork.craigslist.org/bka"]

  def parse(self, response):
    titles = response.xpath("//a")
    link_set = []
    for link in titles:
      item = CraigsItem()
      item["link"] = link.xpath("@href").extract()
      item["text"] = link.xpath("text()").extract()
      item["timestamp_audit"] = "eval(new Date();)"
      if len(link_set) == 100:
        return link_set
      else:
        link_set.append(item)

class BarterSpider(Spider):
  name = "barter"
  allowed_domains = ["craigslist.org"]
  start_urls = ["http://newyork.craigslist.org/bar/"]

  def parse(self, response):
    client = MongoClient("localhost", 27017)
    db = client.craigslist
    titles = response.xpath("//a")
    link_set = []
    i = 0
    for link in titles:
      if i == 100:
        break
      else:
        item = {}
        item['link'] = link.xpath("@href").extract()
        item['text'] = link.xpath("text()").extract()
        item['timestamp_audit'] = datetime.now()
        db.barter.insert(item)
        i += 1
        # db.barter.insert(item)


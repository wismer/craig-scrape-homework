# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.spider import Spider
from craigs.items import CraigsItem

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
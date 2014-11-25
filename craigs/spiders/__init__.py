# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.


from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigs.items import CraigsItem

class BookSpider(BaseSpider):
  name = "craig"
  allowed_domains = ["craigslist.org"]
  start_urls = ["http://newyork.craigslist.org/search/bka"]

  def link_text(self, link):
    return link.select("/text()").extract()

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    titles = hxs.select("//a")
    list = []
    for link in titles:
      link_href = link.select("@href").extract()
      print(self.link_text(link))

      # craig_item = CraigsItem()
      # text = titles.select("a/text()").extract()
      # if text == []:

      # craig_item['text'] = titles.select("a/text()").extract()
      # craig_item['link'] = titles.select("a/@href").extract()
      # print(link)

      # if titles.select("a/text()").extract() == "":
      #   print(link)
      # title = titles.select("a/text()").extract()
      # lnk = titles.select("a/@href").extract()
      # print(title, lnk)
      # print(link)
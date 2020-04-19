import scrapy 

def cleanText(text):
    if text:
        return text.strip()

class ActusSpider(scrapy.Spider):
    name = "actus"

    start_urls = ["http://www.jeuxvideo.com/"]

    def parse(self, response):
        # self.logger.info('hello this is my first spider')
        actus = response.css("article.item-home-accroche")

        for actu in actus:
            t = cleanText(actu.css('.mtag::text').get())
            title = cleanText(actu.css('.titre-wrapper > a::text').get())
            link = cleanText(actu.css('.titre-wrapper > a::attr(href)').get())
            date = cleanText(actu.css('.date-li::text').get())
            comments = cleanText(actu.css('.nombre::text').get())

            yield {
                'type': t,
                'title': title,
                'link': link,
                'date': date,
                'comments': comments,
            }
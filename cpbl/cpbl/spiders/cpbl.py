import scrapy
from scrapy_splash import SplashRequest
from cpbl.items import CpblItem


class AppleCrawler(scrapy.Spider):
    name = 'cpbl'
    allowed_domains = ['cpbl.com.tw']
    start_url = 'http://www.cpbl.com.tw/stats/all.html?year=0000&stat=pbat&online=0&sort=G&order=desc&per_page='

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
        }
        
        for i in range(0, 40):
            url = self.start_url + str(i)
            yield SplashRequest(url, self.parse, endpoint='render.html',
                                args=splash_args)

    def parse(self, response):
        name = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[2]/a/text()').extract()
        g = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[3]/text()').extract()
        pa = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[4]/text()').extract()
        ab = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[5]/text()').extract()
        rbi = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[6]/text()').extract()
        r = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[7]/text()').extract()
        h = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[8]/text()').extract()
        h_1b = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[9]/text()').extract()
        h_2b = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[10]/text()').extract()
        h_3b = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[11]/text()').extract()
        hr = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[12]/text()').extract()
        tb = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[13]/text()').extract()
        so = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[14]/text()').extract()
        sb = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[15]/text()').extract()
        obp = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[16]/text()').extract()
        slg = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[17]/text()').extract()
        avg = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[18]/text()').extract()
        gidp = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[19]/text()').extract()
        sac = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[20]/text()').extract()
        sf = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[21]/text()').extract()
        bb = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[22]/text()').extract()
        ibb = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[23]/text()').extract()
        hbp = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[24]/text()').extract()
        cs = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[25]/text()').extract()
        go = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[26]/text()').extract()
        ao = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[27]/text()').extract()
        gf = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[28]/text()').extract()
        sbp = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[29]/text()').extract()
        ta = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[30]/text()').extract()
        ssa = response.xpath(
            '/html/body/div[4]/div/div/div[4]/table/tbody/tr/td[31]/text()').extract()

        item = CpblItem()
        item['name'] = name
        item['g'] = g
        item['pa'] = pa
        item['ab'] = ab
        item['rbi'] = rbi
        item['r'] = r
        item['h'] = h
        item['h_1b'] = h_1b
        item['h_2b'] = h_2b
        item['h_3b'] = h_3b
        item['hr'] = hr
        item['tb'] = tb
        item['so'] = so
        item['sb'] = sb
        item['obp'] = obp
        item['slg'] = slg
        item['avg'] = avg
        item['gidp'] = gidp
        item['sac'] = sac
        item['sf'] = sf
        item['bb'] = bb
        item['ibb'] = ibb
        item['hbp'] = hbp
        item['cs'] = cs
        item['go'] = go
        item['ao'] = ao
        item['gf'] = gf
        item['sbp'] = sbp
        item['ta'] = ta
        item['ssa'] = ssa

        return item

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class CpblPipeline(object):
    # Connect to Database
    def __init__(self):
        self.connect = pymysql.connect(
            host='127.0.0.1',
            db='CPBL',
            user='root',
            passwd='admin1234',
            charset='utf8',
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            for i in range(0, len(item['name'])):
                sql = 'INSERT INTO Player (Name, G, PA, AB, RBI, R, H, 1B, 2B, 3B, HR, TB, SO, SB, OBP, SLG, AVG, ' \
                      'GIDP, SAC, SF, BB, IBB, HBP, CS, GO, AO, GF, SBP, TA, SSA) VALUES (%s, %s, %s, %s, %s, %s, ' \
                      '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) '
                lis = (item['name'][i],
                       item['g'][i],
                       item['pa'][i],
                       item['ab'][i],
                       item['rbi'][i],
                       item['r'][i],
                       item['h'][i],
                       item['h_1b'][i],
                       item['h_2b'][i],
                       item['h_3b'][i],
                       item['hr'][i],
                       item['tb'][i],
                       item['so'][i],
                       item['sb'][i],
                       item['obp'][i],
                       item['slg'][i],
                       item['avg'][i],
                       item['gidp'][i],
                       item['sac'][i],
                       item['sf'][i],
                       item['bb'][i],
                       item['ibb'][i],
                       item['hbp'][i],
                       item['cs'][i],
                       item['go'][i],
                       item['ao'][i],
                       item['gf'][i],
                       item['sbp'][i],
                       item['ta'][i],
                       item['ssa'][i])
                self.cursor.execute(sql, lis)
                self.connect.commit()

        except Exception as error:
            print(error)

        return item

    # Close Database
    def close_spider(self, spider):
        self.connect.close();
        self.cursor.close();

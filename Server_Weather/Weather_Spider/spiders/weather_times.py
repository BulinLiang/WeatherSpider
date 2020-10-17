# -*- coding: utf-8 -*-
import scrapy
from ..items import Weather_timesSpiderItem
import pymysql, datetime


class WeatherTimesSpider(scrapy.Spider):
    name = 'time'
    allowed_domains = ['www.scnewair.cn']
    urls = ["http://www.scnewair.cn:6112/publish/getAllCityRealTimeAQIC"]
    # head_google = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0",
    #     "Cookie": "JSESSIONID=561F426AF99D5755BD5F4F5853C3EB6A"
    # }

    def start_requests(self):
        print("\nSpider：time")
        print(datetime.datetime.now().strftime("%F %T"))
        '''
            一天删除一次数据
        '''
        self.deleteData()
        for i in range(len(self.urls)):
            print(self.urls[0])
            yield scrapy.Request(url=self.urls[0], callback=self.parse, encoding='utf-8')

    def parse(self, response):

        items = Weather_timesSpiderItem()
        res = response.text
        items['html'] = res

        yield items

    # 删除数据
    def deleteData(self):
        db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="root",
                             db="weather_quality")
        cursor_sel = db.cursor()  # 获取游标对象
        cursor_del = db.cursor()
        sel_time = "SELECT timepoint from timesdata WHERE cityname = '成都市' ORDER BY timepoint"

        delete = "DELETE FROM timesdata"
        try:
            cursor_sel.execute(sel_time)
            temp_time = datetime.datetime.strptime(cursor_sel.fetchall()[0][0], "%Y-%m-%d %H:%M:%S")  # 从数据库调出日期
            now = datetime.datetime.now().day  # 当前日期
            day = now - temp_time.day  # 当前日期和从数据库调出的日期相减计算天数
            print(day)
            if day != 0:
                del_time = str(temp_time).split(" ")[0]
                cursor_del.execute(delete + f" WHERE timepoint LIKE '{del_time}%'")
                print('删除数据成功')
            db.commit()

        except:
            db.rollback()
            print("删除数据失败")
        finally:
            db.close()

# -*- coding: utf-8 -*-
import scrapy
import datetime
from ..items import Weather_daysSpiderItem
# from ..items import Weather_daysSpiderItem
import pymysql


class WeatherDaysSpider(scrapy.Spider):
    name = 'days'
    allowed_domains = ['www.scnewair.cn']
    urls = ["http://www.scnewair.cn:6112/publish/getAllCityDayAQIC"]

    # head_google = {
    #     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",
    #     # "Cookie": "BAIDUID=E5000918C40BAAA2186E18AFCFCFE3D8:FG=1; BIDUPSID=E5000918C40BAAA2368D4A35746EC34F; PSTM=1584598854; BD_UPN=133352; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=30969_1426_31125_21080_31187_30823_31195; delPer=0; BD_CK_SAM=1; PSINO=6; H_PS_645EC=8c2a6N4WqJp6pn8wSP2oLBPRdT9wD9NSu1o51kv47xYDbnvOCXMC2gh9Ofk"
    # }

    def start_requests(self):
        print("\nSpider：days")
        print(datetime.datetime.now().strftime("%F %T"))
        '''
            一个月删除一次数据
        '''
        self.deleteData()
        for i in range(len(self.urls)):
            print(self.urls[0])
            yield scrapy.Request(url=self.urls[0], callback=self.parse, encoding='utf-8')

    def parse(self, response):
        items = Weather_daysSpiderItem()
        res = response.text
        items['html'] = res
        # 传递数据至 piplines
        # 区别 return
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
        sel_time = "SELECT timepoint from daysdata WHERE cityname = '成都市' ORDER BY timepoint ASC"

        delete = "DELETE FROM daysdata"
        try:
            cursor_sel.execute(sel_time)
            temp_time = datetime.datetime.strptime(cursor_sel.fetchall()[0][0], "%Y-%m-%d %H:%M:%S")  # 从数据库调出日期
            now = datetime.datetime.now().month  # 当前日期
            day = now - temp_time.month  # 当前日期和从数据库调出的日期相减计算天数
            if day != 0:
                now_date = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month)	
                # print(now_date)
                cursor_del.execute(delete + f" WHERE timepoint NOT LIKE '{now_date}%'")
                print('删除数据成功')
            db.commit()

        except:
            db.rollback()
            print("删除数据失败")
        finally:
            db.close()

# -*- coding: utf-8 -*-

'''
    源网站：http://182.148.109.15:82/PublishService/nav/naviGation.vm?target=0
'''
import scrapy
import time, datetime, pymysql, json
from ..items import Weather_predictionSpiderItem


class WeatherPredictionSpider(scrapy.Spider):
    name = 'prediction'
    urls = ["http://www.scnewair.cn:6112/smartadmin/forecast/getCityAuditResult?timePoint="]
    # head_google = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0",
    #     "Cookie": "JSESSIONID=561F426AF99D5755BD5F4F5853C3EB6A"
    # }

    def start_requests(self):
        print("\nSpider：prediction")
        print(datetime.datetime.now().strftime("%F %T"))
        self.deleteData()
        self.flag = 0  # 代表偶数天，当天
        for i in range(len(self.urls)):
            now = datetime.datetime.now().strftime('%Y-%m-%d')  # 字符类型的时间,取年月日
            timeArray = time.strptime(now, '%Y-%m-%d')  # 转换日期类型

            today = time.strptime(now, '%Y-%m-%d').tm_mday  # 取出当天日期，判断今天是偶数天还是基数天，如果是基数天无法获取预报
            if today % 2 == 0:
                timeStamp = int(time.mktime(timeArray)) * 1000 - 86400000
                self.flag = 1
            else:
                # 构造13位的时间戳 - 一天的时间戳 = 前一天的时间戳
                timeStamp = int(time.mktime(timeArray)) * 1000 - 86400000
                self.flag = 1  # 代表基数天，基数天会减去前一天的一个数据
            url = self.urls[0] + str(timeStamp)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse, encoding='utf-8')

    def parse(self, response):
        items = Weather_predictionSpiderItem()
        res = json.loads(response.text)
        res['data']['flag'] = str(self.flag)
        items['html'] = json.dumps(res)
        yield items

    # 删除数据
    def deleteData(self, condition=""):
        db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="root",
                             db="weather_quality")
        cursor = db.cursor()  # 获取游标对象
        if condition == "":
            delete = "DELETE FROM predictiondata"
        else:
            delete = "DELETE * FROM predictiondata WHERE '%s'" % (condition)
        print(delete)
        try:
            cursor.execute(delete)
            db.commit()
            print('删除数据成功')
        except:
            db.rollback()
            print("删除数据失败")
        finally:
            db.close()

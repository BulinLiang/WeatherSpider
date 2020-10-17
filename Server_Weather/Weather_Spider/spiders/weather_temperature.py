# -*- coding: utf-8 -*-
import scrapy
from ..items import Weather_temperatureSpiderItem
import json, pymysql,datetime
import random

class WeatherTemperatureSpider(scrapy.Spider):
    USER_AGENT_LIST = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    USER_AGENT = random.choice(USER_AGENT_LIST)


    name = 'temperature'
    allowed_domains = ['t.weather.sojson.com/api/weather/city']
    urls = ['http://t.weather.sojson.com/api/weather/city/']

    # head_google = {
    #     USER_AGENT,
    #     # "Cookie": "BAIDUID=E5000918C40BAAA2186E18AFCFCFE3D8:FG=1; BIDUPSID=E5000918C40BAAA2368D4A35746EC34F; PSTM=1584598854; BD_UPN=133352; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=30969_1426_31125_21080_31187_30823_31195; delPer=0; BD_CK_SAM=1; PSINO=6; H_PS_645EC=8c2a6N4WqJp6pn8wSP2oLBPRdT9wD9NSu1o51kv47xYDbnvOCXMC2gh9Ofk"
    # }
    def start_requests(self):
        print("\nSpider：temperature")
        print(datetime.datetime.now().strftime("%F %T"))
        '''
            每日更新，因为json文件中字典无序,所以取出的城市代码不一定和前一次取出的相同，所以生成的id会有所不同，
            但是设置id为主键要出错，所以当每次插入数据之前先删除以前的数据
        '''
        self.deleteData()

        # 记录第几个城市天气信息，方便记录id
        self.n = 0
        with open("./code.json", "r", encoding='utf-8') as f:
            code = json.loads(f.read())
        for code in code.values():
            url = self.urls[0] + code
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse,  encoding='utf-8')

    def parse(self, response):

        items = Weather_temperatureSpiderItem()
        res = json.loads(response.text)
        res["id"] = str(self.n)
        items['html'] = json.dumps(res)
        self.n += 1
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
            delete = "DELETE FROM temperaturedata"
        else:
            delete = "DELETE * FROM temperaturedata WHERE '%s'" % (condition)
        # print(delete)
        try:
            cursor.execute(delete)
            print('删除数据成功')
            db.commit()
        except:
            db.rollback()
            print("删除数据失败")
        finally:
            db.close()

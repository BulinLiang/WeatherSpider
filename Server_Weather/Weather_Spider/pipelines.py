# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import time, datetime
import pymysql
import re
from xpinyin import Pinyin


class WeatherSpiderPipeline(object):
    def createTable(self, sql, db):
        cursor = db.cursor()  # 获取游标对象
        # 创建数据库，如果数据库已经存在，注意主键不要重复，否则出错

        try:
            # print(sql)
            cursor.execute(sql)
        except Exception as info:
            print(info)

    def insertSQL(self, spiderName, db, datas):
        cursor = db.cursor()  # 获取游标对象
        if spiderName == "time":
            for i in range(len(datas)):
                data = datas[i]["columns"]


                temp_time = self.timeChange(data["TIMEPOINT"])  # 将时间戳格式化为系统格式
                time_array = datetime.datetime.strptime(temp_time, "%Y-%m-%d %H:%M:%S")  # 将字符时间转换为日期型时间
                delta = datetime.timedelta(hours=2)  # 获取1天的时间类型
                timepoint = str(time_array + delta)  # 天数相加，转换为字符型
                # print(timepoint)

                # timepoint = self.timeChange(data["TIMEPOINT"])  # 将时间戳格式化为系统格式

                # 日_小时_顺序
                id = str(time.localtime().tm_mday) + "_" + timepoint.split(" ")[1].split(":")[0] + "_" + str(i)
                cityname = data["CITYNAME"] + "市"
                AQI = data["AQI"]
                SO2 = data["SO2"]
                NO2 = data["NO2"]
                CO = data["CO"]
                O3 = data["O3"]
                PM2_5 = data["PM2_5"]
                PM10 = data["PM10"]
                # 插入数据语句
                insert = "insert into timesdata (id,cityname,timepoint, AQI,SO2 , NO2 ,CO , O3 ,PM2_5 ,PM10)" \
                         " values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' , '%s')" % \
                         (id, cityname, timepoint, AQI, SO2, NO2, CO, O3, PM2_5, PM10)
                try:
                    cursor.execute(insert)
                    db.commit()
                    print('插入小时报数据成功')
                except:
                    db.rollback()
                    print("插入小时报数据失败")

        elif spiderName == "days":
            for i in range(len(datas)):
                data = datas[i]["columns"]
                id = str(time.localtime().tm_mon) + '_' + str(time.localtime().tm_mday) + '_' + str(i)
                cityname = data["CITYNAME"] + "市"

                day = self.timeChange(data["TIMEPOINT"])  # 将时间戳格式化为系统格式
                day_array = datetime.datetime.strptime(day, "%Y-%m-%d %H:%M:%S")  # 将字符时间转换为日期型时间
                delta = datetime.timedelta(days=1)  # 获取1天的时间类型
                timepoint = str(day_array + delta)  # 天数相加，转换为字符型

                CODE = data["CITYCODE"]
                AQI = data["AQI"]
                SO2 = data["SO2"]
                NO2 = data["NO2"]
                CO = data["CO"]
                O3 = data["O3"]
                PM2_5 = data["PM2_5"]
                PM10 = data["PM10"]
                insert = "insert into daysdata (id,cityname,timepoint,CODE, AQI,SO2 , NO2 ,CO , O3 ,PM2_5 ,PM10)" \
                         " values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' , '%s')" % \
                         (id, cityname, timepoint, CODE, AQI, SO2, NO2, CO, O3, PM2_5, PM10)
                # print(id, cityname, timepoint, CODE, AQI, SO2, NO2, CO, O3, PM2_5, PM10)

                try:
                    cursor.execute(insert)
                    db.commit()
                    print('插入日报数据成功')
                except:
                    db.rollback()
                    print("插入日报数据失败")

        elif spiderName == "prediction":
            pinyin = Pinyin()
            time_temp = self.timeChange(datas["timePoint"])  # 将时间戳格式化为系统格式
            timepoint = re.split(" ", time_temp)[0]
            flag = int(datas['flag'])
            datas = datas["forecast"]
            for k in datas.keys():
                data = datas[k]

                id = str(time.localtime().tm_mday) + "_" + str(time.localtime().tm_hour) + "_" + k
                cityname = data["CITYNAME"]
                cityname_temp = pinyin.get_pinyin(data["CITYNAME"])
                cityname_py = re.sub('-', '', cityname_temp)
                if data["PRIMARYPOLLUTANT"] == None:
                    pullutant = "无,无,无,无,无,无,无"
                    if flag == 1:
                        pullutant = pullutant.replace("无,", "", 1)  # 第三个参数是替换次数不超过max次
                else:
                    temp_pull = data["PRIMARYPOLLUTANT"].split('|')
                    if flag == 1:
                        temp_pull.pop(0)
                    pullutant = re.sub("'|\[|]| ", "", str(temp_pull))

                if data["AQI"] == None:
                    aqi = "无,无,无,无,无,无,无"
                    if flag == 1:
                        aqi = aqi.replace("无,", "", 1)  # 第三个参数是替换次数不超过max次
                else:
                    temp_aqi = data["AQI"].split('|')
                    if flag == 1:
                        temp_aqi.pop(0)
                    aqi = re.sub("'|\[|]| ", "", str(temp_aqi))

                if data["QUALITY"] == None:
                    quality = "无,无,无,无,无,无,无"
                    if flag == 1:
                        quality = quality.replace("无,", "", 1)  # 第三个参数是替换次数不超过max次
                else:
                    temp_quality = data["QUALITY"].split('|')
                    if flag == 1:
                        temp_quality.pop(0)
                    quality = re.sub("'|\[|]| ", "", str(temp_quality))

                # print(id, cityname, timepoint, pullutant, type(AQI))
                insert = "insert into predictiondata (id,cityname,timepoint, pullutant,aqi,quality,cityname_py)" \
                         "values('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                         (id, cityname, timepoint, pullutant, aqi, quality, cityname_py)

                try:
                    # print("ddd")
                    cursor.execute(insert)
                    db.commit()
                    print('插入空气质量预报数据成功')
                except:
                    db.rollback()
                    print("插入空气质量预报数据失败")

        elif spiderName == "temperature":
            cityname = datas["cityInfo"]["city"]
            forecast = datas["data"]["forecast"]
            shidu = datas["data"]["shidu"]
            temperature = datas["data"]["wendu"]
            times = datas["time"]
            for i in range(len(forecast)):
                if i > 0:
                    shidu = 0
                    temperature = 0
                    times = forecast[i]["ymd"]
                id = datas["id"] + '_' + str(i)
                week = forecast[i]["week"]
                # # 将高低温文字和温度使用“ ”分割，取出温度
                high_low = re.sub("℃", "", forecast[i]["low"].split(" ")[1]) + "/" + forecast[i]["high"].split(" ")[1]
                fx = forecast[i]["fx"]
                fl = forecast[i]["fl"]
                types = forecast[i]["type"]
                notice = forecast[i]["notice"]
                insert = "insert into temperaturedata(id,cityname,times, week,high_low , temperature ,shidu , fx ,fl ,types,notice)" \
                         " values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' , '%s', '%s')" % \
                         (id, cityname, times, week, high_low, temperature, shidu, fx, fl, types, notice)
                try:
                    cursor.execute(insert)
                    db.commit()
                    print('插入天气预报数据成功')
                except:
                    db.rollback()
                    print("插入天气预报数据失败")

    # 将时间戳格式化为系统格式
    def timeChange(self, timeStamp):
        timeStamp = timeStamp / 1000
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)  # 将时间格式转换为字符串
        # print(type(otherStyleTime))
        return otherStyleTime

    def process_item(self, item, spider):
        # 转换html成dict类型并取出数据
        datas_temp = json.loads(item["html"])
        data s = datas_temp["data"]
        db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="root",
                             db="weather_quality")

        if spider.name == "time":
            # print("Spider：time")
            print("保存小时报信息至数据库...")
            # 必须加\，否则报错
            createTimes = "CREATE TABLE timesdata(" \
                          "id char(20) primary key ," \
                          "cityname char(20)," \
                          "timepoint char(20)," \
                          "AQI char(20)," \
                          "SO2 char(20)," \
                          "NO2 char(20)," \
                          "CO char(20)," \
                          "O3 char(20)," \
                          "PM2_5 char(20)," \
                          "PM10 char(20))"
            # 创建数据表timesdata
            self.createTable(createTimes, db)
            # 数据提取及插入
            self.insertSQL(spider.name, db, datas)

        elif spider.name == "days":
            # print("Spider：days")
            print("保存日报信息至数据库...")
            createDays = "CREATE TABLE daysdata(" \
                         "id char(20) primary key," \
                         "cityname char(20), " \
                         "timepoint char(20)," \
                         "CODE char(6)," \
                         "AQI char(20)," \
                         "SO2 char(20)," \
                         "NO2 char(20)," \
                         "CO char(20)," \
                         "O3 char(20)," \
                         "PM2_5 char(20)," \
                         "PM10 char(20))"
            # 创建数据表daysdata
            self.createTable(createDays, db)
            # 数据提取及插入
            self.insertSQL(spider.name, db, datas)

        elif spider.name == "prediction":
            # print("Spider：prediction")
            print("保存预报信息至数据库...")
            createQuality = "CREATE TABLE predictiondata(" \
                            "id char(20)," \
                            "cityname char(10), " \
                            "timepoint char(15)," \
                            "pullutant char(80)," \
                            "aqi char(80)," \
                            "quality char(60),"\
                            "cityname_py char(20))"
            # 创建数据表qualitydata
            self.createTable(createQuality, db)
            # 数据提取及插入
            self.insertSQL(spider.name, db, datas)
        elif spider.name == "temperature":
            # print("Spider：temperature")
            print("保存天气温度至数据库...")
            createTemperature = "CREATE TABLE temperaturedata(" \
                                "id  char(5)," \
                                "cityname char(10), " \
                                "times char(20) ," \
                                "week char(10)," \
                                "high_low char(10)," \
                                "temperature char(3)," \
                                "shidu char(5)," \
                                "fx char(10)," \
                                "fl char(10)," \
                                "types char(20)," \
                                "notice char(20))"
            # 创建数据表temperaturedata
            self.createTable(createTemperature, db)
            # 数据提取及插入
            self.insertSQL(spider.name, db, datas_temp)

        db.close()

        return item

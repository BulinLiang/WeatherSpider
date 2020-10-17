'''
    -*- coding: utf-8 -*- 
    @Time : 2020/2/2 16:05 
    @Author : Bulin Liang 
    @File : SearchSQL.py 
    @Software: PyCharm
'''

'''
该文件完成功能：
    查询城市空气质量，提供给ui界面生成信息使用
    1、小时报
    2、日报
    3、预报
'''
import pymysql, datetime, re
from xpinyin import Pinyin


class SearchSQL(object):
    db = pymysql.connect(host="localhost",
                         port=3306,
                         user="root",
                         password="root",
                         db="weather_quality")

    # 0
    def __init__(self):
        cursor = self.db.cursor()  # 获取游标对象
        # 查询语句，使用模糊查找
        select = "SELECT id,cityname FROM predictiondata ORDER BY id"
        pinyin = Pinyin()
        try:
            cursor.execute(select)  # 执行语句
            self.db.commit()
            result = cursor.fetchall()  # 输出字段
            # print(result)
            global city_name
            # city_name[0]存放城市名，city_name[1]存放城市名拼音
            self.city_name = [[], []]
            for name in result:
                self.city_name[0].append(name[1])
                name_temp = pinyin.get_pinyin(f"{name[1]}")
                self.city_name[1].append(re.sub('-', '', name_temp))
        except:
            self.db.rollback()  # 发生错误时回滚

    # 1
    def prediction(self, city_name):
        cursor = self.db.cursor()  # 获取游标对象
        # 查询语句，使用模糊查找
        select = "SELECT * FROM predictiondata WHERE cityname = '%s'" % (city_name)
        try:
            cursor.execute(select)  # 执行语句
            self.db.commit()
            result = cursor.fetchall()  # 输出字段
            # print(list(result[0]))
            return result[0]
        except:
            self.db.rollback()  # 发生错误时回滚

    # 2
    def temperature(self, city_name):
        cursor = self.db.cursor()  # 获取游标对象
        # 查询语句，使用模糊查找
        select = "SELECT * FROM temperaturedata WHERE cityname = '%s'ORDER BY shidu desc,times" % (city_name)
        try:
            cursor.execute(select)  # 执行语句
            self.db.commit()
            result = cursor.fetchall()  # 输出字段
            # print(len(result))
            return result

        except:
            self.db.rollback()  # 发生错误时回滚

    # 3
    def airDatas(self, city_name):
        day_cursor = self.db.cursor()  # 获取游标对象
        time_cursor = self.db.cursor()  # 获取游标对象

        day_select = "SELECT * FROM daysdata WHERE cityname = '%s'ORDER BY timepoint ASC " % (city_name)
        times_select = "SELECT * FROM timesdata WHERE cityname = '%s'GROUP BY id ORDER BY timepoint ASC" % (city_name)
        result = {}
        try:
            day_cursor.execute(day_select)  # 执行语句
            time_cursor.execute(times_select)  # 执行语句
            self.db.commit()
            day_result = day_cursor.fetchall()  # 输出字段
            time_result = time_cursor.fetchall()
            result["day"] = day_result
            result["time"] = time_result
            # print(result)
            return result
        except:
            self.db.rollback()  # 发生错误时回滚

    # 4
    def searchCity(self, city_name):
        cursor = self.db.cursor()
        select = "SELECT cityname FROM predictiondata WHERE cityname = '%s'" % (city_name)
        try:
            cursor.execute(select)
            self.db.commit()
            result = cursor.fetchall()
            # print(result)
            return result[0]

        except:
            self.db.rollback()

    # 将时间戳格式化为系统格式
    def timeChange(self):
        month = datetime.datetime.now().month
        hour = datetime.datetime.now().hour
        timeStamp = str(month) + '_' + str(hour)
        return timeStamp


if __name__ == '__main__':
    select = SearchSQL()
    # select.airDatas("成都市")
    select.db.close()

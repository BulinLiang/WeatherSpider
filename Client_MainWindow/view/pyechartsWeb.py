'''
    -*- coding: utf-8 -*-
    @Time    : 2020/3/2 16:51
    @Author  : Walden
    @ProjectName： Weather_Spider
    @File    : pyechartsWeb.py
    @ProductName ： PyCharm
'''

'''
python2.X --> pyecharts V0.5
python3.X --> pyecharts V1.0

pyechartsV1.0 中文说明文档：http://pyecharts.org/#/zh-cn/chart_api

参考文档网站：https://www.okcode.net/article/31144 设置图表的风格和控件的位置
            https://www.okcode.net/article/83121 散点图每个点显示数据
            https://gallery.echartsjs.com/editor.html?c=xS1jMxuOVm 图表代码网页测试
            
'''
from pyecharts.charts import Line, Grid
from pyecharts import options as opts
import re


# bar =Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.show_config()
# bar.render()

# init_opts=opts.InitOpts(width="600px",height="300px")可以这是图像显示大小
class PyechartWeb:
    def createView(self, Clt, city_name):  # Clt客户端程序
        # self.day_datas, self.time_datas = SearchSQL().airDatas(city_name)
        air_datas = Clt.sendData(f"3 {city_name}")
        self.day_datas = air_datas["day"]
        self.time_datas = air_datas["time"]

        timepoint = [[], []]
        aqi = [[], []]
        so2 = [[], []]
        no2 = [[], []]
        co = [[], []]
        o3 = [[], []]
        pm2_5 = [[], []]
        pm10 = [[], []]

        for datas in self.day_datas:
            # 分割日期
            day = re.sub("^2.*?-", '', datas[2].split(' ')[0])  # 取出日期，将年份去掉
            timepoint[0].append(day)
            aqi[0].append(int(datas[4]))
            so2[0].append(int(datas[5]))
            no2[0].append(int(datas[6]))
            co[0].append(float(datas[7]))
            o3[0].append(int(datas[8]))
            pm2_5[0].append(int(datas[9]))
            pm10[0].append(int(datas[10]))
        # print(timepoint[0], aqi[0], so2[0], no2[0], co[0], o3[0], pm2_5[0], pm10[0])

        day_line = Line()
        day_line.add_xaxis(timepoint[0])  # 增加x轴
        day_line.add_yaxis("AQI", aqi[0],
                           is_smooth=True,  # 线条平滑
                           areastyle_opts=opts.AreaStyleOpts(opacity=0),  # 曲线填充面积的透明度
                           color="#4169E1"
                           )
        day_line.add_yaxis("SO2", so2[0],
                           is_smooth=True,
                           areastyle_opts=opts.AreaStyleOpts(opacity=0),
                           color="#FF0033"
                           )
        day_line.add_yaxis("NO2", no2[0],
                           is_smooth=True,
                           areastyle_opts=opts.AreaStyleOpts(opacity=0),
                           color="#4169E1"
                           )
        day_line.add_yaxis("CO", co[0],
                           is_smooth=True,
                           areastyle_opts=opts.AreaStyleOpts(opacity=0),
                           color="#FF0033"
                           )
        day_line.add_yaxis("O3", o3[0],
                           is_smooth=True,
                           areastyle_opts=opts.AreaStyleOpts(opacity=0),
                           color="#FF0033"
                           )
        day_line.add_yaxis("PM2.5", pm2_5[0],
                           is_smooth=True,
                           areastyle_opts=opts.AreaStyleOpts(opacity=0),
                           color="#4169E1"
                           )
        day_line.add_yaxis("PM10", pm10[0],
                           is_smooth=True,
                           areastyle_opts=opts.AreaStyleOpts(opacity=0),
                           color="#FF0033"
                           )
        day_line.set_global_opts(
            title_opts=opts.TitleOpts(title=city_name, subtitle="日报", padding=1, pos_left="center", item_gap=7),
            # 设置标题居中
            legend_opts=opts.LegendOpts(pos_right="right",  # 将标签设置为水平居右
                                        pos_top="center",  # 将标签设置为垂直居中
                                        padding=1,  # 标签与边界距离
                                        item_gap=16,  # 标签之间的间距
                                        item_height=12,  # 标签的高度
                                        ),
            xaxis_opts=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                                     is_scale=False,
                                     boundary_gap=False),  # 图像贴近y轴
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True))  # 增加y轴分割线
        )
        day_line.set_series_opts(markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                                         opts.MarkPointItem(type_="min")],  # 标注最大值最小值
                                                                   symbol_size=[30, 34],  # 标注样式的宽，高
                                                                   label_opts=opts.LabelOpts(position="inside",
                                                                                             color="#fff",
                                                                                             font_size=9)),  # 标注内字体的大小
                                 label_opts=opts.LabelOpts(is_show=True)  # 显示每个坐标点的值
                                 # markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")])  # 标注平均线
                                 )  # 系列配置项
        # 设置图表在页面居中：Anaconda3\Lib\site - packages\pyecharts\render\templates\macro
        # 添加margin:auto;top:8px;

        # 框架
        day_grid = Grid(init_opts=opts.InitOpts(width="800px", height="380px"))
        day_grid.add(day_line, grid_opts=opts.GridOpts(pos_top="70"))

        day_grid.render("../web/day_line.html")

        for datas in self.time_datas:
            time_temp = datas[2].split(" ")[1]
            timepoint[1].append(time_temp)
            aqi[1].append(int(datas[3]))
            so2[1].append(int(datas[4]))
            no2[1].append(int(datas[5]))
            co[1].append(float(datas[6]))
            o3[1].append(int(datas[7]))
            pm2_5[1].append(int(datas[8]))
            pm10[1].append(int(datas[9]))
        # print(timepoint[1], aqi[1], so2[1], no2[1], co[1], o3[1], pm2_5[1], pm10[1])

        time_line = Line(init_opts=opts.InitOpts(width="800px", height="300px"))
        time_line.add_xaxis(timepoint[1])  # 增加x轴
        time_line.add_yaxis("AQI", aqi[1],
                            is_smooth=True,  # 线条平滑
                            areastyle_opts=opts.AreaStyleOpts(opacity=0),  # 曲线填充面积的透明度
                            color="#4169E1"
                            )
        time_line.add_yaxis("SO2", so2[1],
                            is_smooth=True,
                            areastyle_opts=opts.AreaStyleOpts(opacity=0),
                            color="#FF0033"
                            )
        time_line.add_yaxis("NO2", no2[1],
                            is_smooth=True,
                            areastyle_opts=opts.AreaStyleOpts(opacity=0),
                            color="#4169E1"
                            )
        time_line.add_yaxis("CO", co[1],
                            is_smooth=True,
                            areastyle_opts=opts.AreaStyleOpts(opacity=0),
                            color="#FF0033"
                            )
        time_line.add_yaxis("O3", o3[1],
                            is_smooth=True,
                            areastyle_opts=opts.AreaStyleOpts(opacity=0),
                            color="#FF0033"
                            )
        time_line.add_yaxis("PM2.5", pm2_5[1],
                            is_smooth=True,
                            areastyle_opts=opts.AreaStyleOpts(opacity=0),
                            color="#4169E1"
                            )
        time_line.add_yaxis("PM10", pm10[1],
                            is_smooth=True,
                            areastyle_opts=opts.AreaStyleOpts(opacity=0),
                            color="#FF0033"
                            )
        time_line.set_global_opts(
            title_opts=opts.TitleOpts(title=city_name, subtitle="时报", padding=1, pos_left="center", item_gap=7),
            legend_opts=opts.LegendOpts(pos_right="right",  # 将标签设置为水平居右
                                        pos_top="center",  # 将标签设置为垂直居中
                                        padding=1,  # 标签与边界距离
                                        item_gap=16,  # 标签之间的间距
                                        item_height=12,  # 标签的高度
                                        ),
            xaxis_opts=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                                     is_scale=False,
                                     boundary_gap=False),  # 图像贴近y轴
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True))  # 增加y轴分割线
        )
        time_line.set_series_opts(markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                                          opts.MarkPointItem(type_="min")],  # 标注最大值最小值
                                                                    symbol_size=[30, 34],  # 标注样式的宽，高
                                                                    label_opts=opts.LabelOpts(position="inside",
                                                                                              color="#fff",
                                                                                              font_size=9)),  # 标注内字体的大小
                                  label_opts=opts.LabelOpts(is_show=True)  # 显示每个坐标点的值
                                  # markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")])  # 标注平均线
                                  )  # 系列配置项

        time_grid = Grid(init_opts=opts.InitOpts(width="800px", height="380px"))
        time_grid.add(time_line, grid_opts=opts.GridOpts(pos_top="70"))

        time_grid.render("../web/time_line.html")
        # print("生成图表成功...")

#
# if __name__ == "__main__":
#     web = PyechartWeb()
# web.createView("成都市")

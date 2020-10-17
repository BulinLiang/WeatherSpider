# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testLIst.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


'''
    命名规则：
    类名：多个单词大写开头
    函数名： 多个单词第一个单词开头小写，第二个单词大写
    控件名/变量名： 大写

'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtWebEngineWidgets import QWebEngineView

import sys
from xpinyin import Pinyin
import re
import datetime

# 自定义包,调用时必须使用绝对路径
# from Weather_Spider.spiders.SearchSQL import SearchSQL
from view.pyechartsWeb import PyechartWeb
from view.tcpClient import Client


class XM_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 810)
        MainWindow.setMinimumSize(QtCore.QSize(1120, 810))
        MainWindow.setMaximumSize(QtCore.QSize(1120, 810))
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # MainWindow.setWindowOpacity(0.9)  # 设置窗口透明度
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Left_Widget = QtWidgets.QWidget(self.centralwidget)
        self.Left_Widget.setMinimumSize(QtCore.QSize(245, 810))
        self.Left_Widget.setMaximumSize(QtCore.QSize(245, 810))
        self.Left_Widget.setStyleSheet("background-color: rgb(97, 101, 247);\n"
                                       "border-top-left-radius:10px;\n"
                                       "border-bottom-left-radius:10px;")
        self.Left_Widget.setObjectName("Left_Widget")

        self.Logo_Lable = QtWidgets.QLabel(self.Left_Widget)
        self.Logo_Lable.setGeometry(QtCore.QRect(24, 28, 43, 41))
        self.Logo_Lable.setMinimumSize(QtCore.QSize(43, 41))
        self.Logo_Lable.setMaximumSize(QtCore.QSize(43, 41))
        self.Logo_Lable.setStyleSheet("background-image:url(../icon/logo.png);")
        # self.Logo_Lable.setText("")
        self.Logo_Lable.setObjectName("Logo_Lable")

        self.Title_Quality_Back = QtWidgets.QLabel(self.Left_Widget)
        self.Title_Quality_Back.setGeometry(QtCore.QRect(75, 30, 151, 31))
        self.Title_Quality_Back.setText("XM-Weather")
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title_Quality_Back.setFont(font)
        self.Title_Quality_Back.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title_Quality_Back.setObjectName("Title_Quality_Back")

        self.List_Widget = QtWidgets.QListWidget(self.Left_Widget)
        self.List_Widget.setGeometry(QtCore.QRect(0, 160, 245, 300))
        self.List_Widget.setMinimumSize(QtCore.QSize(245, 0))
        self.List_Widget.setMaximumSize(QtCore.QSize(245, 245))
        self.List_Widget.setStyleSheet("QListWidget::Item:selected {"
                                       "    border-left: 5px solid rgb(255,255,255);"
                                       "    color:rgb(255,255,255);"
                                       "}"
                                       "QListWidget::Item:hover {"
                                       "    border-left: 5px solid rgb(255,255,255);}"
                                       # "    image:url(../icon/dashboard.png);"
                                       # "}"
                                       "QListWidget::focus{outline: none;}"
                                       # "QListWidget::Item{"
                                       # "image:url(../icon/logo.png);}"
                                       )
        self.List_Widget.setIconSize(QtCore.QSize(245, 60))
        self.List_Widget.setModelColumn(0)
        self.List_Widget.setObjectName("List_Widget")
        self.horizontalLayout.addWidget(self.Left_Widget)

        self.Msg_Quality_Back = QtWidgets.QLabel(self.Left_Widget)
        self.Msg_Quality_Back.setGeometry(QtCore.QRect(31, 453, 180, 330))
        self.Msg_Quality_Back.setMinimumSize(QtCore.QSize(180, 330))
        self.Msg_Quality_Back.setMaximumSize(QtCore.QSize(185, 330))
        self.Msg_Quality_Back.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:10px;")
        self.Msg_Quality_Back.setText("")
        self.Msg_Quality_Back.setObjectName("Msg_Quality_Back")

        self.Msg_Icon = QtWidgets.QLabel(self.Left_Widget)
        self.Msg_Icon.setGeometry(QtCore.QRect(53, 477, 60, 60))
        self.Msg_Icon.setMinimumSize(QtCore.QSize(60, 60))
        self.Msg_Icon.setMaximumSize(QtCore.QSize(60, 60))
        self.Msg_Icon.setStyleSheet("border-radius:10px;")
        self.Msg_Icon.setObjectName("Msg_Icon")

        self.Msg_Days = QtWidgets.QLabel(self.Left_Widget)
        self.Msg_Days.setGeometry(QtCore.QRect(120, 480, 50, 20))
        self.Msg_Days.setMinimumSize(QtCore.QSize(50, 20))
        self.Msg_Days.setMaximumSize(QtCore.QSize(50, 20))
        self.Msg_Days.setText("今天")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.Msg_Days.setFont(font)
        self.Msg_Days.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Days.setObjectName("Msg_Days")

        self.Msg_Time = QtWidgets.QLabel(self.Left_Widget)
        self.Msg_Time.setGeometry(QtCore.QRect(121, 511, 50, 15))
        self.Msg_Time.setMinimumSize(QtCore.QSize(50, 15))
        self.Msg_Time.setMaximumSize(QtCore.QSize(50, 15))
        self.Msg_Time.setText("20:20")
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.Msg_Time.setFont(font)
        self.Msg_Time.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Time.setObjectName("Msg_Time")
        self.Msg_Date = QtWidgets.QLabel(self.Left_Widget)
        self.Msg_Date.setGeometry(QtCore.QRect(121, 527, 80, 15))
        self.Msg_Date.setMinimumSize(QtCore.QSize(80, 15))
        self.Msg_Date.setMaximumSize(QtCore.QSize(80, 15))
        self.Msg_Date.setText("2020/1/28")
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.Msg_Date.setFont(font)
        self.Msg_Date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Date.setObjectName("Msg_Date")

        self.Msg_Temper = QtWidgets.QLabel(self.Left_Widget)
        self.Msg_Temper.setGeometry(QtCore.QRect(31, 560, 180, 60))
        self.Msg_Temper.setMinimumSize(QtCore.QSize(180, 60))
        self.Msg_Temper.setMaximumSize(QtCore.QSize(185, 60))
        self.Msg_Temper.setText("+26℃")
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Msg_Temper.setFont(font)
        self.Msg_Temper.setStyleSheet("border-radius:10px;"
                                      "background-color: rgb(255, 255, 255);")
        self.Msg_Temper.setAlignment(QtCore.Qt.AlignCenter)
        self.Msg_Temper.setObjectName("Msg_Temper")

        self.Msg_City = QtWidgets.QLabel(self.Left_Widget)
        self.Msg_City.setGeometry(QtCore.QRect(31, 621, 180, 25))
        self.Msg_City.setMinimumSize(QtCore.QSize(180, 25))
        self.Msg_City.setText("成都市")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.Msg_City.setFont(font)
        self.Msg_City.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_City.setAlignment(QtCore.Qt.AlignCenter)
        self.Msg_City.setObjectName("Msg_City")
        self.Msg_Humidity = QtWidgets.QLabel(self.Left_Widget)
        self.Msg_Humidity.setGeometry(QtCore.QRect(57, 669, 30, 15))
        self.Msg_Humidity.setMinimumSize(QtCore.QSize(30, 15))
        self.Msg_Humidity.setMaximumSize(QtCore.QSize(30, 15))
        self.Msg_Humidity.setText("湿度：")
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Msg_Humidity.setFont(font)
        self.Msg_Humidity.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Humidity.setObjectName("Msg_Humidity")
        self.Humidity_Scale = QtWidgets.QLabel(self.Left_Widget)
        self.Humidity_Scale.setGeometry(QtCore.QRect(167, 669, 30, 15))
        self.Humidity_Scale.setMinimumSize(QtCore.QSize(30, 15))
        self.Humidity_Scale.setMaximumSize(QtCore.QSize(30, 15))
        self.Humidity_Scale.setText("10%")
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Humidity_Scale.setFont(font)
        self.Humidity_Scale.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Humidity_Scale.setObjectName("Humidity_Scale")
        self.Humidity_Bar = QtWidgets.QProgressBar(self.Left_Widget)
        self.Humidity_Bar.setGeometry(QtCore.QRect(56, 699, 131, 4))
        self.Humidity_Bar.setMinimumSize(QtCore.QSize(131, 4))
        self.Humidity_Bar.setMaximumSize(QtCore.QSize(4, 3))
        self.Humidity_Bar.setStyleSheet(
            "QProgressBar {border: 2px ;   border-radius: 1.5px; background-color: rgb(216, 216, 216);}"
            "::chunk {background-color: rgb(255, 173, 71);}")

        self.Humidity_Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.Humidity_Bar.setFormat("")
        self.Humidity_Bar.setObjectName("Humidity_Bar")
        self.Humidity_Bar.setProperty("value", 10)

        self.Msg_Precipitation = QtWidgets.QLabel(self.Left_Widget)
        self.Msg_Precipitation.setGeometry(QtCore.QRect(57, 719, 40, 15))
        self.Msg_Precipitation.setMinimumSize(QtCore.QSize(40, 15))
        self.Msg_Precipitation.setMaximumSize(QtCore.QSize(40, 15))
        self.Msg_Precipitation.setText("降水量")
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Msg_Precipitation.setFont(font)
        self.Msg_Precipitation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Precipitation.setObjectName("Msg_Precipitation")
        self.Precipitation_Scale = QtWidgets.QLabel(self.Left_Widget)
        self.Precipitation_Scale.setGeometry(QtCore.QRect(167, 719, 30, 15))
        self.Precipitation_Scale.setMinimumSize(QtCore.QSize(30, 15))
        self.Precipitation_Scale.setMaximumSize(QtCore.QSize(30, 15))
        self.Precipitation_Scale.setText("10%")
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Precipitation_Scale.setFont(font)
        self.Precipitation_Scale.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Precipitation_Scale.setObjectName("Precipitation_Scale")
        self.Precipitation_Bar = QtWidgets.QProgressBar(self.Left_Widget)
        self.Precipitation_Bar.setGeometry(QtCore.QRect(55, 747, 131, 4))
        self.Precipitation_Bar.setMinimumSize(QtCore.QSize(131, 4))
        self.Precipitation_Bar.setMaximumSize(QtCore.QSize(4, 3))
        self.Precipitation_Bar.setStyleSheet("QProgressBar::chunk {background-color: rgb(255, 173, 71);}\n"
                                             "QProgressBar {border: 2px ;   border-radius: 1.5px; background-color: rgb(216, 216, 216);}")

        self.Precipitation_Bar.setProperty("value", 10)
        self.Precipitation_Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.Precipitation_Bar.setFormat("")
        self.Precipitation_Bar.setObjectName("Precipitation_Bar")

        self.Right_Widget = QtWidgets.QWidget(self.centralwidget)
        self.Right_Widget.setMinimumSize(QtCore.QSize(875, 810))
        self.Right_Widget.setMaximumSize(QtCore.QSize(875, 810))
        self.Right_Widget.setObjectName("Right_Widget")

        # 搜索栏
        self.Search_group = QtWidgets.QGroupBox(self.centralwidget)
        self.Search_group.setGeometry(QtCore.QRect(245, 0, 875, 280))
        self.Search_group.setMinimumSize(QtCore.QSize(875, 280))
        self.Search_group.setMaximumSize(QtCore.QSize(875, 280))
        self.Search_group.setStyleSheet("border-top-right-radius:10px;"
                                        "background-color: rgb(255, 255, 255);")
        self.Search_group.setObjectName("Search_group")

        self.Right_Pages = QtWidgets.QStackedWidget(self.Right_Widget)
        self.Right_Pages.setGeometry(QtCore.QRect(0, 280, 875, 530))
        self.Right_Pages.setMinimumSize(QtCore.QSize(875, 530))
        self.Right_Pages.setMaximumSize(QtCore.QSize(875, 530))
        self.Right_Pages.setStyleSheet("border-bottom-right-radius:10px;"
                                       "background-color: rgb(255, 255, 255);")
        self.Right_Pages.setObjectName("Right_Pages")

        self.Search_Quality_Back = QtWidgets.QLabel(self.Search_group)
        self.Search_Quality_Back.setGeometry(QtCore.QRect(24, 22, 30, 30))
        self.Search_Quality_Back.setMinimumSize(QtCore.QSize(30, 30))
        self.Search_Quality_Back.setMaximumSize(QtCore.QSize(30, 30))
        pixmap = QtGui.QPixmap("../icon/search.png")  # 按指定路径找到图片，注意路径必须用双引号包围，不能用单引号
        self.Search_Quality_Back.setPixmap(pixmap)  # 在Quality_Back上显示图片
        self.Search_Quality_Back.setScaledContents(True)  # 让图片自适应Quality_Back大小
        self.Search_Quality_Back.setObjectName("Search_Quality_Back")

        self.Search_lineEdit = QtWidgets.QLineEdit(self.Search_group)
        self.Search_lineEdit.setGeometry(QtCore.QRect(60, 25, 270, 23))
        self.Search_lineEdit.setMinimumSize(QtCore.QSize(270, 23))
        self.Search_lineEdit.setMaximumSize(QtCore.QSize(270, 23))
        self.Search_lineEdit.setStyleSheet("border-radius:10px;"
                                           "border-color: rgb(223, 223, 223);"
                                           "border-width: 1px;"
                                           "border-style: solid;"
                                           "padding-left:7px")
        self.Search_lineEdit.setPlaceholderText("搜索四川省城市名...")  # 输入框提示字符
        self.Search_lineEdit.setObjectName("Search_lineEdit")
        self.Search_lineEdit.returnPressed.connect(bCustom.getValue)  # 文本框回车事件

        self.User_Button = QtWidgets.QPushButton(self.Search_group)
        self.User_Button.setGeometry(QtCore.QRect(606, 21, 33, 33))
        self.User_Button.setMinimumSize(QtCore.QSize(33, 33))
        self.User_Button.setMaximumSize(QtCore.QSize(33, 33))
        self.User_Button.setStyleSheet("border-radius:17px;"
                                       "background-image:url(../icon/user.png);")
        self.User_Button.setObjectName("User_Button")

        self.Info_Box = QtWidgets.QComboBox(self.Search_group)
        self.Info_Box.setGeometry(QtCore.QRect(643, 26, 110, 22))
        self.Info_Box.setMinimumSize(QtCore.QSize(110, 22))
        self.Info_Box.setMaximumSize(QtCore.QSize(110, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.Info_Box.setFont(font)
        self.Info_Box.setStyleSheet("QComboBox{border-color:#C8C8C8;color: rgb(80, 80, 80);padding-left: 10px;}"
                                    "::drop-down{border: none;}"
                                    "::down-arrow{border-image:url(../icon/drop_down.png);}")
        self.Info_Box.setObjectName("Info_Box")
        self.Info_Box.addItem("User_Name")
        self.Info_Box.addItem("个人信息")
        self.Info_Box.addItem("切换帐号")

        self.Dividing_Search = QtWidgets.QLabel(self.Search_group)
        self.Dividing_Search.setGeometry(QtCore.QRect(766, 27, 8, 20))
        self.Dividing_Search.setMinimumSize(QtCore.QSize(8, 20))
        self.Dividing_Search.setMaximumSize(QtCore.QSize(8, 20))
        self.Dividing_Search.setText("|")
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(15)
        self.Dividing_Search.setFont(font)
        self.Dividing_Search.setObjectName("Dividing_Search")

        self.Min_Button = QtWidgets.QPushButton(self.Search_group)
        self.Min_Button.setGeometry(QtCore.QRect(790, 25, 25, 25))
        self.Min_Button.setMinimumSize(QtCore.QSize(25, 25))
        self.Min_Button.setMaximumSize(QtCore.QSize(25, 25))
        self.Min_Button.setStyleSheet(
            "QPushButton{background-image:url(../icon/min.png);border-radius:5px;}QPushButton:hover{background-image:url(../icon/min_hover.png);}")
        self.Min_Button.setObjectName("Min_Button")
        self.Min_Button.clicked.connect(MainWindow.showMinimized)  # 最小化单击事件

        self.Close_Button = QtWidgets.QPushButton(self.Search_group)
        self.Close_Button.setGeometry(QtCore.QRect(825, 25, 25, 25))
        self.Close_Button.setMinimumSize(QtCore.QSize(25, 25))
        self.Close_Button.setMaximumSize(QtCore.QSize(25, 25))
        self.Close_Button.setStyleSheet(
            "QPushButton{background-image:url(../icon/close.png);border-radius:5px;}QPushButton:hover{background-image:url(../icon/close_hover.png);}")
        self.Close_Button.setObjectName("Close_Button")
        self.Close_Button.clicked.connect(MainWindow.close)  # 关闭单击事件
        self.Search_group.raise_()
        self.User_Button.raise_()

        # 菜单列表和生成的对应页面
        self.setItemsPages()

        # 城市列表
        self.cityList()

        # 菜单对应的界面
        self.Dashboard()

        self.Statistics()

        self.Setting()

        self.horizontalLayout.addWidget(self.Right_Widget)
        MainWindow.setCentralWidget(self.centralwidget)

        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #  菜单列表和生成对应的页面
    def setItemsPages(self):
        self.List_Widget.setFrameShape(QtWidgets.QListWidget.NoFrame)
        self.List_Widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏滚动条
        self.List_Widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['Dashboard', 'Statistics', 'Setting']
        self.page = []
        self.button = []
        for i in range(len(list_str)):
            self.page.append(i)
            self.button.append(i)
            item = QtWidgets.QListWidgetItem(self.List_Widget)  # list_str[i],
            item.setIcon(QtGui.QIcon(f"C:/Users/Administrator/Desktop/Client_MainWindow/icon/{list_str[i]}.png"))
            item.setTextAlignment(QtCore.Qt.AlignCenter)

            item.setSizeHint(QtCore.QSize(60, 60))
            font = QtGui.QFont()
            font.setFamily("Verdana")
            font.setPointSize(16)
            item.setFont(font)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.List_Widget.addItem(item)  # 左侧选项的添加

            self.page[i] = QtWidgets.QWidget(self.Right_Pages)
            self.page[i].setObjectName(f"page{[i]}")
            self.Right_Pages.addWidget(self.page[i])

        # 列表与右侧的QWidgetIndex对应绑定
        self.List_Widget.itemClicked.connect(self.switch_stack)
        self.List_Widget.setCurrentRow(0)  # 默认选中列表中的第一个

    # 菜单按下跳转到第i个rightView
    def switch_stack(self):
        try:
            i = self.List_Widget.currentIndex().row()
            if i == 0:
                self.Search_Quality_Back.setHidden(False)
                self.Search_lineEdit.setHidden(False)
                self.City_Quality_Back.setHidden(False)
                self.City_Scroll.setHidden(False)
            elif i == 1:
                self.Search_Quality_Back.setHidden(False)
                self.Search_lineEdit.setHidden(False)
                self.City_Quality_Back.setHidden(False)
                self.City_Scroll.setHidden(False)
            elif i == 2:
                self.Search_Quality_Back.setHidden(True)
                self.Search_lineEdit.setHidden(True)
                self.City_Quality_Back.setHidden(True)
                self.City_Scroll.setHidden(True)

            self.Right_Pages.setCurrentIndex(i)
        except:
            pass

    # 城市列表
    def cityList(self):
        self.City_Quality_Back = QtWidgets.QLabel(self.Search_group)
        self.City_Quality_Back.setGeometry(QtCore.QRect(30, 76, 54, 30))
        self.City_Quality_Back.setMinimumSize(QtCore.QSize(45, 30))
        self.City_Quality_Back.setMaximumSize(QtCore.QSize(45, 30))
        self.City_Quality_Back.setText("城市")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.City_Quality_Back.setFont(font)
        self.City_Quality_Back.setObjectName("City_Quality_Back")

        self.City_Scroll = QtWidgets.QScrollArea(self.Search_group)
        self.City_Scroll.setGeometry(QtCore.QRect(47, 116, 791, 170))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.City_Scroll.sizePolicy().hasHeightForWidth())

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 3900, 170))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        '''
        1、需要城市数量
        2、需要城市拼音
        3、需要给按钮排序
        '''
        # city_name = SearchSQL().city_name[0]
        city_data = Clt.sendData(city_name="0 成都市")
        city_name = city_data[0]
        # city_pinyin = SearchSQL().city_name[1]
        city_pinyin = city_data[1]
        self.City_Button = []
        self.City_Dict = {}
        for i in range(len(city_name)):
            self.City_Button.append(i)

            self.City_Button[i] = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.City_Button[i].setMinimumSize(QtCore.QSize(145, 138))
            self.City_Button[i].setMaximumSize(QtCore.QSize(145, 138))
            self.City_Button[i].setObjectName("City_Button1")
            self.City_Button[i].setText(f"{city_name[i]}")
            font = QtGui.QFont()
            font.setFamily("等线")
            font.setPointSize(12)
            self.City_Button[i].setFont(font)

            # 此字典，存放按钮拼音名与其号数
            self.City_Dict[city_pinyin[i]] = i
            # 使用self.sender()时class Ui_MainWindow(QMainWindow):括号内必须是QMainWindow,不能是object
            self.City_Button[i].clicked.connect(
                lambda: bCustom.moveButton(self.sender().text()))
            # 默认选中第一个城市
            if i == 0:
                self.City_Button[i].setStyleSheet("QPushButton{"
                                                  "border-radius:10px;"
                                                  "text-align:bottom;"
                                                  "padding-bottom:2px;"
                                                  f"background-image:url(../city_pictures/{city_pinyin[i]}.png);"
                                                  "color: rgb(97, 101, 247);font:Bold 12.5pt '等线';}")
                self.City_Button[i].move(2, 6)
            else:
                self.City_Button[i].setStyleSheet("QPushButton{"
                                                  "border-radius:10px;"
                                                  "text-align:bottom;"
                                                  "padding-bottom:2px;"
                                                  f"background-image:url(../city_pictures/{city_pinyin[i]}.png);"
                                                  "}"
                                                  "QPushButton:hover{color: rgb(97, 101, 247);font:Bold 12.5pt '等线';}")
                self.City_Button[i].move(2 + 180 * i, 18)

        self.City_Scroll.setSizePolicy(sizePolicy)
        self.City_Scroll.setMinimumSize(QtCore.QSize(791, 170))
        self.City_Scroll.setMaximumSize(QtCore.QSize(791, 170))
        self.City_Scroll.setFrameShadow(QtWidgets.QFrame.Plain)
        self.City_Scroll.setLineWidth(1)
        self.City_Scroll.setMidLineWidth(0)
        self.City_Scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.City_Scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.City_Scroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.City_Scroll.setWidgetResizable(False)
        self.City_Scroll.setAlignment(QtCore.Qt.AlignCenter)
        self.City_Scroll.setObjectName("City_Scroll")
        self.City_Scroll.setWidget(self.scrollAreaWidgetContents)

    # Dashboard
    def Dashboard(self):
        self.Quality_Title = QtWidgets.QLabel(self.page[0])
        self.Quality_Title.setGeometry(QtCore.QRect(30, 20, 161, 30))
        self.Quality_Title.setMinimumSize(QtCore.QSize(161, 30))
        self.Quality_Title.setMaximumSize(QtCore.QSize(161, 30))
        self.Quality_Title.setText("城市空气质量预报")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Quality_Title.setFont(font)
        self.Quality_Title.setObjectName("Quality_Title")

        self.Quality_ScrollAreaWidgetContents = QtWidgets.QWidget(self.page[0])
        self.Quality_ScrollAreaWidgetContents.setGeometry(QtCore.QRect(47, 0, 850, 121))
        self.Quality_ScrollAreaWidgetContents.setObjectName("Quality_ScrollAreaWidgetContents")

        self.Quality_Icon = []
        self.Quality_Temperature = []
        self.Quality_Date = []
        self.Quality_Back = []
        quality_num, air_num = bCustom.weatherInfo()
        for i in range(len(quality_num)):
            self.Quality_Icon.append(i)
            self.Quality_Temperature.append(i)
            self.Quality_Date.append(i)
            self.Quality_Back.append(i)

            self.Quality_Icon[i] = QtWidgets.QPushButton(self.Quality_ScrollAreaWidgetContents)
            self.Quality_Icon[i].setMinimumSize(QtCore.QSize(50, 50))
            self.Quality_Icon[i].setMaximumSize(QtCore.QSize(50, 50))
            self.Quality_Icon[i].setObjectName("Quality_Icon")

            self.Quality_Temperature[i] = QtWidgets.QPushButton(self.Quality_ScrollAreaWidgetContents)
            self.Quality_Temperature[i].setMinimumSize(QtCore.QSize(80, 20))
            self.Quality_Temperature[i].setMaximumSize(QtCore.QSize(80, 20))
            font = QtGui.QFont()
            font.setFamily("Verdana")
            font.setPointSize(11)
            self.Quality_Temperature[i].setFont(font)
            self.Quality_Temperature[i].setStyleSheet("border-radius:7px;"
                                                      "background-color:none;")
            self.Quality_Temperature[i].setObjectName("Quality_Temperature")

            self.Quality_Date[i] = QtWidgets.QPushButton(self.Quality_ScrollAreaWidgetContents)
            self.Quality_Date[i].setMinimumSize(QtCore.QSize(80, 23))
            self.Quality_Date[i].setMaximumSize(QtCore.QSize(80, 23))
            font = QtGui.QFont()
            font.setFamily("Verdana")
            font.setPointSize(12)
            self.Quality_Date[i].setFont(font)
            self.Quality_Date[i].setStyleSheet("border-radius:7px;"
                                               "background-color:none;"
                                               "color: rgb(109, 109, 109);")
            self.Quality_Date[i].setObjectName("Quality_Date")

            self.Quality_Back[i] = QtWidgets.QPushButton(self.Quality_ScrollAreaWidgetContents)
            self.Quality_Back[i].setMinimumSize(QtCore.QSize(90, 110))
            self.Quality_Back[i].setMaximumSize(QtCore.QSize(90, 110))
            self.Quality_Back[i].setStyleSheet("QPushButton{border-radius:14px;"
                                               "background-color: rgb(247, 247, 247);"
                                               "border-color: rgb(223, 223, 223);"
                                               "border-width: 1.5px;"
                                               "border-style: solid;}"
                                               "::hover{background:rgb(225, 225, 225);}")
            self.Quality_Back[i].setObjectName("Quality_Back")

            self.Quality_Back[i].raise_()
            self.Quality_Icon[i].raise_()
            self.Quality_Temperature[i].raise_()
            self.Quality_Date[i].raise_()

            self.Quality_Icon[i].move(22 + 120 * i, 10)
            self.Quality_Temperature[i].move(7 + 120 * i, 64)
            self.Quality_Date[i].move(7 + 120 * i, 86)
            self.Quality_Back[i].move(2 + 120 * i, 5)

        self.Quality_Scroll = QtWidgets.QScrollArea(self.page[0])
        self.Quality_Scroll.setGeometry(QtCore.QRect(47, 65, 791, 121))
        self.Quality_Scroll.setMinimumSize(QtCore.QSize(791, 121))
        self.Quality_Scroll.setMaximumSize(QtCore.QSize(791, 121))
        self.Quality_Scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Quality_Scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Quality_Scroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Quality_Scroll.setWidgetResizable(False)
        self.Quality_Scroll.setObjectName("Quality_Scroll")
        self.Quality_Scroll.setWidget(self.Quality_ScrollAreaWidgetContents)
        self.Quality_Scroll.raise_()
        self.Quality_Title.raise_()

        # 修改天气预报
        self.Air_Title = QtWidgets.QLabel(self.page[0])
        self.Air_Title.setGeometry(QtCore.QRect(30, 210, 161, 30))
        self.Air_Title.setMinimumSize(QtCore.QSize(161, 30))
        self.Air_Title.setMaximumSize(QtCore.QSize(161, 30))
        self.Air_Title.setText("城市天气预报")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Air_Title.setFont(font)
        self.Air_Title.setObjectName("Quality_Title")

        self.Air_ScrollAreaWidgetContents = QtWidgets.QWidget(self.page[0])
        self.Air_ScrollAreaWidgetContents.setGeometry(QtCore.QRect(47, 0, 2405, 220))
        self.Air_ScrollAreaWidgetContents.setObjectName("Air_ScrollAreaWidgetContents")

        self.Air_Icon = []
        self.Air_Tpye = []
        self.Air_Temperature = []
        self.Air_Fx = []
        self.Air_Week = []
        self.Air_Date = []
        self.Air_Back = []
        for i in range(len(air_num)):
            self.Air_Icon.append(i)
            self.Air_Tpye.append(i)
            self.Air_Temperature.append(i)
            self.Air_Fx.append(i)
            self.Air_Week.append(i)
            self.Air_Date.append(i)
            self.Air_Back.append(i)

            self.Air_Icon[i] = QtWidgets.QPushButton(self.Air_ScrollAreaWidgetContents)
            self.Air_Icon[i].setMinimumSize(QtCore.QSize(50, 50))
            self.Air_Icon[i].setMaximumSize(QtCore.QSize(50, 50))
            self.Air_Icon[i].setObjectName("Air_Icon")

            self.Air_Tpye[i] = QtWidgets.QPushButton(self.Air_ScrollAreaWidgetContents)
            self.Air_Tpye[i].setMinimumSize(QtCore.QSize(120, 20))
            self.Air_Tpye[i].setMaximumSize(QtCore.QSize(120, 20))
            font = QtGui.QFont()
            font.setFamily("等线")
            font.setPointSize(11)
            self.Air_Tpye[i].setFont(font)
            self.Air_Tpye[i].setStyleSheet("border-radius:7px;"
                                           "background-color:none;")
            self.Air_Tpye[i].setObjectName("Air_Tpye")

            self.Air_Temperature[i] = QtWidgets.QPushButton(self.Air_ScrollAreaWidgetContents)
            self.Air_Temperature[i].setMinimumSize(QtCore.QSize(120, 20))
            self.Air_Temperature[i].setMaximumSize(QtCore.QSize(120, 20))
            font = QtGui.QFont()
            font.setFamily("Verdana")
            font.setPointSize(11)
            self.Air_Temperature[i].setFont(font)
            self.Air_Temperature[i].setStyleSheet("border-radius:7px;"
                                                  "background-color:none;")
            self.Air_Temperature[i].setObjectName("Air_Temperature")

            self.Air_Fx[i] = QtWidgets.QPushButton(self.Air_ScrollAreaWidgetContents)
            self.Air_Fx[i].setMinimumSize(QtCore.QSize(120, 20))
            self.Air_Fx[i].setMaximumSize(QtCore.QSize(120, 20))
            font = QtGui.QFont()
            font.setFamily("等线")
            font.setPointSize(11)
            self.Air_Fx[i].setFont(font)
            self.Air_Fx[i].setStyleSheet("border-radius:7px;"
                                         "background-color:none;")
            self.Air_Fx[i].setObjectName("Air_Fx")

            self.Air_Week[i] = QtWidgets.QPushButton(self.Air_ScrollAreaWidgetContents)
            self.Air_Week[i].setMinimumSize(QtCore.QSize(120, 20))
            self.Air_Week[i].setMaximumSize(QtCore.QSize(120, 20))
            font = QtGui.QFont()
            font.setFamily("等线")
            font.setPointSize(11)
            self.Air_Week[i].setFont(font)
            self.Air_Week[i].setStyleSheet("border-radius:7px;"
                                           "color: rgb(109, 109, 109);"
                                           "background-color:none;")
            self.Air_Week[i].setObjectName("Air_Week")

            self.Air_Date[i] = QtWidgets.QPushButton(self.Air_ScrollAreaWidgetContents)
            self.Air_Date[i].setMinimumSize(QtCore.QSize(120, 20))
            self.Air_Date[i].setMaximumSize(QtCore.QSize(120, 20))
            font = QtGui.QFont()
            font.setFamily("Verdana")
            font.setPointSize(12)
            self.Air_Date[i].setFont(font)
            self.Air_Date[i].setStyleSheet("border-radius:7px;"
                                           "background-color:none;"
                                           "color: rgb(109, 109, 109);")
            self.Air_Date[i].setObjectName("Air_Date")

            self.Air_Back[i] = QtWidgets.QPushButton(self.Air_ScrollAreaWidgetContents)
            self.Air_Back[i].setMinimumSize(QtCore.QSize(120, 210))
            self.Air_Back[i].setMaximumSize(QtCore.QSize(120, 210))
            self.Air_Back[i].setStyleSheet("QPushButton{border-radius:14px;"
                                           "background-color: rgb(247, 247, 247);"
                                           "border-color: rgb(223, 223, 223);"
                                           "border-width: 1.5px;"
                                           "border-style: solid;}"
                                           "::hover{background:rgb(225, 225, 225);}")
            self.Air_Back[i].setObjectName("Air_Back")

            self.Air_Back[i].raise_()
            self.Air_Icon[i].raise_()
            self.Air_Tpye[i].raise_()
            self.Air_Temperature[i].raise_()
            self.Air_Fx[i].raise_()
            self.Air_Week[i].raise_()
            self.Air_Date[i].raise_()

            self.Air_Icon[i].move(37 + 152 * i, 5)
            self.Air_Tpye[i].move(3 + 152 * i, 66)
            self.Air_Temperature[i].move(3 + 152 * i, 98)
            self.Air_Fx[i].move(3 + 152 * i, 126)
            self.Air_Week[i].move(3 + 152 * i, 154)
            self.Air_Date[i].move(3 + 152 * i, 181)
            self.Air_Back[i].move(2 + 152 * i, 4)

        self.Air_Scroll = QtWidgets.QScrollArea(self.page[0])
        self.Air_Scroll.setGeometry(QtCore.QRect(47, 250, 791, 220))
        self.Air_Scroll.setMinimumSize(QtCore.QSize(791, 220))
        self.Air_Scroll.setMaximumSize(QtCore.QSize(791, 220))
        self.Air_Scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Air_Scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Air_Scroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Air_Scroll.setWidgetResizable(False)
        self.Air_Scroll.setObjectName("Air_Scroll")
        self.Air_Scroll.setWidget(self.Air_ScrollAreaWidgetContents)

        # 必须在ScrollArea添加到其他控件后使用才有效
        self.scrollBar = self.Air_Scroll.horizontalScrollBar()
        self.scrollBar.setValue(300)

        # 设置空气质量预报按钮
        # bCustom.airButton()

    # Statistics
    def Statistics(self):
        f1 = open("../web/day_line.html", "w")
        f2 = open("../web/time_line.html", "w")
        f1.close()
        f2.close()
        self.browser = QWebEngineView()  # 右侧用QWebView来显示html网页,必须卸载QVBoxLayout框架前，不然无法刷新

        self.Widget_Page2 = QtWidgets.QWidget(self.page[1])
        self.Widget_Page2.setGeometry(QtCore.QRect(30, 20, 811, 491))
        self.Widget_Page2.setObjectName("Widget_Page2")

        self.Vb_Layout = QtWidgets.QVBoxLayout(self.Widget_Page2)
        self.Vb_Layout.setContentsMargins(0, 0, 0, 0)
        self.Vb_Layout.setSpacing(10)
        self.Vb_Layout.setObjectName("Vb_Layout")

        self.View_Title = QtWidgets.QLabel(self.Widget_Page2)
        self.View_Title.setMinimumSize(QtCore.QSize(161, 30))
        self.View_Title.setMaximumSize(QtCore.QSize(161, 30))
        self.View_Title.setText("城市空气质量图")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.View_Title.setFont(font)
        self.View_Title.setObjectName("View_Title")
        self.Vb_Layout.addWidget(self.View_Title)

        self.Vh_Layout = QtWidgets.QHBoxLayout()
        self.Vh_Layout.setObjectName("Vh_Layout")

        spacerItem = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Fixed)
        self.Vh_Layout.addItem(spacerItem)

        # 日报、时报
        self.Type_Box = QtWidgets.QComboBox(self.Widget_Page2)
        self.Type_Box.setMinimumSize(QtCore.QSize(70, 22))
        self.Type_Box.setMaximumSize(QtCore.QSize(70, 22))
        self.Type_Box.setStyleSheet("QComboBox{"
                                    "border-color:#C8C8C8;"
                                    "color: rgb(80, 80, 80);"
                                    "border-style:solid;"
                                    "border-width: 0.5 0.5 0.5 0.5;"
                                    "border-radius: 4px;"
                                    "padding-left: 5px;}"
                                    "::drop-down{border: none; }"
                                    "::down-arrow{border-image:url(../icon/drop_down.png);}")
        self.Type_Box.setObjectName("Type_Box")
        self.Type_Box.addItem("时报")
        self.Type_Box.addItem("日报")
        self.Type_Box.currentTextChanged.connect(bCustom.choiceAirItem)
        self.Vh_Layout.addWidget(self.Type_Box)

        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        self.Vh_Layout.addItem(spacerItem1)
        self.Vb_Layout.addLayout(self.Vh_Layout)

        spacerItem2 = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        self.Vb_Layout.addItem(spacerItem2)

        url_list = ['day_line.html', 'time_line.html']
        with open(f"../web/{url_list[1]}", 'r') as html:
            self.browser.setHtml(html.read())  # 设置网页
        html.close()
        self.Vb_Layout.addWidget(self.browser)

    # Setting
    def Setting(self):
        pass


# 按钮自定义
class ButtonCustom:
    def __init__(self):
        # 在数据库中查找出城市名
        ''' 每次点击都会调用SearchSQL函数，过后需要优化'''
        # city_pinyin = SearchSQL().city_name[1]
        city_pinyin = Clt.sendData(city_name="0 成都市")[1]
        # 记录默认按钮的拼音名字和号数
        self.button_flag = {"new": city_pinyin[0] + "_0", "old": city_pinyin[0] + "_0"}

    # 按钮弹起，第一个界面
    def moveButton(self, button_name="成都市"):
        pinyin = Pinyin()
        city_name = re.sub('-', '', pinyin.get_pinyin(button_name))
        ui.City_Button[ui.City_Dict[city_name]].move(2 + 180 * ui.City_Dict[city_name], 6)
        ui.City_Button[ui.City_Dict[city_name]].setStyleSheet(
            "border-radius:10px;"
            "text-align:bottom;"
            "padding-bottom:2px;"
            f"background-image:url(../city_pictures/{city_name}.png);"
            "color: rgb(97, 101, 247);font:Bold 12.5pt '等线';")

        # 记录新按下的按钮作为老的按钮，下一次按下其他按钮时，可以对老按钮进行还原
        # 它就像一个开关，按下新按钮时关闭旧按钮
        self.button_flag["old"] = self.button_flag["new"]
        # 当按下同一个按钮时不做按钮还原操作
        if self.button_flag["old"] != city_name + "_" + str(ui.City_Dict[city_name]):
            # 按钮还原函数
            self.Reduction(self.button_flag)
        self.button_flag["old"] = self.button_flag["new"]
        self.button_flag["new"] = city_name + "_" + str(ui.City_Dict[city_name])

        self.weatherInfo(button_name)  # 天气温度信息获取整理 weatherInfo

        # 以下函数是按下城市按钮，其他控件做出的相应
        self.airButton()

        # 生成新的网页，并在软件界面刷新新的网页
        self.createHtml(button_name)

    # 将弹起的按钮还原，第一个界面
    def Reduction(self, name_num):
        # 存放上一个选中按钮的名字和按钮的号数
        old = name_num["old"].split("_")
        ui.City_Button[int(old[1])].move(2 + 180 * int(old[1]), 18)
        ui.City_Button[int(old[1])].setStyleSheet(
            "QPushButton{border-radius:10px;"
            "text-align:bottom;"
            "padding-bottom:2px;"
            f"background-image:url(../city_pictures/{old[0]}.png);"
            "}"
            "QPushButton:hover{color: rgb(97, 101, 247);font:Bold 12.5pt '等线';}")

    # 天气信息获取整理
    def weatherInfo(self, button_name="成都市"):
        # Msg_Quality_Back的信息生成
        # result_msg = SearchSQL().temperature(button_name)  # 查询选中城市的所有的字段数据
        result_msg = Clt.sendData(city_name=f"2 {button_name}")
        self.times_msg = []
        self.week = []
        self.high_low = []
        self.temperature = []
        self.shidu = []
        self.fx = []
        self.fl = []
        self.types = []
        self.notice = []
        self.cityname = result_msg[0][1]

        for i in range(len(result_msg)):
            self.times_msg.append(result_msg[i][2])
            self.week.append(result_msg[i][3])
            self.high_low.append(result_msg[i][4])
            self.temperature.append(result_msg[i][5])
            self.shidu.append(result_msg[i][6])
            self.fx.append(result_msg[i][7])
            self.fl.append(result_msg[i][8])
            self.types.append(result_msg[i][9])
            self.notice.append(result_msg[i][10])

        '''
            1、主要污染物
            2、aqi指数
            3、日期（需要转换）
        '''
        # result_pre = SearchSQL().prediction(button_name)
        result_pre = Clt.sendData(city_name=f"1 {button_name}")
        self.pullutant = result_pre[3].split(",")  # 主要污染物列表
        self.aqi = result_pre[4].split(",")  # api区间
        self.times_pre = []
        for i in range(len(self.pullutant)):
            temp_times = datetime.datetime.now()  # 将文本型日期转换成日期型数据
            delta = datetime.timedelta(days=i)  # 构造往后几天的天数
            n_days = temp_times + delta  # 生成往后几天的日期
            self.times_pre.append(n_days.strftime('%b %d'))

        return self.pullutant, self.times_msg

    # 选中城市的天气预报详细信息的生成
    def airButton(self):
        # TodayButton内的图标设置
        ui.Msg_Icon.setStyleSheet("background-color:none;")
        pixmap = QtGui.QPixmap(f"../icon/weather/{self.types[0]}.png")
        ui.Msg_Icon.setPixmap(pixmap)  # 在Quality_Back上显示图片
        ui.Msg_Icon.setScaledContents(True)  # 让图片自适应Quality_Back大小

        ui.Msg_Days.setText(self.types[0])
        ui.Msg_Time.setText(self.times_msg[0].split(" ")[1])
        ui.Msg_Date.setText(self.times_msg[0].split(" ")[0])
        ui.Msg_Temper.setText(f"{self.temperature[0]}℃")
        ui.Msg_City.setText(self.cityname)
        ui.Humidity_Scale.setText(self.shidu[0])
        ui.Humidity_Bar.setProperty("value", int(re.sub("%", "", self.shidu[0])))

        # Quality_Scroll内的图标设置
        for i in range(len(self.pullutant)):
            ui.Quality_Icon[i].setStyleSheet("border-radius:7px;"
                                             "background-color:none;"
                                             f"background-image:url(../icon/airQuality/{self.pullutant[i]}.png);"
                                             )
            ui.Quality_Temperature[i].setText(self.aqi[i])
            ui.Quality_Date[i].setText(self.times_pre[i])

        # Air_Scroll内的图标设置
        for i in range(len(self.times_msg)):
            ui.Air_Icon[i].setStyleSheet("border-radius:7px;"
                                         "background-color:none;"
                                         f"background-image:url(../icon/weather/{self.types[i]}.png);"
                                         )
            ui.Air_Tpye[i].setText(self.types[i])
            ui.Air_Temperature[i].setText(self.high_low[i])
            ui.Air_Fx[i].setText(self.fx[i])
            ui.Air_Week[i].setText(self.week[i])
            if i == 0:
                temp_times = self.times_msg[i].split(" ")[0]
                ui.Air_Date[i].setText(temp_times)
            else:
                ui.Air_Date[i].setText(self.times_msg[i])

    # 生成日报时报的html网页
    def createHtml(self, button_name="成都市"):
        web = PyechartWeb()
        web.createView(Clt, button_name)
        # 刷新新生成的网页
        self.url_list = ['time_line.html', 'day_line.html']
        url = self.url_list[0]
        if ui.Type_Box.currentText() == "日报":
            url = self.url_list[1]
        with open(f"../web/{url}", 'r') as html:
            ui.browser.setHtml(html.read())
        html.close()

    def choiceAirItem(self):
        url = self.url_list[0]
        if ui.Type_Box.currentText() == "日报":
            url = self.url_list[1]

        with open(f"../web/{url}", 'r') as html:
            ui.browser.setHtml(html.read())
        html.close()

    def getValue(self):
        city_name = ui.Search_lineEdit.text()
        text = re.search(".*?市$", city_name)
        if text == None:
            city_name = ui.Search_lineEdit.text() + '市'
        # tt = SearchSQL().searchCity(city_name)  # 判断输入的城市名数据库是否查得到
        tt = Clt.sendData(city_name=f"4 {city_name}")

        if tt != ():
            self.moveButton(city_name)
        elif tt == ():
            messageBox = QMessageBox()
            messageBox.setWindowTitle('输入错误')
            messageBox.setText('请重新输入所要查询的城市名...')
            messageBox.addButton(QtWidgets.QPushButton('确定'), QMessageBox.YesRole)
            messageBox.exec_()

            ui.Search_lineEdit.clear()
            ui.Search_lineEdit.setFocus()


class XX(QMainWindow):
    def __init__(self):
        super().__init__()
        self.m_flag = False

    # def keyPressEvent(self, event):
    #     print("12345")
    # def mousePressEvent(self,event):
    #     if event.button() == Qt.LeftButton:
    #         print("鼠标左键点击！")
    #         # print(event.pos().x(),event.pos().y())
    #     if event.button() == Qt.RightButton:
    #         print("鼠标右键点击！")

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = QMouseEvent.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            QMouseEvent.accept()
            # self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # web = PyechartWeb("成都市")
    Clt = Client()
    MainWindow = XX()
    bCustom = ButtonCustom()

    ui = XM_MainWindow()
    ui.setupUi(MainWindow)
    bCustom.moveButton()  # 打开界面后自动生成左下角图片
    MainWindow.show()

    sys.exit(app.exec_())

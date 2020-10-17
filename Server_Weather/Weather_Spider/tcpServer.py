# coding: UTF-8
'''
    !/usr/bin/python3
    @Time    : 2020/3/23 10:15
    @Author  : Walden
    @ProjectName： Weather_Spider
    @File    : tcpServer.py
    @ProductName ： PyCharm
'''

import socket
import json
import re
import time
# from Weather_Spider.spiders.SearchSQL import SearchSQL

from spiders.SearchSQL import SearchSQL
HOST = '127.0.0.1'
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST, PORT)
isClose = False


def Close(Ser):
    Ser.close()


if __name__ == "__main__":
    while not isClose:
        print("\n>>>Create a socket successfully...")
        Ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        Ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 地址复用

        Ser.bind(ADDR)

        Ser.listen(5)
        clnt, addr = Ser.accept()
        print("Capture to a connection:", addr)  # 捕获到一个连接
        while True:
            try:
                clt_data = clnt.recv(BUFSIZ)
                # 选择调用哪个函数
                t = clt_data.decode().split(" ")[0]
                city_name = clt_data.decode().split(" ")[1]
                print("Client input code and cityName:", clt_data.decode())

                if not clt_data:
                    print("Client did not send data... ")
                    isClose = True
                    break

            except Exception as err:
                # 关闭客户端，服务器不会报错
                if re.search(".*?关闭.*?连接。$", str(err)):
                    Close(Ser)
                    print(err)
                    break
                elif re.search(".*?Broken pipe$", str(err)):
                    Close(Ser)
                    print(err)
                    break
                elif re.search(".*?Connection reset by peer$", str(err)):
                    Close(Ser)
                    print(err)
                    break
                # 输入有误，服务器返回客户端错误信息
                clnt.sendall(str(err).encode())
                break

            if t == '0':
                default = SearchSQL().city_name
            elif t == '1':
                default = SearchSQL().prediction(city_name)
            elif t == '2':
                default = SearchSQL().temperature(city_name)
            elif t == '3':
                default = SearchSQL().airDatas(city_name)
            elif t == '4':
                default = SearchSQL().searchCity(city_name)
            else:
                # 当没有前面几个数字的时候返回调用函数错误
                clnt.sendall("No function number...".encode())
                break

            if default == None:
                clnt.sendall(f"Search is {default}...".encode())
                print("Search is None...\n")
            else:
                clnt.sendall(json.dumps(default).encode())
                print("Data returned successfully...\n")



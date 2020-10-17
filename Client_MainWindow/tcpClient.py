'''
    @Time    : 2020/3/23 16:04
    @Author  : Walden
    @ProjectName： Weather_Spider_
    @File    : testClient.py
    @ProductName ： PyCharm
'''

import socket
import json
import re


class Client:
    def __init__(self):
        with open("../config.cfg", "r") as host:
            addr = json.loads(host.read())
        host.close()
        HOST = addr["host"]
        PORT = addr["port"]
        ADDR = (HOST, PORT)

        self.BUFSIZ = 4096
        self.Clt = socket.socket()
        self.Clt.connect(ADDR)

    def sendData(self, city_name):
        while True:
            if city_name == '':
                continue
            # 给服务器发送信息
            self.Clt.sendall(city_name.encode())

            # 接受服务器返回的信息
            data = self.Clt.recv(self.BUFSIZ)  # bytes类型
            # 如果发送数据错误，服务器也会返回错误提醒，并继续执行客户端
            if not re.search("^\[.*?]$", data.decode()) and not re.search("^{.*?}$", data.decode()):
                # print("Send to Server data is error:\n", data.decode())
                break

            # print(json.loads(data.decode()))
            return json.loads(data.decode())

        # self.Clt.close()
if __name__ =="__main__":
    Client()
#coding=utf-8

from socket import *  
HOST = 'localhost'              #设置自己主机
PORT = 21533                    #端口必须和服务器设置的一致
BUFSIZ = 1024 
ADDR = (HOST, PORT)   
tcpCliSock = socket(AF_INET, SOCK_STREAM)  
tcpCliSock.connect(ADDR)       #连接，而不是监听
while True:                    #死循环
    data = raw_input('> ')     #等待用户输入
    if not data:               #如果为空，则，跳出死循环，执行tcpCliSock.close() 
        break  
    tcpCliSock.send(data)      #如果不空，则发送
    data = tcpCliSock.recv(BUFSIZ)   #接受服务器数据，并且处理，其处理过程是在此date之前加入时间
    if not data:                    #接受数据为空，则，退出
        break
    print data                 #打印数据
tcpCliSock.close() 

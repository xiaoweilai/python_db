
#coding=utf-8
 
from socket import *  
from time import ctime  
HOST = ''                       #空字符表示不绑定如何ip，如何ip都可以与此服务器连接
PORT = 21533                    #端口是随机的，但是不能用与计算机其他程序端口重复，建议1024-65535。还有值得注意，如果此脚本运行2次，则会出现错误，第二次需                                #要改动代码，因为关闭此脚本时，没有关闭端口，第二次运行时，21533已经存在。要么命令行去关闭端口，要么重启，要么改程序。
BUFSIZ = 1024                   #缓存大小，我只发字符，这里设置为1k足以。发送大东西，需要用循环。
ADDR = (HOST,PORT)               #绑定
tcpSerSock = socket(AF_INET,SOCK_STREAM)        # SOCK_STREAM指的是tcp
tcpSerSock.bind(ADDR)                           #绑定
tcpSerSock.listen(5)                            #监听
 
while True:                                     #死循环
    print 'waiting for connection...'           #打印
    tcpCliSock, addr = tcpSerSock.accept()      #接受消息，当有消息接收后，才会再向下执行
    print '...connected from:', addr            #接受到消息后，打印消息
    while True:                                 #又一个死循环。除非接收到消息为空，才会跳出次循环
        data = tcpCliSock.recv(BUFSIZ)          #设置数据大小
        if not data:                            #如上上所述，数据为空，则结束此层循环
            break  
        tcpCliSock.send('[%s] %s'%(ctime(), data))    #发送消息到客户端，消息为“服务器时间”+“客户端接收到的消息”
    
tcpCliSock.close()                             #最后2行代码永远不会被执行，因为前面是死循环，这也造成了，我之前说的，第二次执行代码是会出错。
tcpSerSock.close()  

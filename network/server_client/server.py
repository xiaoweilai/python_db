
#coding=utf-8
 
from socket import *  
from time import ctime  
HOST = ''                       #���ַ���ʾ�������ip�����ip��������˷���������
PORT = 21533                    #�˿�������ģ����ǲ�������������������˿��ظ�������1024-65535������ֵ��ע�⣬����˽ű�����2�Σ������ִ��󣬵ڶ�����                                #Ҫ�Ķ����룬��Ϊ�رմ˽ű�ʱ��û�йرն˿ڣ��ڶ�������ʱ��21533�Ѿ����ڡ�Ҫô������ȥ�رն˿ڣ�Ҫô������Ҫô�ĳ���
BUFSIZ = 1024                   #�����С����ֻ���ַ�����������Ϊ1k���ԡ����ʹ�������Ҫ��ѭ����
ADDR = (HOST,PORT)               #��
tcpSerSock = socket(AF_INET,SOCK_STREAM)        # SOCK_STREAMָ����tcp
tcpSerSock.bind(ADDR)                           #��
tcpSerSock.listen(5)                            #����
 
while True:                                     #��ѭ��
    print 'waiting for connection...'           #��ӡ
    tcpCliSock, addr = tcpSerSock.accept()      #������Ϣ��������Ϣ���պ󣬲Ż�������ִ��
    print '...connected from:', addr            #���ܵ���Ϣ�󣬴�ӡ��Ϣ
    while True:                                 #��һ����ѭ�������ǽ��յ���ϢΪ�գ��Ż�������ѭ��
        data = tcpCliSock.recv(BUFSIZ)          #�������ݴ�С
        if not data:                            #����������������Ϊ�գ�������˲�ѭ��
            break  
        tcpCliSock.send('[%s] %s'%(ctime(), data))    #������Ϣ���ͻ��ˣ���ϢΪ��������ʱ�䡱+���ͻ��˽��յ�����Ϣ��
    
tcpCliSock.close()                             #���2�д�����Զ���ᱻִ�У���Ϊǰ������ѭ������Ҳ����ˣ���֮ǰ˵�ģ��ڶ���ִ�д����ǻ����
tcpSerSock.close()  

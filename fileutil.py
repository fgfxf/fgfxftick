#!/usr/bin/python
#coding=utf-8

#
#读取单行文件
#
#返回字符串
#
def readCookieFromFile(filename):
    #从文件读取cookie
    f=open(filename,mode='r')
    getfilecookie=f.read()
    f.close
    getfilecookie=getfilecookie.split('\n')
    getfilecookie=getfilecookie[0].strip()
    return getfilecookie


#
#
#清空文件 并写入一行字符串
#

def writeCookieToFile(filename,NewCookie):
    f=open(filename,mode='w')
    f.write(NewCookie)
    f.close()
    return 1


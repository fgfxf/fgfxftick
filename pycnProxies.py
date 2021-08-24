#!/usr/bin/python
#coding=utf-8
import requests
import json
import re
import socket
import socks

#
#模块开发：河南师范大学 fgfxf
#
#模块名称：Python 品易代理模块
#
#官网：http://pc.py.cn/
#
proxies={'http':'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'}  # debug查看发包
def testProxies():
    #连接iptool.lu测试ip
    url="https://ip.tool.lu"
    UA={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'}
    response=requests.get(url=url,headers=UA)
    return response.text

def Str2IP(ipstr):
    ex=r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    ret=re.findall(ex,ipstr,re.S)
    return ret[0]

def setSocketProxies(ip,port):
    socks.set_default_proxy(socks.SOCKS5, ip,port)
    socket.socket = socks.socksocket
    return "设置"+ip+":"+str(port)+"为socket代理"

def loginPYCNProxies(USERNAME,PASSWORD):
    IndexUrl="http://pc.py.cn/"
    UA={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'}
    print(requests.get(url=IndexUrl,headers=UA))
    loginUrl="http://pycn.yapi.3866866.com/login"
    headers={
    'POST':'/login HTTP/1.1',
    'Host':'pycn.yapi.3866866.com',
    'Content-Length': '47',
    'Accept': 'text/html, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://pc.py.cn',
    'Referer': 'http://pc.py.cn/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'close'
    }
    data={
    'phone':USERNAME,
    'password':PASSWORD,
    'remember':0
    }
    resp=requests.post(url=loginUrl,headers=headers,data=data)
    token=json.loads(resp.text)
    token=token.get('ret_data').get("token")
    return token
    
def AddWhiteList(ip,token):
    url="http://pycn.yapi.3866866.com/user/save_white_ip"
    headers={
    'POST':'/user/save_white_ip HTTP/1.1',
    'Host':'pycn.yapi.3866866.com',
    'Content-Length': '10',
    'Accept': 'text/html, */*; q=0.01',
    'Authorization':'Bearer '+ token,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://pc.py.cn',
    'Referer': 'http://pc.py.cn/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'close'

    }
    data={
     'ip':ip
    }
    resp=requests.post(url=url,headers=headers,data=data)
    return resp.text

def GetProxiesIPlist(API):
    UA={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'}
    response=requests.get(url=API,headers=UA).text
    return response



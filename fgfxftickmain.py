#!/usr/bin/python
#coding=utf-8
import pycnProxies as pycn
import fileutil as fileutil
import htusign as htusign
import randomLocate as randomLocate
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


##########个人变量##########
#API设置为txt文本格式，以\r\n结束,格数  IP:PORT\r\nIP:PORT  最好是单行的
#github

import os
GETPROXIESAPI=os.environ["GETPROXIESAPI"]
USERNAME=os.environ["USERNAME"]
PASSWORD=os.environ["PASSWORD"]
YOURPHONE=os.environ["YOURPHONE"]
EMERGENCYPHONE=os.environ["EMERGENCYPHONE"]
CONTACTS=os.environ["CONTACTS"]
COOKIEFILE=os.environ["COOKIEFILE"]
G_COOKIES=os.environ["G_COOKIES"]
LOCATE=os.environ["LOCATE"]
ANS=os.environ["ANS"]


##########全局变量##########

HtuCookie=""
NewCookie=""
LocateList=LOCATE.split(';')
##########main函数##########
def exit(code):
    raise
    
#随机休眠
import random
import time

SleepTime=random.randint(60*15,1.5*60*60)  #随机时间   单位秒
print("休眠"+str(SleepTime/60)+"分钟")

time.sleep(SleepTime)   #休眠  单位秒   GitHub最多支持运行6小时


FileCookie=fileutil.readCookieFromFile(COOKIEFILE)
print("【+】从文件读取cookie："+FileCookie)
HtuCookie=FileCookie
OldCookie=G_COOKIES+";"+HtuCookie+";"


#代理ip处理
checkip=pycn.testProxies() #测试当前ip  和归属地
print(checkip)
currentip=pycn.Str2IP(checkip)  #提取ip
time.sleep(1)
token=pycn.loginPYCNProxies(USERNAME,PASSWORD) #登录pycn
time.sleep(3)
print("【info】提取前先将ip加入到白名单:",end="")
print(pycn.AddWhiteList(currentip,token))
time.sleep(3)


circle=0
iplist=pycn.GetProxiesIPlist(GETPROXIESAPI) #获取代理ip
IpDict=iplist.split("\r\n")
while(1):
    
    print("【+】获取到代理ip:"+IpDict[circle])
    if(len(IpDict)-2 <circle):
        exit(0)
    proxiesIP=IpDict[circle].split(':')
    proxiesPort=proxiesIP[1]
    proxiesIP=proxiesIP[0]
    _socket=pycn.setSocketProxies(proxiesIP,int(proxiesPort))
    try:
        checkfakeip=pycn.testProxies()#测试当前ip  和归属地
        break
    except:
        pycn.RecoverSocket(_socket)
        print("【!】检测到代理ip失效！进入了循环！")
        time.sleep(3)
        circle=circle+1
        if(circle<10):
            continue
        else:
            raise 
print(checkfakeip)

#!代理ip处理结束

#HTU正式处理
responseFromWX=htusign.GetFromWX(OldCookie)
print(responseFromWX)
if(responseFromWX.status_code==302):
    print("【+】GetFromWX成功！")
else:
    print("【x】GetFromWX失败！")
    exit(0)
time.sleep(0.3)
responseStuCen=htusign.GetStudentCenter(OldCookie)
print(responseStuCen)
if(responseStuCen.status_code==200):
    print("【+】获取学生中心成功！")
    HtuCookie=responseStuCen.headers['Set-Cookie'].split(';')
    HtuCookie=HtuCookie[0]
    print("【*】新的cookie为："+HtuCookie)
else:
    print("【x】获取学生中心失败！")
    exit(0)
time.sleep(2)

if(FileCookie==HtuCookie):
    print("【info】平台cookie没有发生改变！")
else:
    print("【***】平台cookie发生改变了,新的cookie为： "+NewCookie)
    ret=fileutil.writeCookieToFile(COOKIEFILE,HtuCookie)
    if(ret):
        print("【+】新cookie已经写入文件！")

NewCookie=G_COOKIES+";"+HtuCookie+";"
responseTick=htusign.GetTickIndex(NewCookie)
print(responseTick)
if(responseTick.status_code==200):
    print("【+】获取打卡页面成功！")
    if(148==responseTick.text.count("label")):
        print("******************")
        print("*表单没有发生更改*")
        print("******************")
    else:
        print("xxxxxxxxxxxxxxxxxx")
        print("xx表单发生了更改xx")
        print("xxxxxxxxxxxxxxxxxx")
        exit(0)
    
else:
    print("【x】获取打卡页面失败！")
    exit(0)
time.sleep(2)
print(htusign.GetJSticket(NewCookie))
time.sleep(3)
GPSstr=randomLocate.randomGPSlocate(SleepTime,LocateList,ANS)
print("【+】随机地点为"+GPSstr)

data={
    'form_id':18461,
    'formdata[v]':GPSstr,  #v 位置
                        # 0 为是，1为否
    'formdata[q]':1,   #q 您是否在校 
    'formdata[z]':0,   #z 学生身份 0：本科生 1：硕士生 2：博士生 3：新联学院学生 4：预科生 5：成教生 6：留学生
    'formdata[x]':1,   #x 接触人群中是否有进口冷链食品、口岸直接接触进口货物、隔离场所、交通运输工具等特殊行业从业人员
    'formdata[w]':1,   #w 当前位置是否在中高风险区
    'formdata[a]':0,   #a 是否接种过疫苗
    'formdata[y]':1,   #y 已接种几针（0：一针头 1：两针 2：三针）
    'formdata[b]':'36.5',#temperature=random.randint(1,9) #随机体温  36.1~36.8
    'formdata[c]':1,   #c 是否有症状
    'formdata[d]':1,   #d 是否发热（37.3度及以上）
    'formdata[e]':1,   #e 是否被确诊为新型冠状病毒肺炎病例
    'formdata[f]':1,   #f 是否是高度疑似新型冠状病毒肺炎人员
    'formdata[g]':'',  #g 若高度疑似，具体隔离措施为
    'formdata[h]':1,   #h 假期（近14天）是否去过中高风险区
    'formdata[i]':1,   #i 假期（近14天）中是否与确诊的新型冠状病毒人员接触
    'formdata[j]':1,   #j 假期（近14天）中是否途径/中转/停留中高风险区
    'formdata[k]':1,   #k 近期您的家人朋友，是否有发热、咳嗽、乏力、呼吸困难等症状
    'formdata[l]':1,   #L 近14天是否与来自中高风险区其他地市的亲朋好友或有发热、咳嗽、呼吸困难、感冒等症状的亲友接触过
    'formdata[m]':0,   #m 今日心里健康状况# 0：健康 1：偶有情绪波动但能自我调节 2：较差，需要心理协助
    'formdata[r]':YOURPHONE,  #r 本人电话
    'formdata[s]':CONTACTS,   #s 紧急联系人姓名
    'formdata[t]':EMERGENCYPHONE,#t 紧急联系人手机号
    'formdata[u]':'',   #u 您需要学校提供跟此次疫情相关的协助说明
    '_bjmf_fields_s':"{\"gps\":[\"v\"]}"
}

# 是否申请返校
#n   =  1
# 是否在返校途中
#o   =  1
# 是否返回学校所在地
#p   =  1

response=htusign.PostTickData(data,NewCookie)
#print(response)
import re
ex='<div class="desc">(.*?)</div>'
result=re.findall(ex,response,re.S)
print(result)
ex2='layui.layer.alert\(\'(.*?)\'\);'
result2=re.findall(ex2,response,re.S)
print(result2)
checkip=pycn.testProxies()
print(checkip)


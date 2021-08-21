#!/usr/bin/python
#coding=utf-8
import requests
import re
import random
import time

proxies={'http':'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'}  # debug查看发包

url1="http://htu.banjimofang.com/student/course/31028/profiles/6099"

x=random.randint(368,410) #随机后n位GPS制造飘逸假象
y=random.randint(56,85)  #随机后n位GPS制造飘逸假象
temperature=random.randint(1,9) #随机体温  36.1~36.8

sleeptime=random.randint(60,3600)  #随机时间   单位秒
print("休眠"+str(sleeptime/60)+"分钟")
GPSlocate=["仰韶路","仰韶路渑池县第三小学东50米(仰韶路北)","仰韶路渑池县第三小学东北100米(仰韶路北)","仰韶路渑池县第三小学东100米(仰韶路北)"]
locate=random.randint(0,len(GPSlocate)-1)
time.sleep(sleeptime)   #休眠  单位秒   GitHub最多支持运行6小时

data1={
    'form_id':18461,
    'formdata[v]':'河南省,三门峡市,渑池县,'+GPSlocate[locate]+'|34.76'+str(x)+',111.749'+str(y),
    'formdata[q]':1,
    'formdata[x]':1,
    'formdata[w]':1,
    'formdata[a]':0,
    'formdata[y]':1,
    'formdata[b]':'36.'+str(temperature),
    'formdata[c]':1,
    'formdata[d]':1,
    'formdata[e]':1,
    'formdata[f]':1,
    'formdata[g]':'',
    'formdata[h]':1,
    'formdata[i]':1,
    'formdata[j]':1,
    'formdata[k]':1,
    'formdata[l]':1,
    'formdata[m]':0,
    'formdata[r]':'15238981687',
    'formdata[s]':'马小林',
    'formdata[t]':'15838942258',
    'formdata[u]':'',
    '_bjmf_fields_s':"{\"gps\":[\"v\"]}"
}
headers1={
    'Host': 'htu.banjimofang.com',
    'Connection': 'close',
    'Content-Length': '591',
    'Cache-Control':'max-age=0',
    'Origin': 'https://htu.banjimofang.com',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User':'?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://htu.banjimofang.com/student/course/31028/profiles/6099',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cookie':'remember_student_59ba36addc2b2f9401580f014c7f58ea4e30989d=970776%7CglFkBf2nDmDNiicluZpIsSUu6PL3Ipm8uABiXErJ075NyBViv7h6aLzI9zrn%7C; wxid=oIalJ5trVbPsjFZXf3Cm8IDpOnPU$1628859127$0509ee11712997a2c85e03a1afb78b30; yxktmf=6Ra43JQVWjWhWJe4jPj2STcifASyfLFzSJhonojP',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SPN-AL00 Build/HUAWEISPN-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045709 Mobile Safari/537.36 MMWEBID/7142 MicroMessenger/8.0.7.1920(0x28000737) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
}

resp=requests.post(url=url1,verify=False,data=data1,headers=headers1).text
print(resp)
ex='<div class="desc">(.*?)</div>'
result=re.findall(ex,resp,re.S)
print(result)

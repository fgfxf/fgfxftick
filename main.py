#!/usr/bin/python
#coding=utf-8
import requests
import re
import random
import time
import hashlib



#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

f=open("fgfxf.cookie",mode='r')
getfilecookie=f.read()
f.close
print("从文件读取  "+getfilecookie)

proxies={'http':'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'}  # debug查看发包
G_cookies="wxid=oIalJ5trVbPsjFZXf3Cm8IDpOnPU$1628859127$0509ee11712997a2c85e03a1afb78b30;  remember_student_59ba36addc2b2f9401580f014c7f58ea4e30989d=970776%7C08VGk8e2eimW5CdMomQPnJsUwFOn2epeyW5hEebhxt4swh5NAZ1hc3fLwA6N%7C"
平台cookie=getfilecookie
oldcookie=G_cookies+";"+平台cookie+ ";"

def getformwx(firstcookie):
    url="http://htu.banjimofang.com/student?from=wx"
    print("模拟微信初次进入获取平台cookie")
    print(firstcookie)
    headers={
    'GET':'/student?from=wx HTTP/1.1',
    'Host': 'htu.banjimofang.com',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Linux; Android 10; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36 MMWEBID/5976 MicroMessenger/8.0.6.1900(0x28000653) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User':'?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'none',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cookie':firstcookie
    }
    resp=requests.get(url=url,verify=False,headers=headers,timeout=(3,3),allow_redirects=False)
    print(resp.status_code)
    if(resp.status_code==302):
        print("getformwx成功")
        return 1
    else:
        return 0
    
    


def get学生中心表单(secondcookie):
    url="http://htu.banjimofang.com/student/course/31028"
    print("模拟从微信进入个人中心")
    headers={
    'GET':'/student/course/31028 HTTP/1.1',
    'Host': 'htu.banjimofang.com',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Linux; Android 10; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36 MMWEBID/5976 MicroMessenger/8.0.6.1900(0x28000653) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User':'?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'none',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cookie':secondcookie
    }
    resp=requests.get(url=url,verify=False,headers=headers,timeout=(3,3),allow_redirects=False)
    print(resp.status_code)
    if(resp.status_code==200):
        print("get学生中心表单成功")
        #print(resp.headers['Set-Cookie'])
        getcookie=resp.headers['Set-Cookie'].split(';')
        print("新的cookie为：   "+getcookie[0])
        return getcookie[0]
    else:
        return "error"
    
def get打卡表单(thirdcookie):
    url="http://htu.banjimofang.com/student/course/31028/profiles/6099"
    print("模拟获取打卡界面")
    headers={
    'GET':'/student/course/31028/profiles/6099 HTTP/1.1',
    'Host': 'htu.banjimofang.com',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Linux; Android 10; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36 MMWEBID/5976 MicroMessenger/8.0.6.1900(0x28000653) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User':'?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'none',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cookie':thirdcookie
    }
    resp=requests.get(url=url,verify=False,headers=headers,timeout=(3,3),allow_redirects=False)
    if(resp.status_code==200):
        print("get打卡表单成功")
        #print(resp.text.count("label"))
        #hash1=hashlib.md5(resp.text.encode(encoding='UTF-8')).hexdigest()
        #print("表单哈希： "+hash1)
        if(148==resp.text.count("label")):
            print("******************\n*表单没有发生更改*\n******************")
        else:
            print("********************表单内容发生了更改！**********************")
        return 1
    else:
        return 0
def getjsticket(cookie):
    print("模拟向服务器获取查询腾讯地图的token")
    url="http://htu.banjimofang.com/weixin/jsticket?url=https://htu.banjimofang.com/student/course/31028/profiles/6099"
    headers={
    'GET':'/weixin/jsticket?url=https://htu.banjimofang.com/student/course/31028/profiles/6099 HTTP/1.1',
    'Host': 'htu.banjimofang.com',
    'Connection': 'close',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Linux; Android 10; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36 MMWEBID/5976 MicroMessenger/8.0.6.1900(0x28000653) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Referer':'https://htu.banjimofang.com/student/course/31028/profiles/6099',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cookie':cookie
    }
    resp=requests.get(url=url,verify=False,headers=headers,timeout=(3,3),allow_redirects=False)
    print(resp.status_code)
    if(resp.status_code==200):
        print("getjsticket成功")
        print(resp.text)
        return 1
    else:
        return 0

    
def post打卡数据(newcookie):
    url1="http://htu.banjimofang.com/student/course/31028/profiles/6099"
    x=random.randint(368,410) #随机后n位GPS制造飘逸假象
    y=random.randint(56,85)  #随机后n位GPS制造飘逸假象
    temperature=random.randint(1,9) #随机体温  36.1~36.8

    sleeptime=random.randint(1200,3600)  #随机时间   单位秒

    GPSlocate=["仰韶路渑池县第三小学东50米(仰韶路北)","仰韶路渑池县第三小学东北100米(仰韶路北)","仰韶路渑池县第三小学东100米(仰韶路北)"]
    locate=random.randint(0,len(GPSlocate)-1)
    print("休眠"+str(sleeptime/60)+"分钟")
    time.sleep(sleeptime)   #休眠  单位秒   GitHub最多支持运行6小时

    data1={
        'form_id':18461,
        'formdata[v]':'河南省,三门峡市,渑池县,'+GPSlocate[locate]+'|34.76'+str(x)+',111.749'+str(y),
        'formdata[q]':1,
        'formdata[z]':0,
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
        'Cookie':newcookie,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SPN-AL00 Build/HUAWEISPN-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045709 Mobile Safari/537.36 MMWEBID/7142 MicroMessenger/8.0.7.1920(0x28000737) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    }

    resp=requests.post(url=url1,verify=False,data=data1,headers=headers1).text
    print(resp)
    ex='<div class="desc">(.*?)</div>'
    result=re.findall(ex,resp,re.S)
    print(result)

getformwx(oldcookie)
time.sleep(1)
thirdcookie=get学生中心表单(oldcookie)
if(平台cookie==thirdcookie):
    print("平台cookie没有发生改变")
else:
    print("平台cookie发生了改变，请本次打卡后修改cookie为："+thirdcookie)
    f=open("fgfxf.cookie",mode='w')
    f.write(thirdcookie)
    f.close()
    time.sleep(3)
    print("新cookie已经写入文件")
 
thirdcookie+=';'
newcookie=G_cookies+thirdcookie
get打卡表单(newcookie)
time.sleep(3)
getjsticket(newcookie)
time.sleep(3)
post打卡数据(newcookie)

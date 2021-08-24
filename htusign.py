#!/usr/bin/python
#coding=utf-8
import requests


def GetFromWX(cookie):
    url="https://htu.banjimofang.com/student?from=wx"
    print("【info】模拟微信初次进入获取平台cookie")
    print(cookie)
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
    'Cookie':cookie
    }
    resp=requests.get(url=url,verify=False,headers=headers,timeout=(3,3),allow_redirects=False)
    return resp
  

def GetStudentCenter(cookie):
    url="https://htu.banjimofang.com/student/course/31028"
    print("【info】模拟从微信进入个人中心")
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
    'Cookie':cookie
    }
    resp=requests.get(url=url,verify=False,headers=headers,timeout=(3,3),allow_redirects=False)
    return resp
    
def GetTickIndex(cookie):
    url="https://htu.banjimofang.com/student/course/31028/profiles/6099"
    print("【info】模拟获取打卡界面")
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
    'Cookie':cookie
    }
    resp=requests.get(url=url,verify=False,headers=headers,timeout=(3,3),allow_redirects=False)
    return resp
  
def GetJSticket(cookie):
    print("【info】模拟向服务器获取查询腾讯地图的token")
    url="https://htu.banjimofang.com/weixin/jsticket?url=https://htu.banjimofang.com/student/course/31028/profiles/6099"
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
    return resp

    
    
def PostTickData(data,cookie):
    url1="https://htu.banjimofang.com/student/course/31028/profiles/6099"
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
        'Cookie':cookie,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SPN-AL00 Build/HUAWEISPN-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045709 Mobile Safari/537.36 MMWEBID/7142 MicroMessenger/8.0.7.1920(0x28000737) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    }

    resp=requests.post(url=url1,verify=False,data=data,headers=headers1).text
    return (resp)

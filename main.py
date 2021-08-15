import requests
import re
url1="https://htu.banjimofang.com/student/course/31028/profiles/6099"
data1={
    'form_id':18461,
    'formdata[v]':'河南省,三门峡市,渑池县,仰韶路|34.76399,111.74968',
    'formdata[w]':1,
    'formdata[b]':36,
    'formdata[g]':'',
    'formdata[r]':'',
    'formdata[s]':'',
    'formdata[t]':'',
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
    'Cookie':'remember_student_59ba36addc2b2f9401580f014c7f58ea4e30989d=970776%7CglFkBf2nDmDNiicluZpIsSUu6PL3Ipm8uABiXErJ075NyBViv7h6aLzI9zrn%7C; wxid=oIalJ5trVbPsjFZXf3Cm8IDpOnPU$1628859127$0509ee11712997a2c85e03a1afb78b30; yxktmf=mEAGyKlJjm9kLsU5b3x2u1rHBw8hoNOHlrYo4krR',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SPN-AL00 Build/HUAWEISPN-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045709 Mobile Safari/537.36 MMWEBID/7142 MicroMessenger/8.0.7.1920(0x28000737) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
}

resp=requests.post(url=url1,data=data1,headers=headers1).text
print(resp)
ex='<div class="desc">(.*?)</div>'
result=re.findall(ex,resp,re.S)
print(result)

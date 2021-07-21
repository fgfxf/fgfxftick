import requests
import re
url1="https://htu.banjimofang.com/student/course/31028/profiles/6099"
data1={
    'form_id':18461,
    'formdata[v]':'河南省,新乡市,牧野区,至学路|35.32993,113.91421',
    'formdata[b]':36,
    'formdata[g]':'',
    'formdata[r]':'',
    'formdata[s]':'',
    'formdata[t]':'',
    'formdata[u]':''
}
headers1={
    'Cookie':'yxktmf=8GsdwshpOQj9xAchY9rw3WDCXocFKDI9YmIoEo16; remember_student_59ba36addc2b2f9401580f014c7f58ea4e30989d=970776%7CglFkBf2nDmDNiicluZpIsSUu6PL3Ipm8uABiXErJ075NyBViv7h6aLzI9zrn',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SPN-AL00 Build/HUAWEISPN-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045709 Mobile Safari/537.36 MMWEBID/7142 MicroMessenger/8.0.7.1920(0x28000737) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
}

resp=requests.post(url=url1,data=data1,headers=headers1).text
ex='<div class="desc">(.*?)</div>'
result=re.findall(ex,resp,re.S)
print(result)

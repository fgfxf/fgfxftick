#!/usr/bin/python
#coding=utf-8
import random

#
#根据休眠时间随机选择定位
#
#返回  "地点|G经度,纬度"
#

def randomGPSlocate(sleeptime,LocateList,ans):
    GPSstr="";
    randay=random.randint(0,100)
    if(sleeptime<(50*60) or randay<60 ):
        #在家
        GPSstr=LocateList[0]
        x=random.randint(390,410) #随机后n位GPS制造飘逸假象
        y=random.randint(75,85)  #随机后n位GPS制造飘逸假象
        GPSstr+="|"
        GPSstr+=ans+str(x)+",111.749"+str(y)
    else:
        #在外面
        GPSstr=LocateList[random.randint(1,len(LocateList)-1)]
        x=random.randint(300,410) #随机后n位GPS制造飘逸假象
        y=random.randint(4870,5419)  #随机后n位GPS制造飘逸假象
        GPSstr+="|"
        GPSstr+=ans+str(x)+",111.7"+str(y)
    return GPSstr

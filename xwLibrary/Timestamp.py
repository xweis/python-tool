#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime, time

format_date = "%Y-%m-%d"
format_datetime = "%Y-%m-%d %H:%M:%S"
format_Y_M = "%Y-%m"

def getDate():
    #获取当前日期：2016-06-01 这样的日期字符串
    return time.strftime(format_date, time.localtime(time.time()))

def getDateTime():
    #获取当前日期：2013-06-01 11:22:11 这样的日期字符串
    return time.strftime(format_datetime, time.localtime(time.time()))

def getDate_Y_M():
    #获取当前日期：2013-06 这样的日期字符串
    return time.strftime(format_Y_M, time.localtime(time.time()))

def getDateHour():
    #获取当前时间的小时数，比如如果当前是下午16时，则返回16
    currentDateTime = getDateTime()
    return currentDateTime[-8:-6]

def getDateElements(sdate):
    #输入日期字符串，返回一个结构体组，包含了日期各个分量
    #输入：2013-09-10或者2013-09-10 22:11:22
    #返回：time.struct_time(tm_year=2013, tm_mon=4, tm_mday=1, tm_hour=21, tm_min=22, tm_sec=33, tm_wday=0, tm_yday=91, tm_isdst=-1)
    dformat = ""
    if judgeDateFormat(sdate) == 0:
        return None
    elif judgeDateFormat(sdate) == 1:
        dformat = format_date
    elif judgeDateFormat(sdate) == 2:
        dformat = format_datetime
    sdate = time.strptime(sdate, dformat)
    return sdate

def getDateToNumber(date1):
    #将日期字符串中的减号冒号去掉:
    #输入：2013-04-05，返回20130405
    #输入：2013-04-05 22:11:23，返回20130405221123
    return date1.replace("-","").replace(":","").replace("","")

def judgeDateFormat(datestr):
    #判断日期的格式，如果是"%Y-%m-%d"格式则返回1，如果是"%Y-%m-%d %H:%M:%S"则返回2，否则返回0
    #参数 datestr:日期字符串
    try:
        datetime.datetime.strptime(datestr, format_date)
        return 1
    except:
        pass
    try:
        datetime.datetime.strptime(datestr, format_datetime)
        return 2
    except:
        pass
    return 0

def timeTodatetime(value):
    #value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    # 经过localtime转换后变成
    # time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format_datetime, value)
    return dt

def dateTotimestamp(dt):
    #dt为字符串
    #中间过程，一般都需要将字符串转化为时间数组
    #将"2012-03-28 06:53:40"转化为时间戳
    s = time.mktime(getDateElements(dt))
    return int(s)

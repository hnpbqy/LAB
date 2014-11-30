#! /usr/bin/env python
#coding=utf-8
##############################################
#
# 201409  ABy:bluewing
#
# 批量抓取全球被黑网站统计信息，按照页码进行选择
#
# utf-8 默认保存的记事本是 utf-8 编码
#
# 注意,结尾有默认关机代码,当设置为主页全部抓取时
#
##############################################

import urllib2
import re
import time
import sys
import os


# Step1
#探测目标网站当前状态，引导你设置爬取参数
#Detecting target website's current state, then guide you to set up parameters needed

print
print u'全球被黑站点统计记录下载工具 V1.0 By:bluewing'.encode('gb2312')
print
popURL = "http://hack-cn.com/?page=1"
try:
    req = urllib2.Request(popURL)
    web = urllib2.urlopen(req,timeout=15)
    data = web.read()
    result = re.findall('pg.pageCount =(.*);',data)
    PageNum = int(result[0])

    result = re.findall('<span>(.*)</span>',data)
    AllNum = int(result[0])

    print u'查询结果总条目数：'.encode('gb2312') + str(AllNum) + ' ' + u'总页数：'.encode('gb2312') + str(PageNum)
    print

except Exception,e:
    print
    print e
    sys.exit()

print u'请输入起始页码：（默认从第1页开始）'.encode('gb2312')
try:
    beginNum = raw_input()
    if beginNum == '':
        beginNum = 1
    else:
        beginNum = int(beginNum)
        if beginNum < 1 or beginNum > PageNum:
            print "Input Num is valid!"
            sys.exit()

    print u'请输入结束页码：'.encode('gb2312')
    endNum = int(raw_input())
    if endNum < beginNum:
        print "Input Num is valid!"
        sys.exit()


except Exception,e:
    print
    print e
    sys.exit()
ShutdownMode = 'n'
print u'抓取完成后是否关机（y/n）?'.encode('gb2312')
ShutdownMode = raw_input()
if ShutdownMode.strip() == 'y' or ShutdownMode.strip() == 'Y':
    ShutdownMode = 'y'
    print u'计划完成后是否关机!!!'.encode('gb2312')


# Step2
# 根据你输入的爬取要求，对指定页面的内容进行爬取然后存储到txt中
#According to the requirements of your setting, get the specified page content and then stored in the TXT file

forUrl = "http://hack-cn.com/?page="

i = beginNum - 1
fileName = 'QuanQALL.txt'
fobk = open(fileName,'w')
beginTime = time.ctime()
while i < endNum:
    i = i + 1
    popURL = forUrl + str(i)
    popURL = popURL.strip()
    print 'PageNo:%d...' % i
    print popURL

    try:

        req = urllib2.Request(popURL)
        web = urllib2.urlopen(req,timeout=15)
        data = web.read()
        HCresult = re.findall('<tr class="xh">(\s*.*\s*.*\s*.*)</td>',data)
        if len(HCresult) > 0:

            for eachLine in HCresult:
                tempDate = eachLine[eachLine.find('>')+1:eachLine.find('>')+11]
                tempUper = eachLine[eachLine.find('var')+4:eachLine.find('"',eachLine.find('var'))]
                tempUrl = eachLine[eachLine.find('http://'):]

                aItem = tempUrl + '    ' + tempUper + '    ' + tempDate
                aItem = aItem.strip()
                print aItem
                fobk.write('%s%s' % (aItem,'\n'))
                fobk.flush()
        else:
            time.sleep(5) #sleep
            continue
    except Exception,e:
        print
        print e
        time.sleep(16)
        print
        continue
endTime = time.ctime()


# Step3
#结果整理与输出
#Show the results and output

print
print 'Task is completed:'
fobk.write('%s%s' % ('\n','\n'))
fileLine = 'AllNum:'+ str(AllNum) + ' ' + 'PageNum:' + str(PageNum)
print fileLine
fobk.write('%s%s' % (fileLine,'\n'))
fileLine = 'beginNum:'+ str(beginNum) + ' ' + 'endNum:' + str(endNum)
print fileLine
fobk.write('%s%s' % (fileLine,'\n'))
print beginTime
fobk.write('%s%s' % (beginTime,'\n'))
print endTime
fobk.write('%s%s' % (endTime,'\n'))
fobk.flush()
fobk.close()
if ShutdownMode == 'y':
    print 'Action:Shutdown after 16 seconds......'
    time.sleep(16)
    cmd = 'shutdown -s -f -t 0'
    os.system(cmd)
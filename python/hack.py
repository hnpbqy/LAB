#! /usr/bin/env python
#coding=utf-8
##############################################
#
# 201409  ABy:bluewing
#
# 批量抓取内容，比如抓取"edu.cn"的，按照页码进行选择
#
# 不输入关键字则按照首页全部抓取
#
#
#
##############################################
import urllib2
import re
import time
import sys

# Step1
#探测目标网站当前状态，引导你设置爬取参数
#Detecting target website's current state, then guide you to set up parameters needed

print
print u'中国被黑站点统计记录下载工具 V1.0 By:bluewing'.encode('gb2312')
print
print u'请输入查找关键字：(默认为首页依次抓取)'.encode('gb2312')
SearchKey = raw_input()
print

KeyMode = 1


popURL = "http://www.zone-h.com.cn/?key=" + SearchKey + "&mode=domain&Submit=+Search+"
if SearchKey is '':
    KeyMode = 0
    SearchKey = 'ALL'
    popURL = "http://www.zone-h.com.cn/"
try:
    req = urllib2.Request(popURL)
    web = urllib2.urlopen(req,timeout=15)
    data = web.read()
    result = re.findall('<form action="/Index.php" method="get">(.*)<a href=',data)
    reNum = '\d+'
    Num = re.findall(reNum,result[0])
    AllNum = int(Num[0])
    PageNum = int(Num[2])

    print u'查询结果总条目数：'.encode('gb2312') + str(AllNum) + ' ' + u'总页数：'.encode('gb2312') + str(PageNum)
    print

except Exception,e:
    print
    print e
    sys.exit()

if AllNum > 0 and PageNum == 1:
    HCresult = re.findall('<td align=center width=80 height=22>(.*\s*.*\s*.*)</td>',data)
    if len(HCresult) > 0:
        for eachLine in HCresult:
            tempDate = eachLine[:10]
            tempUper = eachLine[eachLine.find(' >')+2:eachLine.find('<',eachLine.find(' >'))]
            tempUrl = eachLine[eachLine.find('http://'):]

            aItem = tempUrl + '    ' + tempUper + '    ' + tempDate
            aItem = aItem.strip()
            print aItem
elif PageNum > 1:
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
else:
    sys.exit()

if KeyMode == 0:
    forUrl = "http://www.zone-h.com.cn/Index.php?mode=&type=&key=&page="
else:
    forUrl = "http://www.zone-h.com.cn/Index.php?mode=domain&type=&key="+ SearchKey + "&page="

# Step2
# 根据你输入的爬取要求，对指定页面的内容进行爬取然后存储到txt中
#According to the requirements of your setting, get the specified page content and then stored in the TXT file

i = beginNum - 1
fileName = SearchKey + '.txt'
fobk = open(fileName,'w')
beginTime = time.ctime()
while i < endNum:
    i = i + 1
    popURL = forUrl + str(i)
    popURL = popURL.strip()
    print 'PageNo:%d...' % i
    print

    try:

        req = urllib2.Request(popURL)
        web = urllib2.urlopen(req,timeout=15)
        data = web.read()
        HCresult = re.findall('<td align=center width=80 height=22>(.*\s*.*\s*.*)</td>',data)
        if len(HCresult) > 0:

            for eachLine in HCresult:
                tempDate = eachLine[:10]
                tempUper = eachLine[eachLine.find(' >')+2:eachLine.find('<',eachLine.find(' >'))]
                tempUrl = eachLine[eachLine.find('left>') + 5:]

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
        time.sleep(60)
        print
        continue
endTime = time.ctime()

# Step3
#结果整理与输出
#Show the results and output

print
print 'Task is completed:'
fobk.write('%s%s' % ('\n','\n'))
fileLine = 'SearchKey:'+ SearchKey
print fileLine
fobk.write('%s%s' % (fileLine,'\n'))
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

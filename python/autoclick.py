#! /usr/bin/env python
#coding=utf-8
import sys,os,shutil
import re,_winreg,glob
import cookielib
import urllib
import urllib2
from urllib2 import URLError, HTTPError
from PAM31 import PAMIE
from time import sleep
from random import randint

DEBUG = True

keyword=raw_input("请输入关键词")

#注:在使用IE7以上的浏览器须将是否关闭所有选项卡的勾点上 否则会造成程序死循环
#================清除COOKIE================否则百度不会计算访问,请在程序第67行修改自己电脑路劲
def CleanDir( Dir ):
    if os.path.isdir( Dir ):
        paths = os.listdir( Dir )
        for path in paths:
            filePath = os.path.join( Dir, path )
            if os.path.isfile( filePath ):
                try:
                    os.remove( filePath )
                except os.error:
                    print "OK"
            elif os.path.isdir( filePath ):
                if filePath[-4:].lower() == ".svn".lower():
                    continue
                shutil.rmtree(filePath,True)
    return True


# 更换代理IP。直接修改WINDOWS注册表
def alterip(ip=None):
    key=_winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",0,_winreg.KEY_ALL_ACCESS)
    value,type=_winreg.QueryValueEx(key,"ProxyServer")
    if ip!=None:
        _winreg.SetValueEx(key,'ProxyEnable',0,_winreg.REG_SZ,"1")
        if _winreg.SetValueEx(key,'ProxyServer',0,_winreg.REG_SZ,ip):
            print "Ip更换失败"
        else:
            print "更换成功"
            _winreg.CloseKey(key)
            return True

#==============IE点击模块#
def iepam(keyword=None):
    ie=PAMIE(timeOut=300)
    ie._ie.Navigate('http://www.baidu.com')
#==============关键词模块#
    if ie.setTextBox("wd", keyword)!=False:
        if ie.clickButton("su")!=None:
            sleep(3)
            if ie.getLink(unicode("灵动网络","cp936"))!=None:
                    ie.clickLink(ie.getLink(unicode("灵动网络","cp936")))
                #else:
            #ie.clickLink(ie.getLink(unicode("[%s]"%i,"cp936")))
            #ie.clickLink(ie.getLink(unicode("[%s]"%p,"cp936")))
            #ie.clickLink(ie.getLink(unicode("灵动网络 - 服务器租用托管,VPS,虚拟主机,域名注册,企业邮局,网络...","cp936")))
            #        i+=1
#=============随机停留时间=======
        sleep(randint(5,20))
#=============正确填写自己电脑的COOKIE路劲#
        CleanDir("C:\Users\liyun\AppData\Roaming\Microsoft\Windows\Cookies")
    os.system('taskkill /IM iexplore.exe')

#html页面下载函数
def getHtml(url,post_data=None,cookie=None):
        """Fetch the target html
        url - URL to fetch
        post_data - POST Entity
        cookie - Cookie Header
        """
        if DEBUG:
            print "getHtml: ",url

        result =''

        try:
            #create a request
            request = urllib2.Request(url)
            cj = cookielib.CookieJar()

            #change User-Agent
            request.add_header("accept","*/*")
            request.add_header('User-Agent','Mozilla/5.0')

            #change Referrer
            request.add_header('referer','http://www.51proxied.com/index.html')

            #if has cookie,add cookie header
            if cookie:
               request.add_header('Cookie',cookie)

            #create a opener
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            #if has post entity
            if post_data:

                #encode post data
                post_data = urllib.urlencode(post_data)
                response = opener.open(request,post_data)
            else:
                response = opener.open(request)

            result = response.read()

            response.close()

            #no content,don't save
            if not result or len(result)==0:
                return ''

            return  result
        except HTTPError, e:
            if DEBUG:
                print 'Error retrieving data:',e
                print 'Server error document follows:\n'
                #print e.read()
            return ''
        except URLError, e:
            if hasattr(e, 'reason'):
                if DEBUG:
                    print 'Failed to reach a server.'
                    print 'Reason: ', e.reason
                return ''
            elif hasattr(e, 'code'):
                if DEBUG:
                    print 'The server couldn\'t fulfill the request.'
                    print 'Error code: ', e.code
                return ''
        except Exception, e:
            if DEBUG:
                print e
            return ''


#需要验证的代理列表
proxy_urls = []
proxy_urls.append({'url':'http://www.51proxied.com/http_anonymous.html','type':'http_anonymous'})
#proxy_urls.append({'url':'http://www.51proxied.com/http_non_anonymous.html','type':'http_transparent'})


import re
import socket
import time
import threading

result =[]


#线程同步锁
lock = threading.Lock()

def synchronous(f):
    def call(*args, **kwargs):
        lock.acquire()
        try:
            return f(*args, **kwargs)
        finally:
            lock.release()
    return call



#先获取所有待验证的代理
proxies = []

for proxy_url in proxy_urls:
    html = getHtml(proxy_url['url'])


    #正则匹配获取每一代理
    rs = re.compile(r'''<tr .*?>[\s\S]*?<td .*?>\d+?</td>[\s\S]*?<td>(\S+?)</td>[\s\S]*?<td .*?>(\S+?)</td>[\s\S]*?<td .*?>(\S+?)</td>[\s\S]*?</tr>''',re.DOTALL).findall(html)

    for r in rs:
        proxy = {}

        #代理域名
        proxy['domain'] = r[0]
        #代理端口
        proxy['port'] = r[1]
        #代理国家
        proxy['state'] = r[2]
        #代理类型
        proxy['type'] = proxy_url['type']
        #响应时间
        proxy['time'] = 0

        if not (proxy in proxies):
            proxies.append(proxy)



#获取一个待验证代理
@synchronous
def getproxy():
    global proxies
    if len(proxies)>0:
        return proxies.pop()
    else:
        return ''



#保存验证结果
@synchronous
def saveresult(proxy):
    global result

    if not(proxy in result):
        result.append(proxy)


#线程函数
def verify():

    while 1:
        proxy = getproxy()
        #所有代理均已验证完毕
        if len(proxy)==0:
            return

        print "正在验证：%s,%s" % (proxy['domain'],proxy['port'])

        #验证代理的可用性
        #创建一个TCP连接套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #设置10超时
        sock.settimeout(10)
        try:
            start = time.clock()

            #连接代理服务器
            sock.connect((proxy['domain'], int(proxy['port'])))
            proxy['time'] = int((time.clock() - start) * 1000)
            sock.close()

            saveresult(proxy)
            print "%s,%s 验证通过，响应时间：%d ms." % (proxy['domain'],proxy['port'],proxy['time'])
        except Exception, e:
            if DEBUG:
                print e

            print "%s,%s 验证失败." % (proxy['domain'],proxy['port'])




#init thread_pool
thread_pool = []

for i in range(20):
    th = threading.Thread(target=verify,args=()) ;
    thread_pool.append(th)

# start threads one by one
for thread in thread_pool:
    thread.start()

#collect all threads
for thread in thread_pool:
    threading.Thread.join(thread)


#结果按响应时间从小到大排序

result.sort(lambda x,y: cmp(x['time'], y['time']))

for item in result:
    if item['time'] < 60:
            ip = '%s:%s' % (item['domain'],item['port'])
            print ip
            if alterip(ip):
                iepam(keyword)



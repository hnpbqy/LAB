from sys import exit
from httplib2 import Http
from urllib import urlencode
import re
 
http=Http()
def login(username,password):
    url="https://passport.csdn.net"
    response,content=http.request(url)
    matches=re.search('name="lt"\s+value="([\-\w]+)"',content)
    lt=matches.group(1) if matches else ""
    matches=re.search('name="execution"\s+value="([\-\w]+)"',content)
    execution=matches.group(1) if matches else ""
    matches=re.search('jsessionid=([\w=\.]+)',content)
    url="https://passport.csdn.net/account/login;"
    url+=matches.group(0) if matches else ""
     
    body={'username':username,'password':password,'lt':lt,'execution':execution,'_eventId':'submit'}
    header={'Content-Type':'application/x-www-form-urlencoded'}
    response,content=http.request(url,'POST',headers=header,body=urlencode(body))
     
    if response.status!=200:
        return False
    else:
        return response['set-cookie']
 
def list_category(cookie):
    url="http://download.csdn.net/category"
    header={'Cookie':cookie}
    response,content=http.request(url,'GET',headers=header)
     
    categories=[]
    for matches in re.finditer(u'<a\s+href="/c-(\d{3,})">([\w\u4e00-\u9fa5]+)</a>',content.decode('utf8')):
        suburl='/c-'+matches.group(1)
        url="http://download.csdn.net"+suburl
        response,content=http.request(url,'GET',headers=header)
        maxPage=0
        for matches1 in re.finditer('<a\s+class="pageliststy"\s+href="'+suburl+'/(\d+)"',content):
            tmp=int(matches1.group(1))
            maxPage=tmp if tmp>=maxPage else maxPage
        tmp={'url':url,'title':matches.group(2),'maxpage':maxPage}
        categories.append(tmp)
    return categories
def get_resources(categories,cookie):
    header={'Cookie':cookie}
     
    resources=[]
    for category in categories:
        page=0
        while page<=category['maxpage']:
            page=page+1
            suburl=str(page) if page!=1 else ""
            url=category['url']+"/hot/"+suburl
            response,content=http.request(url,'GET',headers=header)
             
            for matches in re.finditer(u'<a\s+href="([/\w]+)">(.+)</a><span class="marks">(\d+)</span>',content):
                url="http://download.csdn.net/download"+matches.group(1)
                url=url.replace("/detail","")
                response,content=http.request(url,'GET',headers=header)
 
                #get url
                matches=re.search('form\s+name="download_form"\s+id="download_form"\s+method="post"\s+action="([\w/:\.]+)"',content)
                url=matches.group(1) if matches else ""
 
                #get post data
                data={}
                for mat in re.finditer('<input\s+type="hidden"\s+name="basic\[(\w+)\]"',content):
                    data['basic['+mat.group(1)+']']=""
                data['ds']='ds'
                data['validate_code']=''
                 
                tmp={'url':url,'data':data,'title':category['title']}
                resources.append(tmp)
                break
            break
        break
    return resources
def download(resources,cookie):
    header={'Content-Type':'application/x-www-form-urlencoded','Cookie':cookie}
    for resource in resources:
        response,content=http.request(resource['url'],'POST',headers=header)    
        print content
        print response
if __name__=='__main__':
    cookie=login('2673192624@qq.com','msp62524131')
    if not cookie:
        exit()
    categories=list_category(cookie)
    if len(categories)==0:
        exit()
    resources=get_resources(categories,cookie)
    if len(resources)==0:
        exit()
    download(resources,cookie)

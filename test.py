import requests
import json
from bs4 import BeautifulSoup
import urllib


#headers = {'content-type': 'application/json',"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
#params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}

url="http://www.museumsusa.org/museums/?k=1271393%2cAlpha%3aA%3bDirectoryID%3a200454";
headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/60.0.3112.101 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"}


'''headers={
#'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6',
#'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'1366',
'Content-Type':'application/x-www-form-urlencoded',
#'Cookie':'NEX=4287158; ASP.NET_SessionId=ezkdffdedh0mzfqfruo1vota; LocalityFilterParams=zip=32608&state=FL&city=Gainesville&groupBy=Museum&timeFrame=Next30Days; __utmt=1; __utma=194431921.29984883.1502848800.1503124303.1503144432.5; __utmb=194431921.72.10.1503144432; __utmc=194431921; __utmz=194431921.1502848800.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
#'Host':'www.museumsusa.org',
#'Origin':'http://www.museumsusa.org',
#'Referer':'http://www.museumsusa.org/museums/?k=1271393%2cAlpha%3aA%3bDirectoryID%3a200454',
#'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}'''
session = requests.Session()
session.headers.update(headers)
r=session.get(url)
soup=BeautifulSoup(r.content)
#?k=1271393%2cAlpha%3aA%3bDirectoryID%3a200454
VIEWSTATE=soup.find(id="__VIEWSTATE")['value']
#VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR")['value']
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION")['value']


data_in={
'__EVENTTARGET':"ctl08$ctl00$BottomPager$Page2",
'__EVENTARGUMENT':"",
'__VIEWSTATE':VIEWSTATE,
'__EVENTVALIDATION':EVENTVALIDATION,
'ctl04$phrase':"",
'ctl04$directoryList':"/museums/|/museums/search/"
#"k":"1271393,Alpha:A;DirectoryID:200454"
      }


r2 = session.post(url, data=json.dumps(data_in))

print (r2)




if alpha=='A':
    pages=889
elif alpha=='B':
    pages=112


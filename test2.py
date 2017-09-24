import requests
import json
from bs4 import BeautifulSoup

url = "http://www.museumsusa.org/museums/?k=1271393%2cAlpha%3aA%3bDirectoryID%3a200454"
headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko)"
}
session = requests.Session()
session.headers.update(headers)
r=session.get(url)
pages = 10

for _ in range(pages):
    soup=BeautifulSoup(r.content, 'html.parser')
    VIEWSTATE=soup.find(id="__VIEWSTATE")['value']
    EVENTVALIDATION=soup.find(id="__EVENTVALIDATION")['value']
    data_in={
        '__EVENTTARGET':'ctl08$ctl00$BottomPager$Next',
        '__EVENTARGUMENT':"",
        '__VIEWSTATE':VIEWSTATE,
        '__EVENTVALIDATION':EVENTVALIDATION,
        'ctl04$phrase':"",
        'ctl04$directoryList':"/museums/|/museums/search/"
    }
    r = session.post(url, data=data_in)
    print (r)
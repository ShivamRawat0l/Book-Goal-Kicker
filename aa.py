import requests
from bs4 import BeautifulSoup
a=input().replace(" ","-")
r=requests.get("https://timesofindia.indiatimes.com/topic/"+a+"/news")
soup = BeautifulSoup(r.content,'html.parser')
tab= soup.find(class_="tab_content")
for i in tab.find_all('li',class_="article"):
    k=i.find(class_="title")
    print(k.text)

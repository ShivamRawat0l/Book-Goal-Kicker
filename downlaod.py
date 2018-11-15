import requests
from bs4 import BeautifulSoup
import wget
r=requests.get('https://books.goalkicker.com/')
soup=BeautifulSoup(r.content,'html.parser')
soup.prettify()
allbooks=soup.find_all('div',{'class':"bookContainer grow"})
for i in allbooks:
    booklink='https://books.goalkicker.com/'+i.a['href']
    target=requests.get(booklink)
    targetsoup=BeautifulSoup(target.content,'html.parser')
    downlink=targetsoup.find('button',{'class':'download'})['onclick'][15:-1]
    wget.download(booklink+'/'+downlink)
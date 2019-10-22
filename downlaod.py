import os
import requests
from bs4 import BeautifulSoup

def download_pdf(response_object, name):
    with open(name, 'wb') as f:
        f.write(response_object.content)
    print('\u001b[32mDone!\u001b[0m')



r=requests.get('https://books.goalkicker.com/')
soup=BeautifulSoup(r.content,'html.parser')
soup.prettify()
allbooks=soup.find_all('div',{'class':"bookContainer grow"})

for i in allbooks:
    booklink='https://books.goalkicker.com/'+i.a['href']
    target=requests.get(booklink)
    targetsoup=BeautifulSoup(target.content,'html.parser')
    downlink=targetsoup.find('button',{'class':'download'})['onclick'][15:-1]
    print(f'Downloading \u001b[34m{downlink}\u001b[0m...')
    res = requests.get(os.path.join(booklink, downlink))
    download_pdf(res, downlink)

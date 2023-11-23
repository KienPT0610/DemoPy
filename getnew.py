import requests
from bs4 import BeautifulSoup

r = requests.get('https://baomoi.com/tag/LITE.epi')
soup = BeautifulSoup(r.text, 'html.parser')
mydiv = soup.find_all('h3', {'class':'bm_F'})
for new in mydiv:
    print(new.a.get('title')) 
    print(new.a.get('href'))

import requests
from bs4 import BeautifulSoup
import pyperclip


LINK = 'https://www.facebook.com/people/Nafisa-Khan/100051429259431'
r = requests.get(LINK)
html = r.text

soup = BeautifulSoup(html, "html.parser")

meta = soup.find('meta', {'property': 'og:image'})
print(meta['content'])

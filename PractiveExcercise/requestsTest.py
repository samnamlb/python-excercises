from bs4 import BeautifulSoup
import requests
url = 'https://www.wcpss.net/middlecreekhs'
r = requests.get(url)
r_html = r.text
print(r_html)


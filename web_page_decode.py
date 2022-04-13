import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")

titles_list = []

for content in soup.find_all('h3'):
    titles_list.append(content.get_text())

print(titles_list)

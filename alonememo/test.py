from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=24452'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# -------------메타태그를 크롤링하는법. (메타태그는 <head>에 있음)---------------
title = soup.select_one('meta[property="og:title"]')['content']
url = soup.select_one('meta[property="og:url"]')['content']
desc = soup.select_one('meta[property="og:description"]')['content']
image = soup.select_one('meta[property="og:image"]')['content']

print(title, url, desc, image)

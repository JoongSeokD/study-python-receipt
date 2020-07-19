from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
soup = bs(html.text, 'html.parser')
html.close()

data1_list = soup.findAll('div', {'class':'col_inner'})
#pprint(data1)

# 전체 웹툰 리스트
week_title_list = []

for data1 in data1_list:
    data2 = data1.findAll('a', {'class':'title'})
    # pprint(data2)

    title_list = [t.text for t in data2]
    #pprint(title_list)
    week_title_list.append(title_list)


print(week_title_list[0])
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
soup = bs(html.text,'html.parser')
html.close()

data_list = soup.findAll('div',{'class':'col_inner'})
#pprint(len(data1))

week_title_list = []

for data1 in data_list:
    data2 = data1.findAll('a',{'class':'title'})

    title_list = [t.text for t in data2]
    #pprint(title_list)
    week_title_list.extend(title_list)

pprint(week_title_list[0])


#coding=utf-8
#version 1.0 国内机票查询
from bs4 import BeautifulSoup
import requests
import re
from mongodata import connect
import threading
tpool=[]
def get_china_page(page):
    rq = requests.get('http://airport.anseo.cn/c-china__page- %s' %(str(page)))
    rq.encoding = 'utf-8'
    soup = BeautifulSoup(rq.text, 'lxml')
    soup.prettify()
    trs = soup.tbody.find_all('tr')
    pattern = re.compile('^<td>.*?>(.*?)<br/>', re.S)
    for tr in trs:
        tds = tr.find_all('td')
        text = trs[0].find_all('td')[0]
        result = re.findall(pattern, str(text))
        city_name = result[0].strip()
        city_en = tds[0].a['title']
        IATA_CODE = tds[2].span.text
        if IATA_CODE:
            data = {
                '城市拼音':city_en,
                '城市名':city_name,
                '三位码':IATA_CODE
            }
            conn = connect('localhost', 27017, 'airline', 'airlines')
            collection = conn.connet_to_Database()
            conn.Write_Data(data,collection)
for i in range(10):
    tpool.append(threading.Thread(target=get_china_page,args=(i,)))
for i in tpool:
    i.start()
for i in tpool:
    i.join()


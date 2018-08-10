#coding=utf-8
#version 1.0 国内机票查询
import queue
from bs4 import BeautifulSoup
import requests
import re
from mongodata import Connect
import threading
tpool=[]
#获取中国所有机场三位码
def get_china_page(page):
    rq = requests.get('http://airport.anseo.cn/c-china__page- %s' %(str(page)))
    rq.encoding = 'utf-8'
    soup = BeautifulSoup(rq.text, 'lxml')
    soup.prettify()
    trs = soup.tbody.find_all('tr')
    pattern = re.compile('^<td>.*?>(.*?)<br/>', re.S)
    for tr in trs:
        #每个tr下四个td
        tds = tr.find_all('td')
        #通过正则找中文城市名字
        result = re.findall(pattern, str(tds[0]))
        city_zh = result[0].strip()
        #找拼音和三位码
        city_en = tds[0].a['title']
        IATA_CODE = tds[2].span.text
        if IATA_CODE and city_en and city_zh:
            data = {
                'city_en':city_en,
                'city_zh':city_zh,
                'IATA_CODE':IATA_CODE
            }
            #连接数据库写入数据
            conn = Connect('localhost', 27017, 'airline', 'airlines')
            collection = conn.connet_to_Database()
            conn.Write_Data(data,collection)
#创建多个线程加入列表 逐个开启并等待其他线程结束
page = 5
if __name__ == '__main__':
    for i in range(page + 1):
        t = threading.Thread(target=get_china_page, args=(i,))
        tpool.append(t)
    for i in tpool:
        i.start()
    for i in tpool:
        i.join()






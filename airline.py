import requests
from urllib.parse import urlencode
from mongodata import Connect
class Airline():
    def __init__(self,fcity,tcity,fdate,tdate):
        self.fcity = tcity
        self.tcity = fcity
        self.fdate = fdate
        self.tdate = tdate
    def oneway(self):
        base_url = 'https://flight.qunar.com/twell/flight/Search.jsp?'
        params = {'from':'flight_dom_search','searchType':'OnewayFlight',
        'fromCity':self.fcity,'toCity':self.tcity,'fromDate':self.fdate,'toDate':self.tdate,'ishttps':1}
        url = base_url + urlencode(params)
        rq = requests.get(url)
        print(rq)
conn = Connect('localhost',27017,'airline','airlines')
collection = conn.connet_to_Database()
conn.Read_Data(collection,{'city_zh':'北京'})
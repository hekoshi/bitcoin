'''
Created on 2013-9-7

@author: Simon
'''
import json
from api.models import Ticker

def init_ticker_table():
    with open('markets.json') as data_file:    
        data = json.load(data_file)
    print data
    for d in data:
        market = Ticker()
        market.name = d['market']
        market.ticker = d['ticker']
        market.depth = d['depth']
        market.trade = d['trade']
        market.save()
    
def get_markets():
    return Ticker.objects.order_by('name')
        
if __name__ == "__main__":     
    #init_ticker_table()
    print get_markets()
    from urlparse import urlparse, parse_qsl
    o = urlparse('https://796.com/apiV2/depth/100.html?op=futures')
    query_dict = dict(parse_qsl(o.query))
    #d = dict(o.query)
    print query_dict
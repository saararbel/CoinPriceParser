import requests
import time
import datetime
import json

class AllTickerPrice:
    def __init__(self, eth_dict, btc_dict, timestamp):
        self.eth_dict = eth_dict
        self.btc_dict = btc_dict
        self.timestamp = timestamp


def retrieveEthAndBtcCoins(json):
    eth_dict = {}
    btc_dict = {}
    for e in json:
        if e["symbol"].endswith("ETH"):
            eth_dict[e["symbol"][:-3]] = e["price"]
        if e["symbol"].endswith("BTC"):
            btc_dict[e["symbol"][:-3]] = e["price"]

    return AllTickerPrice(eth_dict, btc_dict, time.time())


START_QUERY = 'https://www.binance.com/api/v1/ticker/allPrices'
FROM_COIN = 'ETH'
TO_COINS = 'BTC,USD,EUR'
TIME_STAMP = int(time.time()) #'1452680400'
s = "01/12/2017"
s2 = "02/12/2017"
# TIME_STAMP = time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())
finish = time.mktime(datetime.datetime.strptime(s2, "%d/%m/%Y").timetuple())

lst = []

for i in range(10):
    r = requests.get('%s' % (START_QUERY))
    responedContent = r.content.decode('UTF-8')
    parsedJson = json.loads(responedContent)
    lst.append(retrieveEthAndBtcCoins(parsedJson))
    time.sleep(1)
    print("hey")




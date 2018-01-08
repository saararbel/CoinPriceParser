import requests
import json
import time
from KnownSymbols import *
from AllTickerPrice import AllTickerPrice
from BinanceQuerys import *

SYMBOL = "symbol"
PRICE = "price"

def buildAllTickerPriceFromJson(json):
    eth_conversion = {}
    btc_conversion = {}
    usdt_conversion = {}
    for e in json:
        if e[SYMBOL].endswith(ETH):
            eth_conversion[e[SYMBOL][:-3]] = float(e[PRICE])
        if e[SYMBOL].endswith(BTC):
            btc_conversion[e[SYMBOL][:-3]] = float(e[PRICE])
        if e[SYMBOL].endswith(USDT):
            usdt_conversion[e[SYMBOL][:-4]] = float(e[PRICE])

    return AllTickerPrice(eth_conversion, btc_conversion, usdt_conversion, time.time())


def main():
    coinPriceSnapshots = []

    for i in range(10):
        req = requests.get('%s' % (GET_ALL_COIN_PRICES_QUERY))
        responedJson = json.loads(req.content.decode('UTF-8'))
        coinPriceSnapshots.append(buildAllTickerPriceFromJson(responedJson))
        time.sleep(5)
        print('%s: %s USD' % (coinPriceSnapshots[i].getDateFromTimestamp(),coinPriceSnapshots[i].getCoinPriceInUsd("TRX")))


if __name__ == "__main__":
    main()





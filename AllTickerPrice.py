from KnownSymbols import *
import datetime

class AllTickerPrice:
    def __init__(self, eth_conversion, btc_conversion, usdt_conversion, timestamp):
        self.eth_conversion = eth_conversion
        self.btc_conversion = btc_conversion
        self.usdt_conversion = usdt_conversion
        self.timestamp = timestamp

    def getCoinPriceInUsd(self, coinSymobl):
        if coinSymobl == ETH:
            return self.usdt_conversion[ETH]
        if coinSymobl == BTC:
            return self.usdt_conversion[BTC]

        return ((self.eth_conversion[coinSymobl] * self.usdt_conversion[ETH]) + (
                self.btc_conversion[coinSymobl] * self.usdt_conversion[BTC])) / 2

    def getTimeStamp(self):
        return self.timestamp

    def getDateFromTimestamp(self):
        return datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')
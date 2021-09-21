import krakenex
import json
import time
import datetime
import calendar

/* Returns an array of price data */
def get_crypto_data(pair, since):
    return api.query_public('OHLC', data = {'pair' :pair, 'since' : since})['result']['pair']

/* Returns balance of account */
def get_balance():
    return api.query_private('Balance')['result']


def get_trades_history():
    start_Date = datetime.datetime(2021, 7, 4)
    end_date = datetime.datetune.today()
    return api.query_private('TradesHistory', req(start_date, end_date, 1))['result']['trades']

def date_nix(str_date):
    return calender.timegm(str_date.timetuple())

def req(start, end, ofs):
    req_date = {
        'type' : 'all',
        'trades' : 'true',
        'start' : str(date_nix(start)),
        'end' : str(date_nix(end)),
        'ofs' : str(ofs)
    }
    return req_date

if __name__ == '__main__':
    api = krakenex.API() //Establish API
    api.load_key('kraken.key') //Using they API key to obtain access
    pair = "XETHZUSD" //https://api.kraken.com/0/public/AssetPairs
    since = str(int(time.time() - 3600))

    print(json.dumps(get_crypto_data(pair, since), indent = 4))



import requests
import csv
from datetime import datetime
import time


_tickers = [
    'BTC', 'USDT', 'XRP', 'SOL', 'AVAX', 'DOT', 'MATIC', 'DAI', 'ATOM', 'UNI', 'BCH', 'MANA', 'SAND', 'AXS', 'FIL', 'EOS', 'AAVE', 'MKR', 'ENJ', 'CRV', 'LRC', 'DASH', 'MINA',
    'COMP', '1INCH', 'BNT', 'ANKR', 'SNX', 'SUSHI', 'ZRX', 'DYDX', 'STORJ', 'KEEP', 'KNC', 'OCEAN', 'RAY', 'INJ', 'ANT', 'OXT', 'MNGO', 'AKT', 'REPV2', 'OGN', 'GHST', 'FIDA',
    'BAL', 'ATLAS', 'KILT', 'PHA', 'POLIS', 'SDN', 'TBTC', 'OXY', 'BNC', 'KINT', 'AIR', 'ETH', 'USDC', 'ADA', 'LUNA', 'DOGE', 'SHIB', 'WBTC', 'LTC', 'LINK', 'TRX', 'ALGO',
    'XLM', 'ETC', 'XTZ', 'XMR', 'FLOW', 'GRT', 'ZEC', 'KSM', 'CHZ', 'BAT', 'WAVES', 'YFI', 'QTUM', 'GNO', 'OMG', 'LPT', 'ICX', 'SC', 'KAVA', 'PERP', 'GLMR', 'PAXG', 'REN',
    'SRM', 'MOVR', 'CTSI', 'LSK', 'ASTR', 'EWT', 'BAND', 'REP', 'BADGER', 'ACA', 'MLN', 'CQT', 'MIR', 'KIN', 'RARI', 'ORCA', 'KAR', 'SBR', 'STEP', 'NANO'
    ]

_headers = [
    'Date', 'Time', 'BTC', 'ETH', 'ADA', 'DOGE', 'XRP', 'DOT', 'LTC', 'BCH', 'LINK', 'XLM', 'FIL', 'TRX', 'ETC', 'XMR', 'AAVE', 'ATOM', 'XTZ', 'ALGO', 'DASH', 'WAVES', 'KSM', 'ZEC', 'SNX', 'YFI', 'GRT', 'BAT', 'SC', 'QTUM',
    'ICX', 'OMG', 'NANO', 'FLOW', 'CRV', 'LSK', 'KNC', 'OCEAN', 'STORJ', 'BAL', 'REP', 'EWT', 'REPV2', 'GNO', 'ANT', 'KAVA', 'KEEP', 'OXT', 'MLN', 'PAXG', 'TBTC', 'UNI', 'MATIC', 'EOS', 'DAI', 'MKR', 'COMP', 'SUSHI', 'MANA',
    'ENJ', 'BNT', 'ANKR', 'REN', 'LPT', 'MINA', 'SAND', 'RARI', 'GHST', 'USDT', 'SOL', 'AVAX', 'AXS', 'LRC', '1INCH', 'ZRX', 'DYDX', 'RAY', 'INJ', 'MNGO', 'AKT', 'OGN', 'FIDA', 'ATLAS', 'KILT', 'PHA', 'POLIS', 'SDN', 'OXY',
    'BNC', 'KINT', 'AIR', 'USDC', 'LUNA', 'SHIB', 'WBTC', 'CHZ', 'PERP', 'GLMR', 'SRM', 'MOVR', 'CTSI', 'ASTR', 'BAND', 'BADGER', 'ACA', 'CQT', 'MIR', 'KIN', 'ORCA', 'KAR', 'SBR', 'STEP']

url = "https://api.kraken.com/0/public/Ticker?pair=USD"

_tickerdict = {
    'BTC': 'XXBTZUSD', 'USDT': 'USDTZUSD', 'XRP': 'XXRPZUSD', 'SOL': 'SOLUSD', 'AVAX': 'AVAXUSD', 'DOT': 'DOTUSD', 'MATIC': 'MATICUSD', 'DAI': 'DAIUSD', 'ATOM': 'ATOMUSD',
    'UNI': 'UNIUSD', 'BCH': 'BCHUSD', 'MANA': 'MANAUSD', 'SAND': 'SANDUSD', 'AXS': 'AXSUSD', 'FIL': 'FILUSD', 'EOS': 'EOSUSD', 'AAVE': 'AAVEUSD', 'MKR': 'MKRUSD',
    'ENJ': 'ENJUSD', 'CRV': 'CRVUSD', 'LRC': 'LRCUSD', 'DASH': 'DASHUSD', 'MINA': 'MINAUSD', 'COMP': 'COMPUSD', '1INCH': '1INCHUSD', 'BNT': 'BNTUSD', 'ANKR': 'ANKRUSD',
    'SNX': 'SNXUSD', 'SUSHI': 'SUSHIUSD', 'ZRX': 'ZRXUSD', 'DYDX': 'DYDXUSD', 'STORJ': 'STORJUSD', 'KEEP': 'KEEPUSD', 'KNC': 'KNCUSD', 'OCEAN': 'OCEANUSD', 'RAY': 'RAYUSD',
    'INJ': 'INJUSD', 'ANT': 'ANTUSD', 'OXT': 'OXTUSD', 'MNGO': 'MNGOUSD', 'AKT': 'AKTUSD', 'REPV2': 'REPV2USD', 'OGN': 'OGNUSD', 'GHST': 'GHSTUSD', 'FIDA': 'FIDAUSD',
    'BAL': 'BALUSD', 'ATLAS': 'ATLASUSD', 'KILT': 'KILTUSD', 'PHA': 'PHAUSD', 'POLIS': 'POLISUSD', 'SDN': 'SDNUSD', 'TBTC': 'TBTCUSD', 'OXY': 'OXYUSD', 'BNC': 'BNCUSD',
    'KINT': 'KINTUSD', 'AIR': 'AIRUSD', 'ETH': 'XETHZUSD', 'USDC': 'USDCUSD', 'ADA': 'ADAUSD', 'LUNA': 'LUNAUSD', 'DOGE': 'XDGUSD', 'SHIB': 'SHIBUSD', 'WBTC': 'WBTCUSD',
    'LTC': 'XLTCZUSD', 'LINK': 'LINKUSD', 'TRX': 'TRXUSD', 'ALGO': 'ALGOUSD', 'XLM': 'XXLMZUSD', 'ETC': 'XETCZUSD', 'XTZ': 'XTZUSD', 'XMR': 'XXMRZUSD', 'FLOW': 'FLOWUSD',
    'GRT': 'GRTUSD', 'ZEC': 'XZECZUSD', 'KSM': 'KSMUSD', 'CHZ': 'CHZUSD', 'BAT': 'BATUSD', 'WAVES': 'WAVESUSD', 'YFI': 'YFIUSD', 'QTUM': 'QTUMUSD', 'GNO': 'GNOUSD',
    'OMG': 'OMGUSD', 'LPT': 'LPTUSD', 'ICX': 'ICXUSD', 'SC': 'SCUSD', 'KAVA': 'KAVAUSD', 'PERP': 'PERPUSD', 'GLMR': 'GLMRUSD', 'PAXG': 'PAXGUSD', 'REN': 'RENUSD',
    'SRM': 'SRMUSD', 'MOVR': 'MOVRUSD', 'CTSI': 'CTSIUSD', 'LSK': 'LSKUSD', 'ASTR': 'ASTRUSD', 'EWT': 'EWTUSD', 'BAND': 'BANDUSD', 'REP': 'XREPZUSD', 'BADGER': 'BADGERUSD',
    'ACA': 'ACAUSD', 'MLN': 'XMLNZUSD', 'CQT': 'CQTUSD', 'MIR': 'MIRUSD', 'KIN': 'KINUSD', 'RARI': 'RARIUSD', 'ORCA': 'ORCAUSD', 'KAR': 'KARUSD', 'SBR': 'SBRUSD',
    'STEP': 'STEPUSD', 'NANO': 'NANOUSD', "XXBT": "XXBTZUSD", "XETH": "XETHZUSD", 'XXRP': 'XXRPZUSD', "XXMR": "XXMRZUSD", "XXLM": "XXLMZUSD", "XZEC": "XZECZUSD",
    "XREP": "XREPZUSD", "XMLN": "XMLNZUSD"
    }

_Differencetolast = {
    'BTC': None, 'USDT': None, 'XRP': None, 'SOL': None, 'AVAX': None, 'DOT': None, 'MATIC': None, 'DAI': None, 'ATOM': None, 'UNI': None, 'BCH': None, 'MANA': None, 'SAND': None, 'AXS': None, 'FIL': None, 'EOS': None,
    'AAVE': None, 'MKR': None, 'ENJ': None, 'CRV': None, 'LRC': None, 'DASH': None, 'MINA': None, 'COMP': None, '1INCH': None, 'BNT': None, 'ANKR': None, 'SNX': None, 'SUSHI': None, 'ZRX': None, 'DYDX': None, 'STORJ': None,
    'KEEP': None, 'KNC': None, 'OCEAN': None, 'RAY': None, 'INJ': None, 'ANT': None, 'OXT': None, 'MNGO': None, 'AKT': None, 'REPV2': None, 'OGN': None, 'GHST': None, 'FIDA': None, 'BAL': None, 'ATLAS': None, 'KILT': None,
    'PHA': None, 'POLIS': None, 'SDN': None, 'TBTC': None, 'OXY': None, 'BNC': None, 'KINT': None, 'AIR': None, 'ETH': None, 'USDC': None, 'ADA': None, 'LUNA': None, 'DOGE': None, 'SHIB': None, 'WBTC': None, 'LTC': None,
    'LINK': None, 'TRX': None, 'ALGO': None, 'XLM': None, 'ETC': None, 'XTZ': None, 'XMR': None, 'FLOW': None, 'GRT': None, 'ZEC': None, 'KSM': None, 'CHZ': None, 'BAT': None, 'WAVES': None, 'YFI': None, 'QTUM': None,
    'GNO': None, 'OMG': None, 'LPT': None, 'ICX': None, 'SC': None, 'KAVA': None, 'PERP': None, 'GLMR': None, 'PAXG': None, 'REN': None, 'SRM': None, 'MOVR': None, 'CTSI': None, 'LSK': None, 'ASTR': None, 'EWT': None,
    'BAND': None, 'REP': None, 'BADGER': None, 'ACA': None, 'MLN': None, 'CQT': None, 'MIR': None, 'KIN': None, 'RARI': None, 'ORCA': None, 'KAR': None, 'SBR': None, 'STEP': None, 'NANO': None}

BigChangeCounter = {
    'BTC': 0, 'USDT': 0, 'XRP': 0, 'SOL': 0, 'AVAX': 0, 'DOT': 0, 'MATIC': 0, 'DAI': 0, 'ATOM': 0, 'UNI': 0, 'BCH': 0, 'MANA': 0, 'SAND': 0, 'AXS': 0, 'FIL': 0, 'EOS': 0, 'AAVE': 0, 'MKR': 0, 'ENJ': 0, 'CRV': 0, 'LRC': 0,
    'DASH': 0, 'MINA': 0, 'COMP': 0, '1INCH': 0, 'BNT': 0, 'ANKR': 0, 'SNX': 0, 'SUSHI': 0, 'ZRX': 0, 'DYDX': 0, 'STORJ': 0, 'KEEP': 0, 'KNC': 0, 'OCEAN': 0, 'RAY': 0, 'INJ': 0, 'ANT': 0, 'OXT': 0, 'MNGO': 0, 'AKT': 0,
    'REPV2': 0, 'OGN': 0, 'GHST': 0, 'FIDA': 0, 'BAL': 0, 'ATLAS': 0, 'KILT': 0, 'PHA': 0, 'POLIS': 0, 'SDN': 0, 'TBTC': 0, 'OXY': 0, 'BNC': 0, 'KINT': 0, 'AIR': 0, 'ETH': 0, 'USDC': 0, 'ADA': 0, 'LUNA': 0, 'DOGE': 0,
    'SHIB': 0, 'WBTC': 0, 'LTC': 0, 'LINK': 0, 'TRX': 0, 'ALGO': 0, 'XLM': 0, 'ETC': 0, 'XTZ': 0, 'XMR': 0, 'FLOW': 0, 'GRT': 0, 'ZEC': 0, 'KSM': 0, 'CHZ': 0, 'BAT': 0, 'WAVES': 0, 'YFI': 0, 'QTUM': 0, 'GNO': 0, 'OMG': 0,
    'LPT': 0, 'ICX': 0, 'SC': 0, 'KAVA': 0, 'PERP': 0, 'GLMR': 0, 'PAXG': 0, 'REN': 0, 'SRM': 0, 'MOVR': 0, 'CTSI': 0, 'LSK': 0, 'ASTR': 0, 'EWT': 0, 'BAND': 0, 'REP': 0, 'BADGER': 0, 'ACA': 0, 'MLN': 0, 'CQT': 0, 'MIR': 0,
    'KIN': 0, 'RARI': 0, 'ORCA': 0, 'KAR': 0, 'SBR': 0, 'STEP': 0, 'NANO': 0}

_Lastprice = {}
_watchlist = ["BTC", "ETH", "DOGE", "ADA"]
_cryptoDifference = {}
_currentCrypto = {}
temp = []
Descending = []
webhooksurl = "https://maker.ifttt.com/trigger/bitcoin/with/key/hUVRJhLAo8VbMsBmNKKQIb5hY0G1fauQQ493N-Thg8e"


def priceGatherer():
    for i in _tickers:
        checker = True
        while checker:
            try:
                data = requests.get(f"https://api.kraken.com/0/public/Ticker?pair={i}USD")
                newdata = data.json()
                openingprice = float(newdata["result"][_tickerdict[i]]["o"])
                currentbuyprice = float(newdata["result"][_tickerdict[i]]["a"][0])
                percentageDifference = (currentbuyprice - openingprice)/ openingprice * 100
                _cryptoDifference[i] = percentageDifference
                _currentCrypto[i] = currentbuyprice
                checker = False
            except Exception:
                pass

def _sort():
    global temp
    global Descending
    temp = _tickers
    while len(temp) > 0:
        currentnum = 0
        currentticker = None
        for i in temp:
            if currentnum == 0:
                currentnum = _cryptoDifference[i]**2
                currentticker = i
            if _cryptoDifference[i]**2 > currentnum:
                currentnum = _cryptoDifference[i]**2
                currentticker = i
        Descending.append(currentticker)
        if len(temp) == 1:
            temp = []
        else:
            temp = temp[:temp.index(currentticker)] + temp[temp.index(currentticker)+1:]


def DifferenceFromLast():
    try:
        for i in _tickers:
            _Differencetolast[i] = (_currentCrypto[i] - _Lastprice[i]) / _Lastprice[i] * 100
            if _Differencetolast[i]**2 > 1:
                BigChangeCounter[i] += 1
                print("ADDED")
    except Exception:
        temp = []
        with open("cryptoprices3.csv") as file:
            dictfile = csv.DictReader(file, delimiter=",")
            for i in dictfile:
                temp.append(i)
        for i in _tickers:
            try:
                _Differencetolast[i] = (_currentCrypto[i] - float(temp[-1][i])) / float(temp[-1][i]) * 100
            except Exception:
                _Differencetolast[i] = 0


def printer():
    global _Lastprice
    string = ""
    for i in Descending:
        if BigChangeCounter[i] > 0:
            if i in _watchlist:
                string += f"<b>{i}: {round(_currentCrypto[i], 2)}, {round(_cryptoDifference[i], 2)}%, ({round(_Differencetolast[i], 2)})% ({BigChangeCounter[i]})</b> <br \>"
            else:
                string += f"{i}: {round(_currentCrypto[i], 2)}, {round(_cryptoDifference[i], 2)}%, ({round(_Differencetolast[i], 2)})% ({BigChangeCounter[i]}) <br \>"
        else:
            if i in _watchlist:
                string += f"<b>{i}: {round(_currentCrypto[i], 2)}, {round(_cryptoDifference[i], 2)}%, ({round(_Differencetolast[i], 2)})%</b> <br \>"
            else:
                string += f"{i}: {round(_currentCrypto[i], 2)}, {round(_cryptoDifference[i], 2)}%, ({round(_Differencetolast[i], 2)})%<br \>"
    data = {"value1": string}
    requests.post(webhooksurl, data)
    _Lastprice = _currentCrypto


def writer():
    try:
        with open("cryptoprices3.csv") as file:
            pass
    except Exception:
        with open("cryptoprices3.csv", "w") as file:
            dictfile = csv.DictWriter(file, fieldnames=_headers)
            dictfile.writeheader()
    finally:
        tempdict = _currentCrypto
        currentdate = datetime.now()
        formatteddate = currentdate.strftime("%d/%m/%y")
        formattedtime = currentdate.strftime("%H:%M")
        tempdict["Date"] = formatteddate
        tempdict["Time"] = formattedtime
        with open("cryptoprices3.csv", "a") as file:
            dictfile = csv.DictWriter(file, fieldnames=_headers)
            dictfile.writerow(tempdict)


def reset():
    global _cryptoDifference
    global _currentCrypto
    global temp
    global Descending
    _cryptoDifference = {}
    _currentCrypto = {}
    temp = []
    Descending = []


def operator():
    while True:
        priceGatherer()
        _sort()
        DifferenceFromLast()
        printer()
        writer()
        reset()
        time.sleep(300)


if __name__ == "__main__":
    operator()
#!/usr/bin/env python
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import certifi
import json
import warnings
warnings.filterwarnings("ignore")

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/stable/income-statement?symbol=AAPL&apikey=aa91b6fd2bd83cac2f3364e9f4d07e86")
print(get_jsonparsed_data(url))

url = ("https://financialmodelingprep.com/stable/balance-sheet-statement?symbol=AAPL&apikey=aa91b6fd2bd83cac2f3364e9f4d07e86")
print(get_jsonparsed_data(url))

url = ("https://financialmodelingprep.com/stable/cash-flow-statement?symbol=AAPL&apikey=aa91b6fd2bd83cac2f3364e9f4d07e86")
print(get_jsonparsed_data(url))

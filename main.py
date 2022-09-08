from fastapi import FastAPI, Query
import requests

app = FastAPI()

base = 'https://fapi.binance.com'
path1 = '/fapi/v1/ticker/price'
url1 = base+path1
path2 = '/fapi/v1/trades'
url2 = base+path2

@app.get('/api/v1/ticker/price/{symbol}')
def get_ticker_price(symbol: str):
    param = {'symbol': symbol}
    r = requests.get(url1, params=param)
    if r.status_code == 200:
        return r.json()
    else:
        return {'key': 'error'}

@app.get('/api/v1/trades/{symbol}')
def get_trades(symbol: str, limit: int = Query(None, limit=1000)):
    param = {'symbol': symbol, 'limit': limit}
    r = requests.get(url2, params=param)
    if r.status_code == 200:
        return r.json()
    else:
        return {'key': 'error'}
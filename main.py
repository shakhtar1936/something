from fastapi import FastAPI, Query
import httpx
from schemas import Response_price, Response_trades
from typing import List

app = FastAPI()

BASE_API_URL = 'https://fapi.binance.com'

@app.get('/api/v1/ticker/price/{symbol}', response_model=Response_price)
def get_ticker_price(symbol: str):
    param = {'symbol': symbol}
    r = httpx.get(f'{BASE_API_URL}/fapi/v1/ticker/price', params=param)
    if r.status_code == 200:
        return r.json()
    else:
        return {'key': 'error'}

@app.get('/api/v1/trades/{symbol}', response_model=List[Response_trades])
def get_trades(symbol: str, limit: int = Query(None, limit=1000)):
    param = {'symbol': symbol, 'limit': limit}
    r = httpx.get(f'{BASE_API_URL}/fapi/v1/trades', params=param)
    if r.status_code == 200:
        return r.json()
    else:
        return {'key': 'error'}

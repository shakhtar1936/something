from fastapi import FastAPI, Query
import httpx
from schemas import ResponsePrice, ResponseTrades
from typing import List

app = FastAPI()

BASE_API_URL = 'https://fapi.binance.com'

@app.get('/api/v1/ticker/price/{symbol}', response_model=ResponsePrice)
async def get_ticker_price(symbol: str):
    param = {'symbol': symbol}
    async with httpx.AsyncClient() as client:
        r = await client.get(f'{BASE_API_URL}/fapi/v1/ticker/price', params=param)
    if r.status_code == 200:
        return r.json()
    else:
        return {'key': 'error'}

@app.get('/api/v1/trades/{symbol}', response_model=List[ResponseTrades])
async def get_trades(symbol: str, limit: int = Query(None, limit=1000)):
    param = {'symbol': symbol, 'limit': limit}
    async with httpx.AsyncClient() as client:
        r = httpx.get(f'{BASE_API_URL}/fapi/v1/trades', params=param)
    if r.status_code == 200:
        return r.json()
    else:
        return {'key': 'error'}

from pydantic import BaseModel

class ResponsePrice(BaseModel):
    symbol: str
    price: str
    time: int

class ResponseTrades(BaseModel):
    id: int
    price: str
    qty: str
    quoteQty: str
    time: int
    isBuyerMaker: bool

from pydantic import BaseModel

class Response_price(BaseModel):
    symbol: str
    price: str
    time: int

class Response_trades(BaseModel):
    id: int
    price: str
    qty: str
    quoteQty: str
    time: int
    isBuyerMaker: bool
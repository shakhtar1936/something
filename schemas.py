from pydantic import BaseModel, Field

class ResponsePrice(BaseModel):
    symbol: str
    price: str
    time: int

class ResponseTrades(BaseModel):
    id: int
    price: str
    qty: str
    quoteQty: str = Field(alias="quote_qty")
    time: int
    isBuyerMaker: bool

    class Config:
        allow_population_by_field_name = True

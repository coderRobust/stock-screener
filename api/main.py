from fastapi import FastAPI
from stock_logic import get_top_stocks

app = FastAPI()


@app.get("/top-stocks")
def top_stocks():
    return get_top_stocks()

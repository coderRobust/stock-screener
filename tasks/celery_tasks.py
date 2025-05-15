from celery import Celery
from stock_logic import get_top_stocks

app = Celery("tasks", broker="redis://localhost:6379/0")


@app.task
def daily_stock_check():
    stocks = get_top_stocks()
    print("Top Stocks:", stocks)

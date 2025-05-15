import yfinance as yf
import pandas as pd


def get_top_stocks():
    tickers = ["AAPL", "MSFT", "TSLA", "GOOG"]
    result = []
    for t in tickers:
        data = yf.Ticker(t).history(period="7d")
        if data.empty:
            continue
        last_close = data["Close"].iloc[-1]
        result.append({"ticker": t, "last_close": last_close})
    return sorted(result, key=lambda x: x["last_close"], reverse=True)

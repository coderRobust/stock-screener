import yfinance as yf
import matplotlib.pyplot as plt


def plot_ticker(ticker):
    data = yf.Ticker(ticker).history(period="1mo")
    data["Close"].plot(title=f"{ticker} Price")
    plt.savefig(f"charts/{ticker}.png")

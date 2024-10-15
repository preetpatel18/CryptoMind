# data_fetch.py
import yfinance as yf
import pandas as pd

def fetch_data(symbol, period='3mo'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period=period)
    return data

def add_moving_averages(data, short_window=10, long_window=50, use_ema=False):
    if use_ema:
        data['MA_short'] = data['Close'].ewm(span=short_window, adjust=False).mean()
        data['MA_long'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    else:
        data['MA_short'] = data['Close'].rolling(window=short_window).mean()
        data['MA_long'] = data['Close'].rolling(window=long_window).mean()
    return data

def add_rsi(data, window=14):
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

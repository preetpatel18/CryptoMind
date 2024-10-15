# strategies.py

import pandas as pd

def moving_average_crossover(data):
    buy_signals = (data['MA_short'] > data['MA_long']) & (data['MA_short'].shift(1) <= data['MA_long'].shift(1))
    sell_signals = (data['MA_short'] < data['MA_long']) & (data['MA_short'].shift(1) >= data['MA_long'].shift(1))
    
    signals = pd.DataFrame(index=data.index)
    signals['Buy'] = buy_signals
    signals['Sell'] = sell_signals
    return signals

def rsi_strategy(data, buy_threshold=30, sell_threshold=70):
    buy_signals = data['RSI'] < buy_threshold
    sell_signals = data['RSI'] > sell_threshold
    
    signals = pd.DataFrame(index=data.index)
    signals['Buy'] = buy_signals
    signals['Sell'] = sell_signals
    return signals

# plotter.py

import matplotlib.pyplot as plt

def plot_data(data, signals):
    plt.figure(figsize=(16, 8))
    
    plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.5)
    plt.plot(data['MA_short'], label='Short MA', color='green', alpha=0.75, linewidth=1.5)
    plt.plot(data['MA_long'], label='Long MA', color='red', alpha=0.75, linewidth=1.5)
    
    plt.scatter(signals[signals['Buy']].index, data['Close'][signals['Buy']], marker='^', color='green', label='Buy Signal', s=100, zorder=5)
    plt.scatter(signals[signals['Sell']].index, data['Close'][signals['Sell']], marker='v', color='red', label='Sell Signal', s=100, zorder=5)
    
    plt.title(f'Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price in USD')
    plt.legend(loc='upper left')
    plt.grid(alpha=0.3)
    plt.show()
    
def plot(data, signals, window_size=60):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.5)
    
    buy_signals = signals[signals['Buy']].index
    sell_signals = signals[signals['Sell']].index
    
    adjusted_buy_indices = data.index.intersection(buy_signals)
    adjusted_sell_indices = data.index.intersection(sell_signals)

    plt.scatter(adjusted_buy_indices, data['Close'].loc[adjusted_buy_indices],marker='^', color='green', label='Buy Signal', s=100, zorder=5)
    plt.scatter(adjusted_sell_indices, data['Close'].loc[adjusted_sell_indices], marker='v', color='red', label='Sell Signal', s=100, zorder=5)
    
    plt.title('Stock Price with Buy and Sell Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')
    plt.grid(alpha=0.3)
    plt.show()
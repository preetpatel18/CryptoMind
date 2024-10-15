# main.py

from data_fetch import fetch_data, add_moving_averages, add_rsi
from strategies import moving_average_crossover, rsi_strategy
from plotter import plot_data, plot
from model import train_lstm_model, lstm_strategy

# Parameters
symbol = 'BTC-USD'
short_window = 10
long_window = 50
use_ema = True
rsi_buy_threshold = 30
rsi_sell_threshold = 70
window_size = 60
epochs = 5
batch_size = 1

def main():
    data = fetch_data(symbol)
    
    data = add_moving_averages(data, short_window=short_window, long_window=long_window, use_ema=use_ema)
    data = add_rsi(data)
    strategy = input("Choose a strategy (ma_crossover, rsi, lstm): ").strip()
    if strategy == 'ma_crossover':
        signals = moving_average_crossover(data)
        plot_data(data, signals)
    elif strategy == 'rsi':
        signals = rsi_strategy(data, buy_threshold=rsi_buy_threshold, sell_threshold=rsi_sell_threshold)
        plot_data(data, signals)
    elif strategy == 'lstm':
        model, scaler = train_lstm_model(data, window_size=window_size, epochs=epochs, batch_size=batch_size)
        signals = lstm_strategy(data, model, scaler, window_size=window_size)
        plot(data, signals)
    else:
        print("Invalid strategy")
        return

if __name__ == '__main__':
    main()

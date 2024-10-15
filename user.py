import yfinance as yf
import time

symbol = 'BTC-USD'  # Trading pair for Bitcoin
amount = 0.001  # Amount to trade
buy_price = 20000  # Value Determined by the AI Algorithm (upcoming in Future)
sell_price = 25000 # Value Determined by the AI Algorithm (upcoming in Future)

# Fetch Market Data
def fetch_market_data():
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='1d')
    return data['Close'][-1]  # Return the last closing price

def main():
    while True:
        try:
            last_price = fetch_market_data()
            print(f'Current BTC Price: ${last_price:.2f}')

            # Example trading logic
            if last_price < buy_price:
                place_order('buy')
            elif last_price > sell_price:
                place_order('sell')

            time.sleep(10)  # Adjust time as needed

        except Exception as e:
            print(f'Error: {e}')
            time.sleep(10)
            
            
def place_order(order_type):
    if order_type == 'buy':
        print(f'Placing buy order for {amount} BTC at market price.')
    elif order_type == 'sell':
        print(f'Placing sell order for {amount} BTC at market price.')
        
if __name__ == '__main__':
    main()
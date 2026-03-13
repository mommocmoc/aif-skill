import os
import time
import pyupbit

# Environment variables
ACCESS_KEY = os.environ.get('UPBIT_ACCESS_KEY')
SECRET_KEY = os.environ.get('UPBIT_SECRET_KEY')

def execute_trade(ticker, side, amount_or_volume):
    """
    Because Upbit has extremely strict payload hashing rules for POST requests,
    we use the official pyupbit SDK for the actual financial transactions (the 'hands'),
    ensuring 100% reliability. The AIF CLI can be used for gathering data (the 'eyes').
    """
    upbit = pyupbit.Upbit(ACCESS_KEY, SECRET_KEY)
    
    if side == 'bid':
        print(f"Executing BUY order for {ticker}...")
        res = upbit.buy_market_order(ticker, amount_or_volume)
    else:
        print(f"Executing SELL order for {ticker}...")
        res = upbit.sell_market_order(ticker, amount_or_volume)
        
    return res

if __name__ == "__main__":
    # Example usage
    # execute_trade("KRW-DOGE", "bid", 5000)
    pass
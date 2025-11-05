import ccxt
import pandas as pd
from datetime import datetime, timedelta

binance = ccxt.binance()

def fetch_price_history(symbol, minutes=180):
    """Завантажує історію ціни після лістингу"""
    since = binance.milliseconds() - minutes * 60 * 1000
    ohlcv = binance.fetch_ohlcv(symbol, '1m', since=since)
    df = pd.DataFrame(ohlcv, columns=["time","open","high","low","close","vol"])
    df["time"] = pd.to_datetime(df["time"], unit='ms')
    return df

def analyze_price_movement(df):
    """Аналізує ціновий рух після лістингу"""
    if df.empty: return None
    start = df["open"].iloc[0]
    peak = df["high"].max()
    drop = df["low"].min()
    change = (df["close"].iloc[-1] / start - 1) * 100
    return {
        "initial_pump_%": (peak/start - 1)*100,
        "final_change_%": change,
        "max_drawdown_%": (drop/start - 1)*100
    }

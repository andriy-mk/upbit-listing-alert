import time, os, pandas as pd
from upbit_scraper import fetch_latest_listings
from telegram_bot import send_message
from price_analyzer import fetch_price_history, analyze_price_movement
from model_listing_analyzer import predict_future_move
from config import *

def main():
    seen = set()
    if os.path.exists(LISTINGS_HISTORY):
        df = pd.read_csv(LISTINGS_HISTORY)
        seen = set(df["title"].values)

    while True:
        listings = fetch_latest_listings()
        for l in listings:
            if l["title"] not in seen:
                seen.add(l["title"])
                msg = f"🚨 Новий лістинг: <b>{l['title']}</b>\n{l['link']}"
                print(msg)
                send_message(msg)

                # (опційно) Спробуємо знайти пару на Binance
                # symbol = "NEWCOIN/USDT"
                # df = fetch_price_history(symbol)
                # res = analyze_price_movement(df)
                # if res:
                #     pred = predict_future_move(res['initial_pump_%'], res['max_drawdown_%'])
                #     send_message(f"📈 Аналіз: {res}\n🤖 Прогноз: {pred:.2f}%")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

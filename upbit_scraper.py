import requests
import pandas as pd
from datetime import datetime
import os, time

UPBIT_NEWS_URL = "https://api-manager.upbit.com/api/v1/notices?per_page=20"

def fetch_latest_listings():
    """Парсить останні оголошення про лістинги з Upbit"""
    r = requests.get(UPBIT_NEWS_URL).json()
    items = r.get("data", [])
    listings = []

    for item in items:
        title = item.get("title", "").lower()
        if "new digital asset" in title or "listing" in title:
            listings.append({
                "title": item["title"],
                "link": f"https://upbit.com/service_center/notice?id={item['id']}",
                "created_at": item["created_at"]
            })
    return listings

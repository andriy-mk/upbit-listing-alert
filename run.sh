#!/bin/bash
echo "🚀 Запуск Upbit Listing Bot"
source venv/bin/activate
nohup python3 main.py > logs/signals.log 2>&1 &
echo "✅ Бот запущено у фоновому режимі."

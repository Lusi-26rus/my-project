# data/config.py

BASE_URL = "https://kinopoisk.ru"
# Важно: добавлены 'api.' и '/v1.4'
API_URL = "https://api.poiskkino.dev" 
TOKEN = "4CA3GK8-XVW4W40-HA65XZP-PPM8DKB"

HEADERS = {
    "X-API-KEY": TOKEN,
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


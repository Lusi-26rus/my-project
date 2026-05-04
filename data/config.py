from typing import Final, Dict

# 1. Базовые URL (убираем хардкод из тестов)
BASE_URL: Final[str] = "https://kinopoisk.ru"
API_URL: Final[str] = "https://api.poiskkino.dev/"

# 2. Авторизация
TOKEN: Final[str] = "4CA3GK8-XVW4W40-HA65XZP-PPM8DKB"

# 3. Заголовки (с аннотацией типов)
HEADERS: Final[Dict[str, str]] = {
    "X-API-KEY": TOKEN,
    "Accept": "application/json",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/119.0.0.0 Safari/537.36"
    ),
}

def pytest_configure(config):
    config.addinivalue_line("markers", "api: tests for API endpoints")
    config.addinivalue_line("markers", "ui: tests for UI components")

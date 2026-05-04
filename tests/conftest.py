import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()

    # 1. Скрываем флаг автоматизации navigator.webdriver
    options.add_argument("--disable-blink-features=AutomationControlled")

    # 2. Убираем уведомление "Браузером управляет автоматизированное ПО"
    # В conftest.py
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    # Это поможет обходить простую защиту

    driver = webdriver.Chrome(options=options)

    # 4. Выполняем скрипт, который удаляет следы Selenium
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """},
    )

    driver.maximize_window()
    yield driver
    driver.quit()

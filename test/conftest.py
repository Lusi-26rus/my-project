import undetected_chromedriver as uc
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    
    # 1. Скрываем флаг автоматизации navigator.webdriver
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # 2. Убираем уведомление "Браузером управляет автоматизированное ПО"
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # 3. Устанавливаем реальный User-Agent (можешь скопировать свой из браузера)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    
    # 4. Выполняем скрипт, который удаляет следы Selenium
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })

    driver.maximize_window()
    yield driver
    driver.quit()


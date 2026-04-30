import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

BASE_URL = "https://kinopoisk.ru"

@pytest.mark.ui
class TestKinopoiskUI:

    @allure.title("поиск по названию")
    def test_ui_search_by_name(self, browser):
        with allure.step("Зайти на сайт kinopoisk.ru"):
            browser.get(BASE_URL)
            wait = WebDriverWait(browser, 15)
        
        with allure.step("Нажать на поисковую строку и ввести название"):
            search_input = wait.until(EC.element_to_be_clickable
                                      ((By.CSS_SELECTOR, "input[name='kp_query']")))
            search_input.click()
            search_input.send_keys("Полярный")
            search_input.send_keys(Keys.ENTER)

        with allure.step("Проверить, что поисковик выдал результаты"):
            # Ждем появления заголовка с результатами или списка фильмов
            results = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.search_results, h1.search_results_title")
            ))
            assert results.is_displayed(), "Результаты поиска не отобразились"


    @allure.title("Просмотр фильма")
    def test_ui_view(self, browser):
        with allure.step("Открыть страницу фильма"):
            browser.get(f"{BASE_URL}/film/535341/")
        with allure.step("Проверить кнопку Смотреть"):
            btn = browser.find_element(By.CSS_SELECTOR, "button[data-test-id='Offer']")
            assert btn.is_displayed()

    @allure.title("Буду смотреть")
    def test_ui_wishlist(self, browser):
        with allure.step("Открыть страницу фильма"):
            browser.get(f"{BASE_URL}/series/485542/")

        wait = WebDriverWait(browser, 15)
    
        with allure.step("Проверить кнопку Буду смотреть"):
            btn = wait.until(EC.element_to_be_clickable
                             ((By.CSS_SELECTOR, "button[title='Буду смотреть']")))
            assert btn.is_enabled(), "Кнопка неактивна"
            assert btn.get_attribute("aria-pressed") == "false", "Кнопка уже нажата"
            assert btn.is_enabled()


    @allure.title("Расширенный поиск")
    def test_ui_filters(self, browser):
        with allure.step("Перейти в расширенный поиск"):
            browser.get(f"{BASE_URL}/s/")
    
        wait = WebDriverWait(browser, 15)
    
        with allure.step("Проверить форму фильтров"):
            country_element = wait.until(
            EC.presence_of_element_located((By.ID, "country"))
        )
        assert country_element.is_displayed()


    @allure.title("Форма оценки")
    def test_ui_rating(self, browser):
        with allure.step("Открыть страницу фильма"):
            browser.get(f"{BASE_URL}/film/435/")
        with allure.step("Проверить блок рейтинга"):
            rating = browser.find_element(By.CLASS_NAME, "film-rating")
            assert rating.is_displayed()

    
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from data.config import BASE_URL


@pytest.mark.ui
@allure.epic("Тестирование UI Кинопоиска")
class TestKinopoiskUI:

    @allure.title("Поиск по названию")
    def test_ui_search_by_name(self, browser) -> None:
        wait = WebDriverWait(browser, 15)

        with allure.step(f"Зайти на сайт {BASE_URL}"):
            browser.get(BASE_URL)

        with allure.step("Нажать на поисковую строку и ввести название"):
            search_input = wait.until(
                EC.element_to_be_clickable((By.NAME, "text"))
            )
            search_input.send_keys("Полярный" + Keys.ENTER)

            with allure.step("Проверить, что поисковик выдал результаты"):
                results = wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR,
                         "h2, [data-tid='21855562'], .search-page"))
                )
            assert (
                results.is_displayed()
            ), "Результаты поиска не отобразились на странице"

    @allure.title("Просмотр фильма")
    def test_ui_view(self, browser) -> None:
        wait = WebDriverWait(browser, 15)
        with allure.step("Открыть страницу фильма"):
            browser.get(f"{BASE_URL}/film/535341/")

        with allure.step("Проверить кнопку 'Смотреть'"):
            btn = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "button[data-test-id='Offer']")
                )
            )
            assert btn.is_displayed()

    @allure.title("Добавление в 'Буду смотреть'")
    def test_ui_wishlist(self, browser) -> None:
        wait = WebDriverWait(browser, 15)
        with allure.step("Открыть страницу сериала"):
            browser.get(f"{BASE_URL}/series/485542/")

        with allure.step("Проверить кнопку 'Буду смотреть'"):
            btn = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button[title='Буду смотреть']")
                ))
            assert btn.is_enabled(), "Кнопка неактивна"
            assert (
                btn.get_attribute("aria-pressed") == "false"
            ), "Кнопка уже нажата"

    @allure.title("Расширенный поиск")
    def test_ui_filters(self, browser) -> None:
        wait = WebDriverWait(browser, 15)
        with allure.step("Перейти в расширенный поиск"):
            browser.get(f"{BASE_URL}/lists/categories/movies/1/")

        with allure.step("Проверить наличие фильтров"):
            filter_btn = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "button, select"))
            )
            assert filter_btn.is_displayed()

    @allure.title("Форма оценки")
    def test_ui_rating(self, browser) -> None:
        wait = WebDriverWait(browser, 15)
        with allure.step("Открыть страницу фильма"):
            browser.get(f"{BASE_URL}/film/435/")

        with allure.step("Проверить блок рейтинга"):
            rating = wait.until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "film-rating"))
            )
            assert rating.is_displayed()

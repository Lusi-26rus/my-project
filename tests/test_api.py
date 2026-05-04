import requests
import pytest
import allure
import sys
import os
from data.config import API_URL, HEADERS
sys.path.insert
(0, os.path.abspath(os.path.join
                    (os.path.dirname(__file__), "..")
                    ))


@pytest.mark.api
@allure.epic("Тестирование API Кинопоиска")
@allure.feature("Поиск и получение информации о фильмах")
class TestKinopoiskAPI:

    @allure.title("Поиск фильма по названию")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_search_movie(self) -> None:
        with allure.step("Отправить GET запрос на поиск фильма '1+1'"):
            response = requests.get(
                f"{API_URL}/movie/search",
                headers=HEADERS, params={"query": "1+1"}
            )

        with allure.step("Проверить, что статус-код 200"):
            assert response.status_code == 200

    @allure.title("Получение фильма по ID")
    def test_get_by_id(self) -> None:
        with allure.step("Запросить информацию о фильме с ID 435"):
            response = requests.get(f"{API_URL}/movie/435", headers=HEADERS)

        with allure.step("Проверить успешность запроса"):
            assert response.status_code == 200

    @allure.title("Получение списка возможных значений полей")
    def test_possible_values(self) -> None:
        with allure.step("Запросить возможные значения полей"):
            response = requests.get(
                f"{API_URL}/movie/possible-values-by-field", headers=HEADERS
            )
        assert response.status_code == 200

    @allure.title("Проверка ошибки авторизации")
    def test_unauthorized(self) -> None:
        with allure.step("Отправить запрос без токена авторизации"):
            response = requests.get(f"{API_URL}/movie/435")

        with allure.step("Проверить, что получен статус 401"):
            assert response.status_code == 401

    @allure.title("Поиск несуществующего фильма")
    def test_search_empty(self) -> None:
        params = {"query": "чввпаввв"}
        with allure.step(f"Поиск по строке: {params['query']}"):
            response = requests.get(
                f"{API_URL}/movie/search", headers=HEADERS, params=params
            )
            assert response.status_code == 200

    @allure.step("Проверить, что API вернул успех и корректный JSON")
    def check_response(response):
        if "text/html" in response.headers.get("Content-Type", ""):
            pytest.skip(
                "Сервер вернул HTML (капчу) вместо JSON. Пропуск теста.")
        assert response.status_code == 200

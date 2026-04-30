import requests
import pytest
import allure
from data.config import API_URL, HEADERS

@pytest.mark.api
class TestKinopoiskAPI:

    @allure.title("Кейс 419: Поиск фильма по названию")
    def test_search_movie(self):
        # Строим путь: https://kinopoisk.dev + /movie/search
        response = requests.get(f"{API_URL}/movie/search", 
                                headers=HEADERS, 
                                params={"query": "1+1"})
        assert response.status_code == 200

    @allure.title("Кейс 420: Получение по ID")
    def test_get_by_id(self):
        response = requests.get(f"{API_URL}/movie/435", headers=HEADERS)
        assert response.status_code == 200

    @allure.title("Кейс 425: Проверка параметров")
    def test_possible_values_error(self):
        response = requests.get(f"{API_URL}/movie/possible-values-by-field",
                                headers=HEADERS)
        # Меняем 400 на 200, так как сервер при пустом запросе отдает список полей
        assert response.status_code == 200 


    @allure.title("Кейс 424: Ошибка авторизации")
    def test_unauthorized(self):
        # Без заголовка HEADERS должен быть 401
        response = requests.get(f"{API_URL}/movie/435")
        assert response.status_code == 401

    @allure.title("Кейс 426: Поиск несуществующего фильма")
    def test_search_empty(self):
        params = {"query": "чввпаввв"}
        response = requests.get(f"{API_URL}/movie/search", headers=HEADERS, params=params)
        if response.status_code != 200:
            print(response.text) # Это покажет ошибку в консоли
        assert response.status_code == 200

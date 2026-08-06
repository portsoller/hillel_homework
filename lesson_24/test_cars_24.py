import logging
import pytest

class CarsAPI:
    def __init__(self, session):
        self.session = session
        self.base_url = 'http://127.0.0.1:8080'

    def get_cars(self, sort_by=None, limit=None):
        params = {
            "sort_by": sort_by,
            "limit": limit
        }
        return self.session.get(f'{self.base_url}/cars', params=params)

class TestCarSearch:
    @pytest.fixture(autouse=True)
    def setup_api(self, auth_session):
        self.api = CarsAPI(auth_session)

    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 10),
        ("brand", 1),
        ("price", 25),
        (None, 5),
        ("year", None)
    ])

    def test_search_cars(self, sort_by, limit):
        logging.info(f"Запуск тесту с sort_by={sort_by} и limit={limit}")
        response = self.api.get_cars(sort_by=sort_by, limit=limit)
        assert response.status_code == 200
        cars = response.json()
        logging.info(f"Статус відповіді: {response.status_code}")
        logging.info(f"Отримані дані: {cars}")
        assert isinstance(cars, list)

        if limit:
            assert len(cars) <= limit

        if sort_by:
            values = [car[sort_by] for car in cars]
            assert values == sorted(values)

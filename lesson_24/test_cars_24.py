import logging
import pytest

class TestCarSearch:

    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 3),
    ])
    def test_search_cars(self, auth_session, sort_by, limit):
        logging.info(f"Запуск теста с sort_by={sort_by} и limit={limit}")
        response = self.session.get(http://127.0.0.1:8080/cars, sort_by={sort_by}, limit={limit}')
        assert response.status_code == 200
        ')

import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Хэндлер для записи в файл
    file_handler = logging.FileHandler('test_search.log', mode='w', encoding='utf-8')
    file_handler.setFormatter(formatter)

    # Хэндлер для вывода в консоль
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Очищаем старые хэндлеры (если есть) и добавляем новые
    logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


@pytest.fixture(scope='class')
def auth_session():
    session = requests.Session()
    # Делаем логин
    res = session.post('http://127.0.0.1:8080/auth', auth=HTTPBasicAuth('test_user', 'test_pass'))
    token = res.json().get('access_token')

    # Устанавливаем заголовок авторизации для всех будущих запросов этой сессии
    session.headers.update({'Authorization': f'Bearer {token}'})

    yield session

    # Опционально: закрываем сессию после выполнения всех тестов класса
    session.close()
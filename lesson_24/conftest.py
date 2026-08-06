import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler('test_search.log', mode='w', encoding='utf-8')
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

@pytest.fixture(scope='class')
def auth_session():
    session = requests.Session()
    res = session.post('http://127.0.0.1:8080/auth', auth=HTTPBasicAuth('test_user', 'test_pass'))
    token = res.json().get('access_token')
    session.headers.update({'Authorization': f'Bearer {token}'})

    yield session
    session.close()

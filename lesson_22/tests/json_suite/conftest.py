import json
import logging
from pathlib import Path
import pytest

CURRENT_DIR = Path(__file__).parent

@pytest.fixture(scope='session')
def json_logger():
    logger = logging.getLogger('json_validator')
    log_file = CURRENT_DIR / 'json__abramenko.log'
    handler = logging.FileHandler(log_file, encoding='utf-8')
    logger.addHandler(handler)
    return logger

@pytest.fixture
def json_files(lesson_15_dir):
    json_dir = lesson_15_dir / 'work_with_json'
    return [f for f in json_dir.iterdir() if f.is_file()]

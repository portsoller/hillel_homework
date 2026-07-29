import logging
import pytest
from pathlib import Path

@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True,
    )

PROJECT_ROOT = Path(__file__).parent.parent.parent

@pytest.fixture(scope="session")
def project_root():
    return PROJECT_ROOT

@pytest.fixture(scope="session")
def lesson_15_dir(project_root):
    return project_root / "lesson_15"

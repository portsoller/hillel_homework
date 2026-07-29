import json
import pytest

@pytest.mark.smoke
def test_validate_json_files(json_files, json_logger):

    for file in json_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                json.load(f)
        except json.JSONDecodeError as e:
            json_logger.error(
                f'Файл {file.name} не є валідним JSON. Помилка: {e}'
            )

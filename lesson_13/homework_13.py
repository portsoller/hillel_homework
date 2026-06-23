"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import unittest

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

def get_message(username, status):
    return "Login event - Username: {}, Status: {}".format(username, status)

class TestLogin(unittest.TestCase):

    def test_log_success(self):
        # success
        log_event("user1", "success")
        message = get_message("user1", "success")
        with open("login_system.log", "r") as read_file:
            log_content = read_file.read()
        assert message in log_content

    def test_log_expired(self):
        log_event("user2", "expired")
        message_expired = get_message("user2", "expired")
        with open("login_system.log", "r") as read_file:
            log_content = read_file.read()
        assert message_expired in log_content

    def test_log_failed(self):
        log_event("user3", "failed")
        message_failed = get_message("user3", "failed")
        with open("login_system.log", "r") as read_file:
            log_content = read_file.read()
        assert message_failed in log_content

    if __name__ == "__main__":
        unittest.main()

import logging
import pytest

def get_group_details(root, group_number):
    for group in root.findall('group'):
        group_number_element = group.find('number')
        if group_number_element is not None and group_number_element.text == group_number:
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    logging.info(f"Group: {group.find('name').text}, incoming: {incoming.text}")
                    return incoming.text
                else:
                    logging.info(f"Group: {group.find('name').text}, incoming: Не знайдено")
                    return None
            else:
                logging.info(f"Group: {group.find('name').text}, timingExbytes не знайдено")
                return None

    logging.warning(f"The group with a number {group_number} does not found!")
    return None

@pytest.mark.regression
def test_get_group_details(root):
    result = get_group_details(root,'2')
    assert result is not None
    #pytest.xfail("Очікуваний результат не співпадає з отриманим")

@pytest.mark.smoke
def test_get_invalid_group(root):
    result = get_group_details(root,'1')
    assert result is None

@pytest.mark.xfail(reason="Помилка очікується")
def test_example():
    assert 1 == 2  # Помилка очікується

import pytest
import xml.etree.ElementTree as ET

@pytest.fixture
def root(lesson_15_dir):
    xml_path = lesson_15_dir / 'groups.xml'
    tree = ET.parse(xml_path)
    return tree.getroot()

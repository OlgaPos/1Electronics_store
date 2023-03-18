import pytest
from items import *


@pytest.fixture
def test_item1():
    return Item("Keyboard", 1000, 20)


@pytest.fixture
def test_new_item():
    return Item("None", 1000, 20)


@pytest.fixture()
def test_phone1():
    return Phone("iPhone 14", 120_000, 5, 2)

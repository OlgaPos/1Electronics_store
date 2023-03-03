import pytest
from items import Item


@pytest.fixture
def test_item1():
    return Item("Keyboard", 1000, 20)


def test_multiply_price_quantity(test_item1):
    assert test_item1.calculate_total_price() == 20000


def test_apply_discount(test_item1):
    test_item1.apply_discount()
    assert test_item1.discount_price == 800.0

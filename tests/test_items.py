import pytest
from items import *


def test_multiply_price_quantity(test_item1):
    """Проверяем расчёт общей стоимости одного типа товара"""
    assert test_item1.calculate_total_price() == 20000


def test_apply_discount(test_item1):
    """Проверяем применение скидки"""
    assert test_item1.apply_discount() == 850.0


def test_change_name(test_item1, value="Board"):
    """Проверяем, что можно поменять название товара, несмотря на то, что name теперь приватный атрибут"""
    test_item1.name = value
    print(test_item1.name)
    assert test_item1.name == "Board"


def test_name(value="SuperKeyboard"):
    """Проверяем, что попытка присвоить имя длиннее, чем 10 символов, не сработает"""
    with pytest.raises(Exception):
        Item({value})


def test_is_integer():
    """Проверяем, что переданные значения являются целыми числами"""
    assert Item.is_integer(6) is True
    assert Item.is_integer(6.0) is True
    assert Item.is_integer(6.4) is False


def test_instantiate_from_csv():
    """Проверяем создание списка товаров из файла csv"""
    assert len(Item.instantiate_from_csv(path='./data/items.csv')) == 5


def test_str(test_item1):
    assert str(test_item1) == "Keyboard"


def test_repr(test_phone1):
    assert repr(test_phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(test_phone1):
    """Проверяем, что количество сим-карт больше 0"""
    assert test_phone1.number_of_sim == 2
    test_phone1.number_of_sim = 1
    assert test_phone1.number_of_sim == 1
    with pytest.raises(Exception):
        test_phone1.number_of_sim = 0


def test_add(test_item1, test_phone1):
    """Проверяем возможность сложения между классами"""
    assert test_item1 + test_phone1 == 25
    assert test_phone1 + test_item1 == 25
    assert test_phone1 + test_phone1 == 10
    assert test_item1 + test_item1 == 40
    with pytest.raises(ValueError):
        print(test_phone1 + 100)


def test_repr_kb(test_kb1):
    assert repr(test_kb1) == "KeyBoard('Dark Project KD87A', 9600, 5)"


def test_change_lang(test_kb1):
    """Проверяем текущую раскладку клавиатуры и её изменение"""
    assert test_kb1.language == 'EN'
    test_kb1.change_lang()
    assert test_kb1.language == 'RU'


# def test_error_csv_file_damaged():
#     """Проверяем, что файл csv повреждён"""
#     assert Item.instantiate_from_csv(path='./data/items2.csv') == "Файл item.csv поврежден"


def test_file_not_found_error():
    """Проверяем, что файл csv отсутствует"""
    assert Item.instantiate_from_csv(path='./data/items3.csv') == "Отсутствует файл tests/items.csv"

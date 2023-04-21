import pytest

from course.operations import Operation
from course.utils import read_json



@pytest.fixture()
def class_test():
    return Operation( "2019-01-05T00:52:30.108534",
                     {"amount": int(87941.37), "currency": {"name": "руб.", "code": "RUB"}},"Перевод со счета на счет",
                     "Счет 46363668439560358409", "Счет 46363668439560358409" )


@pytest.fixture()
def second_text():
    return Operation("2019-07-13T18:51:29.313309", {"amount": "97853.86","currency": { "name": "руб.", "code": "RUB"}},"Перевод с карты на счет",
    "Maestro 1308795367077170", "Счет 96527012349577388612")

@pytest.fixture()
def third_test():
    return Operation("2019-07-15T11:47:40.496961",{"amount": "92688.46","currency": {"name": "USD","code": "USD"} }, "Открытие вклада", "Счет 35737585785074382265","Счет 35737585785074382265")


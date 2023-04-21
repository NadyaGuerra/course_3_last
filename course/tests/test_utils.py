import datetime
import os

BASE_PATH = os.path.abspath("data")
JSON_PATH = os.path.join(BASE_PATH, "operations.json")

from course.utils import read_json, executed, data_sort


def test_executed():
    test_data = [{"state": "EXECUTED"},
                 {"state": "EXECUTED"},
                 {"state": "EXECUTED"}]
    assert executed([]) == []

    assert executed(test_data) == [{"state": "EXECUTED"},
                                   {"state": "EXECUTED"},
                                   {"state": "EXECUTED"}]


def test_sort_data():
    sort = [{"date": "2019-07-13T18:51:29.313309"},
            {"date": "2019-01-05T00:52:30.108534"},
            {"date": "2019-07-15T11:47:40.496961"}]

    assert data_sort(sort) == [{'date': '2019-01-05T00:52:30.108534'},
                               {'date': '2019-07-13T18:51:29.313309'},
                               {'date': '2019-07-15T11:47:40.496961'}]


def test_import_file():
    json = [{"id": 667307132, "state": "EXECUTED", "date": "2019-07-13T18:51:29.313309",
             "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
             "description": "Перевод с карты на счет", "from": "Maestro 1308795367077170",
             "to": "Счет 96527012349577388612"}]
    assert read_json() == [{"id": 667307132, "state": "EXECUTED", "date": "2019-07-13T18:51:29.313309",
                            "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
                            "description": "Перевод с карты на счет", "from": "Maestro 1308795367077170",
                            "to": "Счет 96527012349577388612"}]

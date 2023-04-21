import json
import os

BASE_PATH = os.path.abspath('data')
JSON_PATH = os.path.join(BASE_PATH,"operations.json")


def read_json():
    """функция считывания файла"""
    with open(JSON_PATH, "r", encoding="utf-8") as data:
        return json.load(data)


def executed(data:list):
    """функция создания списка выполненных операций"""
    state_executed = []
    for i in range(len(data)):
        if data[i].get("state") == "EXECUTED":
            state_executed.append(data[i])
    return state_executed

def data_sort(data:list):
    """функция сортировки даты"""
    data.sort(key=lambda x: x["date"])
    return data
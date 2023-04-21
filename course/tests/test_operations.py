from course.operations import Operation
import pytest





def test_date_format_correct(class_test):
    assert class_test.date_format() == '05.01.2019'


def test_amount(class_test):
    assert class_test.get_amount() == 87941

def test_amount_second(second_text):
    assert second_text.get_amount()=="97853.86"


def test_description(class_test):
    assert class_test.get_description()=='Перевод со счета на счет'

def test_second(second_text):
    assert second_text.get_description()=="Перевод с карты на счет"

def test_third(third_test):
    assert third_test.get_description()== "Открытие вклада"

def test_hide(class_test):
    assert class_test.hide_to()== 'Счет **8409'
def test_hide_1(second_text):
    assert second_text.hide_to()=='Счет **8612'

def test_third_2(third_test):
    assert third_test.hide_to()== "Счет **2265"

def test_where_from(class_test):
    assert class_test.where_from_method()=='Счет 463636**********8409'
def test_where_from_1(second_text):
    assert second_text.where_from_method()=='Maestro 130879******7170'

def test_currency(class_test):
    assert class_test.get_currency()=="руб."
def test_currency_second(second_text):
    assert second_text.get_currency()=="руб."
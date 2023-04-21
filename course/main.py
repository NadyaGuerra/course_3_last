from utils import read_json, executed, data_sort
from operations import Operation

numbers_of_operations = 5


def main():
    data = data_sort(executed(read_json()))
    data.reverse()

    for i in range(5):
        print(data[i])  # получаем последние 5 операций


    operation = [Operation(data[i].get("date"), data[i].get("operationAmount"), data[i].get("description"),
                           data[i].get("from"),
                           data[i].get("to")) for i in range(numbers_of_operations)]

    for i in range(numbers_of_operations):
        print(f"{operation[i].date_format()} {operation[i].get_description()}")
        if operation[i].where_from_method() != None:
            print(f"{operation[i].where_from_method()}=>{operation[i].hide_to()}")
        else:
            print(f"{operation[i].hide_to()}")

        print(f"{operation[i].get_amount()} {operation[i].get_currency()}\n")

main()

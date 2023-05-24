"""task 3"""
import csv
from collections import defaultdict


def correct_data(date:int, month :int)->bool:
    '''check correct datas'''
    return 1 <= date <= 12 and 1 <= month <= 31


def calculate_profit(oper_data:tuple, depart_data:tuple):
    '''main func calculate'''
    profits = defaultdict(int)

    for entry in oper_data:
        year, month, id, profit = entry
        key = (year, month, department_id, )
        profits[key] += profit

    result = {(year, month, id, profit) for (year, month, division), profit in profits.items()}
    print(result)
    return result


def out_reader(reader: tuple)-> None:
    '''out data from reader .csv'''
    for row in reader:
        print(row)

def get_data()->None:
    '''get data from files'''
    with open('./file3/departments.csv', newline='', encoding='utf-8') as f:
        ddepart = csv.DictReader(f, delimiter=",")    

    with open('./file3/operations.csv', newline='', encoding='utf-8') as f:
        oper = csv.DictReader(f, delimiter=",")
        out_reader(oper)

if __name__ == "__main__":
    get_data()
def process_table_data(table_data):
    result = set()
    monthly_profit = {}

    for row in table_data:
        year = row['year']
        month = row['month']
        department_id = row['department_id']
        income = int(row['income'])

        key = (year, month, department_id)
        monthly_profit[key] = monthly_profit.get(key, 0) + income

    for key, profit in monthly_profit.items():
        year, month, department_id = key
        result.add((year, month, department_id, profit))

    return result
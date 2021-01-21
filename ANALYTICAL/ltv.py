import pandas as pd
from datetime import datetime

pd.options.display.max_columns = 20


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def how_many_conversion(week):
    return len(list(filter(lambda x: x >= week, all_conversions_list)))


def count_lvt(price, conversions, is_apple=True, is_have_trial=True):
    k = 1
    if is_have_trial:
        conversions -= 1
    if is_apple:
        k = 0.7
    ltv = k * price * conversions
    return ltv


DATASET = pd.read_csv('data_analytics.csv')
# print(DATASET)
PRICE_PER_PURCHASE = 9.99

subscriber_id_col = list(DATASET['Subscriber ID'])

list_of_unique_clients_id = list(set(subscriber_id_col))
list_of_count_of_conversions = \
    [subscriber_id_col.count(x) for x in list_of_unique_clients_id]
dict_of_count_of_conversions = \
    dict(zip(list_of_unique_clients_id, list_of_count_of_conversions))

date_dict = {}
for id in list_of_unique_clients_id:
    date_dict[id] = list((DATASET[lambda x: x['Subscriber ID'] == id])['Event Date'])

all_conversions_list = []
for id in date_dict:
    if len(date_dict[id]) - 1 != 0:
        all_conversions_list.append(len(date_dict[id]) - 1)

_0to_1 = how_many_conversion(1)
_1to_2 = how_many_conversion(2)
_2to_3 = how_many_conversion(3)
_3to_4 = how_many_conversion(4)
_4to_5 = how_many_conversion(5)
print(_0to_1, _1to_2, _2to_3, _3to_4, _4to_5)
a1 = 9.99 * 0.7 * _0to_1
a2 = a1 * _1to_2
a3 = a2 * _2to_3
a4 = a3 * _3to_4
a5 = a4 * _4to_5
print(a1+a2+a3+a4+a5)
print()
print(f'proceeds is {(_0to_1 + _1to_2 + _2to_3 + _3to_4 + _4to_5)*9.99*0.7}')
print(f'LTV for all users is {(9.99 * 0.7) * _0to_1 * (1 + _1to_2 + _1to_2 * _2to_3 + _1to_2 * _2to_3 * _3to_4 + _1to_2 * _2to_3 * _3to_4 * _4to_5 )}')

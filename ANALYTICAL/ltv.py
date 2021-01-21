import pandas as pd


def count_lvt(price, conversions, is_have_trial=True):
    if is_have_trial:
        conversions -= 1
    ltv = price * conversions
    return ltv


DATASET = pd.read_csv('DataScience/data_analytics.csv')
PRICE_PER_PURCHASE = 9.99

subscriber_id_col = list(DATASET['Subscriber ID'])
list_of_unique_clients_id = list(set(subscriber_id_col))
list_of_count_of_conversions = \
    [subscriber_id_col.count(x) for x in list_of_unique_clients_id]
dict_of_count_of_conversions = \
    dict(zip(list_of_unique_clients_id, list_of_count_of_conversions))

# Pseudo code
create new data set for writing ltv and other info.

add to new data set dict_of_count_of_conversions
add to new data set values counted with count_lvt() function
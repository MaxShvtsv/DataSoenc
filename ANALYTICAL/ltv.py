import pandas as pd

# ltv = [1] + [2] + [3] + [4] + [5] =
# = d * c + d * c * 1_to_2 + d * c * 1_to_2 * 2_to_3 + d * c * 1_to_2 * 2_to_3 * 3_to_4 +
# + d * c * 1_to_2 * 2_to_3 * 3_to_4 * 4_to_5 = 
# = d * c * (1 + 1_to_2 + 1_to_2 * 2_to_3 + 1_to_2 * 2_to_3 * 3_to_4 + 1_to_2 * 2_to_3 * 3_to_4 * 4_to_5)
# (we count ltv for one client)
# c = 1, as there is one opportunity to take free trial
# d = price per one perchase
# 1_to_2, 2_to_3, 3_to_4, 4_to_5 = 1 or 0, 1 - if subscibes, 1 as we count only for one subsciber, so
# he/she can buy one license per one week;
# 0 - if he doesn't subscibe.
# resulting ltv formula = d * p, p = count of purchases. <----
# [1] = dev proceeds(d) * conversion to trial(c) 
# [2] = [1] * 1_to_2_purchase
# [3] = [2] * 2_to_3_purchase
# [4] = ...


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
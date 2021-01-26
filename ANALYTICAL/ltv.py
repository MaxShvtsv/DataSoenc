# Collaborators:
# Klots Bohdan, Max Nimchenko, Dima Skorodenko, Alexei Bayda.
# For INT20H

import pandas as pd


def count_lvt(price, type_of_purchase, date_device):
    '''
    Function count LTV for one user.
    price: float, price of purchase.
    type_of_purchase: tuple, tuple of types of purchasing: Free Trial -
    taking trial, nan - purchase.
    date_device: tuple, consists of tuples of date, a device for each date on
    which conversion was done.
    This var created to detect commission on dev. proceeds.
    returns: counted ltv.
    '''
    devices = []

    for el in date_device:
        devices.append(el[1])
    # is_apple_list: list, consists of bool vars:
    # True - if used device is Apple, False - otherwise.
    is_apple_list = [x in APPLE_DEVICE_SET for x in list(devices)]

    if 'Free Trial' in type_of_purchase:
        # Remove first elememt, as Free Trial.
        is_apple_list.pop(0)

    # In case user have used different devices(not Apple), so
    # calculate LTV without commission.
    ltv = price * (1 * is_apple_list.count(False) + 0.7 * is_apple_list.count(True))
    return ltv


# APPLE_DEVICE_SET: set of Apple devices to detec commission.
APPLE_DEVICE_SET = {'iPhone', 'iPad'}
DATA_FRAME = pd.read_csv('data_analytics.csv')
PRICE_PER_PURCHASE = 9.99

subscriber_id_col = list(DATA_FRAME['Subscriber ID'])
device_col = list(DATA_FRAME['Device'])
list_of_unique_clients_id = list(set(subscriber_id_col))

# Creating dict with dates of purchasing and free trial.
date_dict = {}
trial_dict = {}

for user_id in list_of_unique_clients_id:
    # Detect for each date used device to calculate commission.
    dates = list((DATA_FRAME[lambda x: x['Subscriber ID'] == user_id])['Event Date'])
    devices = list((DATA_FRAME[lambda x: x['Subscriber ID'] == user_id])['Device'])
    feature_tuple = []
    for i in range(len(dates)):
        one_tuple = tuple([dates[i], devices[i]])
        feature_tuple.append(one_tuple)
    date_dict[user_id] = tuple(feature_tuple)

    # For detections of first week as trial.
    trial_dict[user_id] = \
        tuple((DATA_FRAME[lambda x: x['Subscriber ID'] == user_id])['Subscription Offer Type'])

# Creating dict of counted LTV for each user.
dict_of_ltv = {}
for user_id in list_of_unique_clients_id:
    dict_of_ltv[user_id] = \
        count_lvt(PRICE_PER_PURCHASE, trial_dict[user_id], date_dict[user_id])

total_ltv = sum(dict_of_ltv.values())  # <- LTV for all users.
print(f'Total LTV among users: {round(total_ltv, 3)}')
mean_ltv = total_ltv / len(list_of_unique_clients_id)  # <- Average of LTV among users.
print(f'Average LTV among users: {round(mean_ltv, 3)}')

from collections import OrderedDict
from datetime import timedelta
from datetime import datetime
import random

# dict_1 = {'Gaurav': 27, 'Shyam': 25, 'Sreeram': 24, 'DD': 32}
# dict_2 = {'Gaurav': 23, 'Shyam': 24, 'Sreeram': 25, 'DD': 31}
# dict_3 = {'GauravS': 21, 'ShyamS': 22, 'SreeramS': 64, 'DDS': 35}
# dict_4 = {'GauravS': 25, 'ShyamS': 35, 'SreeramS': 56, 'DDS': 23, 'Ram':53, 'Manu':54}
# dict_5 = {'GauravS': 54, 'ShyamS': 24, 'SreeramS': 34, 'DDS': 45, 'Ram':23, 'Manu':23}

dict_1 = OrderedDict([('2016-09-19T00:00:00.000Z', 1.0), ('2016-09-20T00:00:00.000Z', 2.0), ('2016-09-21T00:00:00.000Z', 7.0), ('2016-09-22T00:00:00.000Z', 8.0), ('2016-09-23T00:00:00.000Z', 2.0)])
dict_2 = OrderedDict([('2016-09-19T00:00:00.000Z', 8.0), ('2016-09-20T00:00:00.000Z', 8.0), ('2016-09-21T00:00:00.000Z', 5.0), ('2016-09-22T00:00:00.000Z', 4.0), ('2016-09-23T00:00:00.000Z', 1.0)])
dict_3 = OrderedDict([('2016-09-19T00:00:00.000Z', 6.0), ('2016-09-20T00:00:00.000Z', 7.0), ('2016-09-21T00:00:00.000Z', 6.0), ('2016-09-22T00:00:00.000Z', 6.0), ('2016-09-23T00:00:00.000Z', 5.0)])
dict_4 = OrderedDict([('2016-09-18T00:00:00.000Z', 4.0), ('2016-09-19T00:00:00.000Z', 1.0), ('2016-09-20T00:00:00.000Z', 2.0), ('2016-09-21T00:00:00.000Z', 1.0), ('2016-09-22T00:00:00.000Z', 3.0), ('2016-09-23T00:00:00.000Z', 6.0), ('2016-09-24T00:00:00.000Z', 6.0)])

dict_5 = OrderedDict([('2016-09-11T00:00:00.000Z', 3.0), ('2016-09-12T00:00:00.000Z', 4.0), ('2016-09-13T00:00:00.000Z', 1.0), ('2016-09-14T00:00:00.000Z', 2.0), ('2016-09-15T00:00:00.000Z', 6.0), ('2016-09-16T00:00:00.000Z', 4.0), ('2016-09-17T00:00:00.000Z', 4.0)])
dict_6 = OrderedDict([('2016-09-11T00:00:00.000Z', 5.0), ('2016-09-12T00:00:00.000Z', 2.0), ('2016-09-13T00:00:00.000Z', 3.0), ('2016-09-14T00:00:00.000Z', 2.0), ('2016-09-15T00:00:00.000Z', 1.0), ('2016-09-16T00:00:00.000Z', 2.0), ('2016-09-17T00:00:00.000Z', 5.0)])
dict_7 = OrderedDict([('2016-09-12T00:00:00.000Z', 1.0), ('2016-09-13T00:00:00.000Z', 5.0), ('2016-09-14T00:00:00.000Z', 3.0), ('2016-09-15T00:00:00.000Z', 2.0), ('2016-09-16T00:00:00.000Z', 1.0)])


verify_expected_dct = {'UX':
                           {'2016-09-18T00:00:00.000Z': [dict_1.copy(), dict_2.copy(), dict_3.copy(), dict_4.copy()],
                             '2016-09-11T00:00:00.000Z': [dict_5, dict_6, dict_7]
                              }
                       }

# # week = [dict_1.copy(), dict_2.copy(), dict_3.copy(), dict_4.copy()]
#
# OUTPUT = {}
#
# for index, dict in enumerate(week):
#
#     current_dict = dict
#     next_dict = week[index+1]
#
#     for key in current_dict:
#         if key in next_dict:
#             next_dict[key] += current_dict[key]
#         else:
#             next_dict[key] = current_dict[key]
#
#     print('\n', next_dict)
#     print('===', dict_4)
#
#     if index == (len(week) - 2):
#         break

def aggregate(current_dict, next_dict):
    for key in current_dict:
        if key in next_dict:
            next_dict[key] += current_dict[key]
        else:
            next_dict[key] = current_dict[key]
    return next_dict



from functools import reduce

# for category in verify_expected_dct:
#     for week_timesheets in verify_expected_dct[category]:
#         verify_expected_dct[category][week_timesheets] = reduce(aggregate, verify_expected_dct[category][week_timesheets])
#
# print(verify_expected_dct)

# for category in verify_expected_dct:
#     for week_timesheets in verify_expected_dct[category]:
#         verify_expected_dct[category][week_timesheets] = reduce(aggregate, verify_expected_dct[category][week_timesheets])

def func(category):
    for week_timesheets in verify_expected_dct[category]:
        verify_expected_dct[category][week_timesheets] = reduce(aggregate, verify_expected_dct[category][week_timesheets])

map(func, verify_expected_dct.keys())



print(verify_expected_dct)


# def date_formatter(date):
#     return str(date).split(' ')[0] + 'T00:00:00.000Z'
#
#
# def construct_time_sheet_dict(day, week_start, num_artifacts):
#     dict_time_sheet = {}
#     date = week_start + timedelta(day)
#     date = date_formatter(date)
#     time_range = 24 // num_artifacts
#     hours = float(random.randint(1, time_range))
#     dict_time_sheet[date] = hours
#     return dict_time_sheet
#
#
# def get_week_start_datetime(no_week=1):
#     current_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
#     day_of_week = current_date.isocalendar()[2]
#     if day_of_week == 7:
#         start_date = current_date
#     else:
#         start_date = current_date - timedelta(day_of_week)
#     week_start = start_date - timedelta(7) * no_week
#     return week_start
#
#
# def get_time_sheet_values(no_week=1, num_artifacts=3, include_weekend=False):
#     week_start = get_week_start_datetime(no_week)
#     dict_time_sheet = OrderedDict()
#     if include_weekend:
#         for i in range(0, 7):
#             dict_time_sheet.update(construct_time_sheet_dict(i, week_start, num_artifacts))
#     else:
#         for i in range(1, 6):
#             dict_time_sheet.update(construct_time_sheet_dict(i, week_start, num_artifacts))
#     return dict_time_sheet

# print(get_time_sheet_values(2, num_artifacts=4, include_weekend=True))
# print(get_time_sheet_values(2, num_artifacts=4))
# print(get_time_sheet_values(1, num_artifacts=4, include_weekend=True))
# print(get_time_sheet_values(1, num_artifacts=4))



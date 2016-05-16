import datetime

def data_calc(dict_date):
    for key in dict_date:
        d = datetime.datetime.today()
        div = dict_date[key] - d
        years = int(div.days) // 365
        days = int(div.days) % 365
        time = (str(div)).split()[2:]
        list_time = time[0].split(':')
        print(key, ": %sг. %sд. %sч. %sм." % (str(years), str(days), list_time[0], list_time[1]))

dict_of_date = {"Маме": datetime.datetime(2016, 6, 16, 0, 0, 0, 0),
                "Папе": datetime.datetime(2017, 10, 4, 0, 0, 0, 0),
                "Кате": datetime.datetime(2017, 10, 5, 8, 0, 0, 0),
                "Новый год": datetime.datetime(2017, 1, 1, 0, 0, 0)}

dr_dict = {"Маме": datetime.datetime(2016, 6, 15, 0, 0, 0, 0),
           "Папе": datetime.datetime(2016, 10, 4, 0, 0, 0, 0),
           "Кате": datetime.datetime(2017, 1, 21, 0, 0, 0, 0),
           "Паше": datetime.datetime(2016, 8, 26, 0, 0, 0, 0),
           "Юле": datetime.datetime(2017, 2, 24, 0, 0, 0, 0),
           "Вите": datetime.datetime(2016, 6, 15, 0, 0, 0, 0),
           'Ване': datetime.datetime(2016, 10, 5, 0, 0, 0, 0)
           }


print("Осталось ждать: ")
data_calc(dict_of_date)
print('Д.Р.:')
data_calc(dr_dict)

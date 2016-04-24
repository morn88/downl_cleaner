import datetime

dict_of_date = {"Маме": datetime.datetime(2016, 5, 16, 0, 0, 0, 0),
                "Папе": datetime.datetime(2017, 10, 4, 0, 0, 0, 0),
                "Кате": datetime.datetime(2017, 10, 5, 8, 0, 0, 0)}

for key in dict_of_date:
    d = datetime.datetime.today()
    div = dict_of_date[key] - d
    years = int(div.days) // 365
    days = int(div.days) % 365
    time = (str(div)).split()[2:]
    list_time = time[0].split(':')
    print("Осталось ждать: ")
    print(key, ": %sг. %sд. %sч. %sм." % (str(years), str(days), list_time[0], list_time[1]))

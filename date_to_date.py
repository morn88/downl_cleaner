import datetime

class Person:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def data_calc(self):
        d = datetime.datetime.today()
        div = self.date - d
        years = int(div.days) // 365
        days = int(div.days) % 365
        time = (str(div)).split()[2:]
        list_time = time[0].split(':')
        return str(years), str(days), list_time[0], list_time[1]

    def __str__(self):
        return self.name + ": %sг. %sд. %sч. %sм." % (self.data_calc())

if __name__ == '__main__':

    print("Осталось ждать: ")
    mom = Person('Мама', datetime.datetime(2017, 6, 15, 0, 0, 0, 0))
    dad = Person('Папа', datetime.datetime(2017, 10, 4, 0, 0, 0, 0))
    sister = Person('Катя', datetime.datetime(2017, 10, 5, 8, 0, 0, 0))
    wife = Person('Юля', datetime.datetime(2017, 2, 24, 0, 0, 0, 0))
    zjat = Person('Витя', datetime.datetime(2017, 6, 15, 0, 0, 0, 0))
    nephew = Person('Ваня', datetime.datetime(2016, 10, 5, 0, 0, 0, 0))
    iam = Person('Паша', datetime.datetime(2016, 8, 26, 0, 0, 0, 0))
    new_year = Person('Новый год', datetime.datetime(2017, 1, 1, 0, 0, 0))

    print(dad)
    print(sister)
    print(new_year)

    print('Д.Р.:')
    dad.date = datetime.datetime(2016, 10, 4, 0, 0, 0, 0)
    sister.date = datetime.datetime(2017, 1, 21, 0, 0, 0, 0)

    print(mom)
    print(dad)
    print(sister)
    print(wife)
    print(zjat)
    print(nephew)
    print(iam)
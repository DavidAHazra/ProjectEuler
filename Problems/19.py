import datetime


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


print(len([single_date for single_date in date_range(datetime.date(1901, 1, 1), datetime.date(2000, 12, 31)) if
           single_date.day == 1 and single_date.isoweekday() == 7]))

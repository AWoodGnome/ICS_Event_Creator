import datetime

def monthlen():
    da = datetime.date
    delta = datetime.timedelta
    dt = datetime.date.today()
    year = dt.year
    month = dt.month+1
    if month > 12:
        month = 1
        year += 1
    mon = month
    yr = year
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    lastDay = ((da(year, month, 1)-delta(days = 1)).day)
    return yr, mon, lastDay
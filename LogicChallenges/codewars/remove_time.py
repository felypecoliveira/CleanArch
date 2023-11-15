def shorten_to_date(long_date):
    long_date = long_date.replace(",", "")
    long_date = long_date.split()
    long_date.pop(3)
    long_date = ' '.join(long_date)

    return long_date

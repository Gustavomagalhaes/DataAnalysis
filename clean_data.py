from datetime import datetime as dt

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')
        
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

    
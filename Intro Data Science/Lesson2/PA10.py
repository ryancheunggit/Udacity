import pandas

def time_to_hour(time):
    '''
    Given an input variable time that represents time in the format of:
    "00:00:00" (hour:minutes:seconds)

    Write a function to extract the hour part from the input variable time
    and return it as an integer. For example:
        1) if hour is 00, your code should return 0
        2) if hour is 01, your code should return 1
        3) if hour is 21, your code should return 21

    Please return hour as an integer.
    '''

    hour = time.split(":")[0]
    if hour.startswith('0'):
        hour = hour[1:]
    return int(hour)

    # return pandas.to_datetime(time).hour

class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second
    """
def print_time(time):
    return('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

def is_after(t1, t2):
    return t2.hour < t1.hour or (t2.hour == t1.hour and t2.minute < t1.minute) or ((t2.hour == t1.hour and t2.minute == t1.minute and t2.second < t1.second))
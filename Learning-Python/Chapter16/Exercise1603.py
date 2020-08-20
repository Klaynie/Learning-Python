class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second
    """

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

def increment(time, seconds):
    time.second += seconds
    additionalMinutes, time.second = divmod(time.second, 60)
    time.minute += additionalMinutes
    additionalHours, time.minute = divmod(time.minute, 60)
    time.hour += additionalHours

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

increment(start, 86461)

print_time(start)
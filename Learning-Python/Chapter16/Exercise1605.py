class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second
    """

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

def time_to_int(time):
    return time.hour *60*60 + time.minute *60 + time.second

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def increment(time, seconds):
    return int_to_time(time_to_int(time) + seconds)

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

newTime = increment(start, 86461)

print_time(start)
print_time(newTime)
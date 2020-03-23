class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second
    """

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

def increment(time, seconds):
    newTime = Time()
    newTime.second = time.second + seconds
    additionalMinutes, newTime.second = divmod(newTime.second, 60)
    newTime.minute = time.minute + additionalMinutes
    additionalHours, newTime.minute = divmod(newTime.minute, 60)
    newTime.hour = time.hour + additionalHours
    return newTime

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

newTime = increment(start, 86461)

print_time(start)
print_time(newTime)
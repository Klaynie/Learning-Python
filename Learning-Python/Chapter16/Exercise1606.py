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

def mul_time(time, multiplicator):
    return int_to_time(time_to_int(time) * multiplicator)

def average_time_per_lap(time, numberOfLaps):
    return mul_time(time, 1/numberOfLaps)

time = Time()
time.hour = 1
time.minute = 15
time.second = 45

numberOfLaps = 3

print_time(average_time_per_lap(time, numberOfLaps))
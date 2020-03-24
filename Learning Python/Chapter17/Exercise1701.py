class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second
    """
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        return self.hour *60*60 + self.minute *60 + self.second

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

time = Time()
time.hour = 1
time.minute = 15
time.second = 45

print(time.time_to_int())
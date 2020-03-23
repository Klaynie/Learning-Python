import datetime
import math
import copy

def weekday_of_today():
    timestamp = datetime.datetime.utcnow()
    return timestamp.weekday()

def age_from_birthday(birthday):
    delta = datetime.datetime.utcnow() - birthday
    ageYears = int(math.floor(delta.days / 365.2425))
    return ageYears

def age_until_date(birthday, date):
    delta = date - birthday + datetime.timedelta(days = 1)
    ageYears = int(math.floor(delta.days / 365.2525))
    return ageYears

def time_until_date(date):
    time = date - datetime.datetime.utcnow()
    return time

def get_time_to_next_birthday(currentTimestamp, birthday):
    if birthday.month <= currentTimestamp.month and (birthday.month <= currentTimestamp.month and birthday.day <= currentTimestamp.day):
        return time_until_date(datetime.datetime(currentTimestamp.year+1, birthday.month, birthday.day))
    else:
        return time_until_date(datetime.datetime(currentTimestamp.year, birthday.month, birthday.day))

def print_age_and_time_to_next_birthday(birthday):
    currentTimestamp = datetime.datetime.utcnow()
    print('You are %g years old. Time to next birthday: %s' % (age_from_birthday(birthday), get_time_to_next_birthday(currentTimestamp, birthday)))

def find_double_date(birthday1, birthday2, n):
    if birthday2 > birthday1:
        i = 0
        newDate = copy.deepcopy(birthday2)
        nextDay = newDate + datetime.timedelta(days = i)
        while age_until_date(birthday1, nextDay) != age_until_date(birthday2, nextDay)*n:
            nextDay = newDate + datetime.timedelta(days = i)
            i += 1
        print(nextDay, age_until_date(birthday1, nextDay),age_until_date(birthday2, nextDay))
    else:
        i = 0
        newDate = copy.deepcopy(birthday1)
        nextDay = newDate + datetime.timedelta(days = i)
        while age_until_date(birthday2, nextDay) != age_until_date(birthday1, nextDay)*n:
            nextDay = newDate + datetime.timedelta(days = i)
            i += 1
        print(nextDay, age_until_date(birthday1, nextDay),age_until_date(birthday2, nextDay))

#birthday = datetime.datetime(1986,11,8)

#print_age_and_time_to_next_birthday(birthday)

birthday1 = datetime.datetime(2000,11,15)
birthday2 = datetime.datetime(1986,7,5)

find_double_date(birthday1, birthday2, 4)
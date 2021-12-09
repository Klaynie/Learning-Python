import datetime
import math
import copy

def get_timestamp():
    print(datetime.datetime.utcnow())
    return datetime.datetime.utcnow()

def weekday_of_today():
    timestamp = get_timestamp()
    return timestamp.weekday()

def calculate_age_between_two_dates(date1, date2):
    return date2.year - date1.year - int(((date2.month, date2.day) < (date1.month, date1.day)))

def current_age_from_birthday(birthday):
    return calculate_age_between_two_dates(birthday, get_timestamp())

def age_until_date(birthday, date):
    return calculate_age_between_two_dates(birthday, date)

def time_until_date(date, timestamp):
    return date - timestamp

def get_time_to_next_birthday(birthday, currentTimestamp):
    if has_birthday_next_year(birthday, currentTimestamp):
        return time_until_date(datetime.datetime(currentTimestamp.year, birthday.month, birthday.day), currentTimestamp)
    else:
        return time_until_date(datetime.datetime(currentTimestamp.year + 1, birthday.month, birthday.day), currentTimestamp)

def has_birthday_next_year(birthday, currentTimestamp):
    result = True
    if birthday.month < currentTimestamp.month:
        result = False
    else:
        if birthday.day < currentTimestamp.day:
            result = False
    return result

def has_birthday(birthday, currentTimestamp):
    result = False
    if birthday.month == currentTimestamp.month:
        if birthday.day == currentTimestamp.day:
            result = True
    return result

def print_age_and_time_to_next_birthday(birthday):
    currentTimestamp = get_timestamp()
    if has_birthday(birthday, currentTimestamp):
        print('You turn %g years old today. Happy Birthday! 🎉' % (current_age_from_birthday(birthday)))
    else:
        print('You are %g years old. Time to next birthday: %s' % (current_age_from_birthday(birthday), get_time_to_next_birthday(birthday, currentTimestamp)))

def find_older_date(date1, date2):
    if date2 > date1:
        return date1, date2
    else:
        return date2, date1

def find_double_date(birthday1, birthday2, n):
    olderBirthday, youngerBirthday = find_older_date(birthday1, birthday2)
    nextDayCounter = 0
    nextDay = copy.deepcopy(youngerBirthday)
    while age_until_date(olderBirthday, nextDay) != age_until_date(youngerBirthday, nextDay)*n:
        nextDay += datetime.timedelta(days = 1)
        nextDayCounter += 1
    print(nextDay, age_until_date(olderBirthday, nextDay), age_until_date(youngerBirthday, nextDay))

birthday1 = datetime.datetime(2000,12,9)
birthday2 = datetime.datetime(1977,2,2)

print_age_and_time_to_next_birthday(birthday1)
find_double_date(birthday1, birthday2, 3)
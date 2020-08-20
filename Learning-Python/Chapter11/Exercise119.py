import random
import datetime

def has_duplicates_dict(t):
    d = dict()
    for c in t:
        if c in d:
            return True
        else:
            d[c] = 1
    return False

def has_duplicates(t):
    i = 0
    j = 1
    while i < len(t):
        while j < len(t):
           if t[i] == t[j]:
               return True
           j += 1
        i += 1
        j = i + 1
    return False

def create_random_int_list(length):
    i = 0
    t = []
    while i < length:
        t.insert(i, random.randint(1, 1000000))
        i += 1
    return t

t = create_random_int_list(10000)

def test_function_duration(f, g, n):
    i = 1
    while i <= n:
        j = 1
        total_duration_1 = 0
        total_duration_2 = 0
        while j <= 1000:
            t = create_random_int_list(100)
            timestamp_begin_1 = datetime.datetime.now()
            f(t)
            timestamp_end_1 = datetime.datetime.now()
            duration_1 = timestamp_end_1 - timestamp_begin_1
            total_duration_1 += duration_1.microseconds
            average_duration_1 = round(total_duration_1/j,0)
            
            timestamp_begin_2 = datetime.datetime.now()
            g(t)
            timestamp_end_2 = datetime.datetime.now()
            duration_2 = timestamp_end_2 - timestamp_begin_2
            total_duration_2 += duration_2.microseconds
            average_duration_2 = round(total_duration_2/j,0)
            
            j += 1
        print(i, average_duration_1, average_duration_2)
        i +=1

test_function_duration(has_duplicates, has_duplicates_dict, 1000)# With 50 we get 985 ms for has_duplicates and 17 ms for has_duplicates_dict
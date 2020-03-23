import datetime
known = {0:0, 1:1}

def fibonacci_known(n):
    global known
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def test_function_duration(f, n):
    i = 1
    while i <= n:
        j = 1
        total_duration = 0
        while j <= 10:
            timestamp_begin = datetime.datetime.now()
            f(i)
            timestamp_end = datetime.datetime.now()
            duration = timestamp_end - timestamp_begin
            total_duration += duration.microseconds
            average_duration = round(total_duration/j,0)
            j += 1
        print(i, average_duration)
        i +=1     

#print(test_function_duration(fibonacci, 100))

test_function_duration(fibonacci_known, 34)
import datetime
known = {}

def ack(m,n):
    global known
    key = str(m) + ', ' + str(n)
    if key in known:
        return known[key]
    if m == 0:
       return n + 1
    if n == 0:
       return ack(m-1,1)
    return ack(m-1,ack(m, n-1))

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
        
def build_ackerman():
    global known
    m = 0
    while m <= 4:
        n = 0
        while n <= 5:
            key = str(m) + ', ' + str(n)
            known[key] = ack(m,n)
            n += 1
        m += 1 
        print(known)
        
print(build_ackerman()) #Maximum is ack(3,5)
#print(ack(3,5)) Maximum is ack(3,5)
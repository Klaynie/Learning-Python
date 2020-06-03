def sq_sum(*numbers):
    result = 0
    for number in numbers:
        result += number ** 2
    return float(result)
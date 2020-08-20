def cummulative_sum(t):
    res = []
    i = 0
    for s in t:
        i += s
        res.append(i)
    return res

inputList = [1,2,3]

print(cummulative_sum(inputList))
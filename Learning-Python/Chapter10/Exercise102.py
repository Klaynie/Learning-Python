def capitalize_nested(t):
    res = []
    i = 0
    for s in t:
        if type(s) == list:
           res.insert(i,capitalize_nested(s))
        if type(s) == str:
           res.insert(i, s.capitalize()) 
        i += 1
    return res

t = ['this',['is','sparta'],['d',['Life','of','pi',['morituri','te','salutant']]]]

print(capitalize_nested(t))
def is_between(x, y, z):
    if x > y:
        return False
    if x <= y:
        if y <= z:
           return True
        else: 
           return False
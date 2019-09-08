def gcd(a,b):
    if b==0:
        return a
    if a<b:
        bigger_number = b
        smaller_number = a
    if a>b:
        bigger_number = a
        smaller_number = b
    if a==b:
        return a
    remainder = bigger_number%smaller_number
    return gcd(smaller_number,remainder)

print(gcd(39,13))
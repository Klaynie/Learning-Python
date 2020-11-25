def prime_factorisation(number):
    result = list()
    divisor = 2
    while (divisor <= number):
        if number % divisor == 0:
            result.append(divisor)
            number /= divisor
        else:
            divisor += 1
    return result


number = int(input("Enter a number: "))
print(prime_factorisation(number))
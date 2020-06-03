def final_deposit_amount(*interest, amount=1000):
    for number in interest:
        amount *= (1 + number / 100)
    return round(amount, 2)

print(final_deposit_amount(5, 7, 4))
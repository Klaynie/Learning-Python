def find_tax_group(income):
    if income <= 15527:
        return 0
    elif income <= 42707:
        return 0.15
    elif income <= 132406:
        return 0.25
    else:
        return 0.28

income = int(input())
tax_group = find_tax_group(income)
tax = income * tax_group
print(f"The tax for {income} is {tax_group:.0%}. That is {tax:.0f} dollars!")
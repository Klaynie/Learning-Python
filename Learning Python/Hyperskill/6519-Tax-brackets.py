def find_tax_group(income):
    if income <= 15527:
        return 0
    if income <= 42707:
        return 0.15
    if income <= 132406:
        return 0.25
    return 0.28

income_value = int(input())
tax_group = find_tax_group(income_value)
tax = income_value * tax_group
print(f"The tax for {income_value} is {tax_group:.0%}. That is {tax:.0f} dollars!")
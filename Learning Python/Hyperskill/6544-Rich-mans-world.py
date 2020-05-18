"""
When a bank has financial problems the government can return a client's deposit if it is less than 700,000. The interest rate for a particular deposit is 7,1% a year. The percentages are paid to the same deposit at the end of the year and a new value of the interest is calculated.

Find out how many years it will take for the sum of the deposit to exceed the value protected by the government. 

The input format:

The initial sum of the deposit. It is guaranteed that the value will be between 50,000 and 700,000.

The output format:

The number of years.

Sample Input 1:

650000

Sample Output 1:

2
"""

initial_investment_amount = float(input())
maximum_protected_amount = 700000
year_counter = 0
interest_rate = 7.1
while initial_investment_amount < maximum_protected_amount:
    initial_investment_amount *= (1 + interest_rate / 100)
    year_counter += 1

print(year_counter)
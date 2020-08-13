"""
In the very first year, there are 120120120 frogs in the marsh. Once a year, 505050 frogs move to a nearby pond, while the remaining frogs breed so that their number doubles. Thus, for year kkk, you can calculate the number of frogs in the marsh based on the formula:

Fk=2(Fk−1−50)F_k = 2(F_{k-1} - 50)Fk​=2(Fk−1​−50)

Write a function number_of_frogs that returns this number for a given year.

Just implement the function, you don't have to handle input or print anything.
"""

def number_of_frogs(year):
    if year == 1:
        return 120
    else:
        return 2 * (number_of_frogs(year - 1) - 50)

print(number_of_frogs(5))
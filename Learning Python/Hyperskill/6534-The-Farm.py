"""
In a farming game, you can buy certain animals for a specific price. As a player, you want to buy the most useful (i.e. the most expensive) animal. Here are the animals and their prices:

Item: Price
Chicken: 23
Goat: 678
Pig: 1296
Cow: 3848
Sheep: 6769

Write a program that determines what is the most expensive animal that the user can buy with their money and how many of them they can buy.

The input format:
The money that the user has.

The output format:
How many animals the user can afford, for example, 20 chickens or 4 cows. If the user cannot afford any animal, write None. 

Pay attention to the number of nouns. Also, keep in mind that the word "sheep" has the irregular plural form "sheep".

Sample Input 1:
25

Sample Output 1:
1 chicken

Sample Input 2:
8

Sample Output 2:
None

Sample Input 3:
668

Sample Output 3:
29 chickens
"""
chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

user_money = int(input())

if user_money < chicken:
    print("None")
elif user_money >= chicken and user_money < goat:
    if user_money // chicken == 1:
        print(user_money // chicken, "chicken")
    elif user_money // chicken > 1:
        print(user_money // chicken, "chickens")
elif user_money >= goat and user_money < cow:
    if user_money // goat == 1:
        print(user_money // goat, "goat")
    elif user_money // goat > 1:
        print(user_money // goat, "goats")
elif user_money >= pig and user_money < cow:
    if user_money // pig == 1:
        print(user_money // pig, "pig")
    elif user_money // pig > 1:
        print(user_money // pig, "pigs")
if user_money >= cow and user_money < sheep:
    if user_money // cow == 1:
        print(user_money // cow, "cow")
    elif user_money // cow > 1:
        print(user_money // cow, "cows")
elif user_money > sheep:
    print(user_money // sheep, "sheep")
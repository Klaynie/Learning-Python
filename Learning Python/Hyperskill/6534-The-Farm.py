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

money = int(input())

if money < chicken:
    print("None")
elif money < goat:
    n_chicken = money // chicken
    print(n_chicken, ("chicken" if n_chicken == 1 else "chickens"))
elif money < pig:
    n_goat = money // goat
    print(n_goat, ("goat" if n_goat == 1 else "goats"))
elif money < cow:
    n_pig = money // pig
    print(n_pig, ("pig" if n_pig == 1 else "pigs"))
elif money < sheep:
    n_cow = money // cow
    print(n_cow, ("cow" if n_cow == 1 else "cows"))
elif money >= sheep:
    n_sheep = money // sheep
    print(n_sheep, "sheep")
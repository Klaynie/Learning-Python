# Write your code here
user_prompts = [    "Write how many cups of coffee you will need:",
                    "Write how many ml of water the coffee machine has:",
                    "Write how many ml of milk the coffee machine has:",
                    "Write how many grams of coffee beans the coffee machine has:"]
output_messages = [ "Starting to make a coffee",
                    "Grinding coffee beans",
                    "Boiling water",
                    "Mixing boiled water with crushed coffee beans",
                    "Pouring coffee into the cup",
                    "Pouring some milk into the cup",
                    "Coffee is ready!"]
ingredient_amount = [200, 50, 15]

def print_ingredient_messages(cups_of_coffee, amount_water, amount_milk, amount_coffee_beans):
    print(f"For {cups_of_coffee} cups of coffee you will need:")
    print(f"{amount_water} ml of water")
    print(f"{amount_milk} ml of milk")
    print(f"{amount_coffee_beans} g of coffee beans")

def calculate_amount_of_cups_capacity(capacity_water, capacity_milk, capacity_coffee_beans):
    capacity = [capacity_water, capacity_milk, capacity_coffee_beans]
    for i in range(len(ingredient_amount)):
        capacity[i] = capacity[i] // ingredient_amount[i]
    return min(capacity)

def check_coffee_amount(cups_of_coffee, capacity):
    if capacity == cups_of_coffee:
        print("Yes, I can make that amount of coffee")
    elif capacity < cups_of_coffee:
        print(f"No, I can make only {capacity} cups of coffee")
    elif capacity > cups_of_coffee:
        print(f"Yes, I can make that amount of coffee (and even {capacity - cups_of_coffee} more than that)")
def calculate_ingredient_amount(cups_of_coffee):
    return cups_of_coffee * ingredient_amount[0], cups_of_coffee * ingredient_amount[1], cups_of_coffee * ingredient_amount[2]

#amount_water, amount_milk, amount_coffee_beans = calculate_ingredient_amount(cups_of_coffee)
#print_ingredient_messages(cups_of_coffee, amount_water, amount_milk, amount_coffee_beans)

capacity_water, capacity_milk, capacity_coffee_beans = int(input(user_prompts[1])), int(input(user_prompts[2])), int(input(user_prompts[3]))
cups_of_coffee = int(input(user_prompts[0]))
capacity = calculate_amount_of_cups_capacity(capacity_water, capacity_milk, capacity_coffee_beans)
check_coffee_amount(cups_of_coffee, capacity)
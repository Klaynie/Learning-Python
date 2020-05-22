# Write your code here
user_prompts = [    "Write how many cups of coffee you will need:",
                    "Write how many ml of water the coffee machine has:",
                    "Write how many ml of milk the coffee machine has:",
                    "Write how many grams of coffee beans the coffee machine has:",
                    "Write action (buy, fill, take, remaining, exit):",
                    "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:",
                    "Write how many cups of coffee you will need:",
                    "Write how many ml of water do you want to add:",
                    "Write how many ml of milk do you want to add:",
                    "Write how many grams of coffee beans do you want to add:",
                    "Write how many disposable cups of coffee do you want to add:"]
output_messages = [ "Starting to make a coffee",
                    "Grinding coffee beans",
                    "Boiling water",
                    "Mixing boiled water with crushed coffee beans",
                    "Pouring coffee into the cup",
                    "Pouring some milk into the cup",
                    "Coffee is ready!"]
actions = ["buy", "fill", "take", "remaining", "exit"]
buy_actions = ["back"]
buy_messages = ["I have enough resources, making you a coffee!", 
                "Sorry, not enough water!",
                "Sorry, not enough milk!",
                "Sorry, not enough coffee beans!",
                "Sorry, not enough disposable cups"]
coffee_machine_messages = [ "The coffee machine has",
                            "{} of water",
                            "{} of milk",
                            "{} of coffee beans",
                            "{} of disposable cups",
                            "${} of money"]                
coffee_machine_capacity = [550, 400, 540, 120, 9]
ingredient_amount = [200, 50, 15]
menu = [['espresso',[4, 250, 0, 16, 1]], ['latte',[7, 350, 75, 20, 1]], ['cappucino',[6, 200, 100, 12, 1]]]
keep_going = True

def print_coffee_machine_content():
    global coffee_machine_capacity
    for i in range(len(coffee_machine_capacity)):
        if i == 0:
            print(coffee_machine_messages[i])
        else:
            print(coffee_machine_messages[i].format(coffee_machine_capacity[i]))
    print(f"${coffee_machine_capacity[0]} of money")

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

def action_to_prompt(action):
    global coffee_machine_capacity
    if action == actions[0]:
        action_buy()
    elif action == actions[1]:
        action_fill()
    elif action == actions[2]:
        action_take()
    elif action == actions[3]:
        print_coffee_machine_content()
    elif action == actions[4]:
        action_exit()

def check_capcity(menu_number):
    capacity_delta = get_capacity_delta(menu_number)
    for i in range(1, len(coffee_machine_capacity)):
        if coffee_machine_capacity[i] - capacity_delta[i] < 0:
            print(buy_messages[i])
            return False
    return True

def get_capacity_delta(menu_number):
    return menu[menu_number - 1][1]

def buy_item(menu_number):
    capacity_delta = get_capacity_delta(menu_number)
    for i in range(len(coffee_machine_capacity)):
        if i == 0:
            coffee_machine_capacity[i] += capacity_delta[i]
        else:
            coffee_machine_capacity[i] -= capacity_delta[i]

def action_buy():
    buy_action = input(user_prompts[5])
    if buy_action == buy_actions[0]:
        return None
    else:
        menu_number = int(buy_action)
        if check_capcity(menu_number):
            print(buy_messages[0])
            buy_item(menu_number)

def action_fill():
    capacity_water =  int(input(user_prompts[7])) 
    capacity_milk = int(input(user_prompts[8]))
    capacity_coffee_beans = int(input(user_prompts[9]))
    capacity_disposable_cups = int(input(user_prompts[10]))
    capacity_delta = [0, capacity_water, capacity_milk, capacity_coffee_beans, capacity_disposable_cups]
    for i in range(len(coffee_machine_capacity)):
        coffee_machine_capacity[i] += capacity_delta[i]

def action_take():
    global coffee_machine_capacity
    take_amount = coffee_machine_capacity[0]
    coffee_machine_capacity[0] = 0
    print(f"I gave you ${take_amount}")

def action_exit():
    global keep_going
    keep_going = False

def coffee_machine_loop():
    global keep_going
    while keep_going:
        action_to_prompt(input(user_prompts[4]))

#amount_water, amount_milk, amount_coffee_beans = calculate_ingredient_amount(cups_of_coffee)
#print_ingredient_messages(cups_of_coffee, amount_water, amount_milk, amount_coffee_beans)

#capacity_water, capacity_milk, capacity_coffee_beans = int(input(user_prompts[1])), int(input(user_prompts[2])), int(input(user_prompts[3]))
#cups_of_coffee = int(input(user_prompts[0]))
#capacity = calculate_amount_of_cups_capacity(capacity_water, capacity_milk, capacity_coffee_beans)
#check_coffee_amount(cups_of_coffee, capacity)

coffee_machine_loop()
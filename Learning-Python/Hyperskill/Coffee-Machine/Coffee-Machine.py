class CoffeeMachine:

    def __init__(self, money, water, milk, beans, cups):
        self.state = "initial"
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups

    def set_state(self, new_state):
        self.state = new_state

    def set_state_initial(self):
        self.set_state(states[0])

    def __str__(self):
        return "The coffee machine has\n" \
                f"{self.water} of water\n" \
                f"{self.milk} of milk\n" \
                f"{self.beans} of coffee beans\n" \
                f"{self.cups} of disposable cups\n" \
                f"${self.money} of money"

    def user_interaction(self):
        if self.state == states[1]:
            self.action_buy()
        elif self.state == states[2]:
            self.action_fill()
        elif self.state == states[3]:
            self.action_take()
        elif self.state == states[4]:
            self.action_remaining()
        elif self.state == states[5]:
            self.action_exit()

    def action_buy(self):
        buy_action = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if buy_action == "back":
            self.set_state_initial()
        else:
            menu_number = int(buy_action)
            if self.check_capcity(menu_number):
                print(buy_messages[0])
                self.buy_item(menu_number)
                self.set_state_initial()

    def action_fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        self.set_state_initial()

    def action_take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        self.set_state_initial()

    def action_remaining(self):
        print(self)
        self.set_state_initial()

    def action_exit(self):
        global keep_going
        keep_going = False

    def check_capcity(self, menu_number):
        capacity_delta = get_capacity_delta(menu_number)
        if self.water - capacity_delta[1] < 0:
                print(buy_messages[1])
                return False
        if self.milk - capacity_delta[2] < 0:
                print(buy_messages[2])
                return False
        if self.beans - capacity_delta[3] < 0:
                print(buy_messages[3])
                return False
        if self.cups - capacity_delta[4] < 0:
                print(buy_messages[4])
                return False
        return True

    def buy_item(self, menu_number):
        capacity_delta = get_capacity_delta(menu_number)
        self.money += capacity_delta[0]
        self.water -= capacity_delta[1]
        self.milk -= capacity_delta[2]
        self.beans -= capacity_delta[3]
        self.cups -= capacity_delta[4]

states = ["initial", "buy", "fill", "take", "remaining", "exit"]
buy_messages = ["I have enough resources, making you a coffee!", 
                "Sorry, not enough water!",
                "Sorry, not enough milk!",
                "Sorry, not enough coffee beans!",
                "Sorry, not enough disposable cups"]
menu = [['espresso',[4, 250, 0, 16, 1]], ['latte',[7, 350, 75, 20, 1]], ['cappucino',[6, 200, 100, 12, 1]]]
keep_going = True

def action_to_prompt(instance, action):
    instance.set_state(action)
    coffee_machine.user_interaction()
    return None

def get_capacity_delta(menu_number):
    return menu[menu_number - 1][1]

def coffee_machine_loop():
    global keep_going
    while keep_going:
        action_to_prompt(coffee_machine, input("Write action (buy, fill, take, remaining, exit):"))

coffee_machine = CoffeeMachine(550, 400, 540, 120, 9)
coffee_machine_loop()
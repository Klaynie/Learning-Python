# Write your code here
user_prompt = ["Write how many cups of coffee you will need:"]
output_messages = [ "Starting to make a coffee",
                    "Grinding coffee beans",
                    "Boiling water",
                    "Mixing boiled water with crushed coffee beans",
                    "Pouring coffee into the cup",
                    "Pouring some milk into the cup",
                    "Coffee is ready!"]
                    
def print_ingredient_messages(cups_of_coffee, amount_water, amount_milk, amount_coffee_beans):
    print(f"For {cups_of_coffee} cups of coffee you will need:")
    print(f"{amount_water} ml of water")
    print(f"{amount_milk} ml of milk")
    print(f"{amount_coffee_beans} g of coffee beans")

def calculate_ingredient_amount(cups_of_coffee):
    return cups_of_coffee * 200, cups_of_coffee * 50, cups_of_coffee * 15

cups_of_coffee = int(input(user_prompt[0]))
amount_water, amount_milk, amount_coffee_beans = calculate_ingredient_amount(cups_of_coffee)
print_ingredient_messages(cups_of_coffee, amount_water, amount_milk, amount_coffee_beans)
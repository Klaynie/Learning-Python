class PiggyBank:

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars, self.cents = to_dollars(to_cents(self.dollars + deposit_dollars, self.cents + deposit_cents))

def to_cents(dollars, cents):
    return (dollars + cents // 100) * 100 + cents % 100

def to_dollars(cents):
    return cents // 100, cents % 100

new_piggy = PiggyBank(0, 50)
new_piggy.add_money(0, 99)

print(new_piggy.dollars, new_piggy.cents)
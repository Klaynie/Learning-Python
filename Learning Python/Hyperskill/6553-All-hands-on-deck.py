hand_value = 0
card_coutner = 0
card_values = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

def sum_card_value(card):
    global hand_value, card_values
    if card.isdigit():
        hand_value += int(card)
    else:
        hand_value += card_values[card]

while card_coutner < 6:
    card = input()
    sum_card_value(card)
    card_coutner += 1

print(hand_value / card_coutner)
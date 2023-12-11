card_deck = {24, 9, 8, 4, 6, 3, 44, 3}
hand = []

while sum(hand) <= 34:
    hand.append(card_deck.pop())
hello = sum(hand)
print(hand, hello)
import random

def build_standard_deck() -> list[dict]:
    ranck = ["A", "2", "3", "4", "5", "6", "7" ,"8" ,"9" ,"10", "J", "Q", "K"]
    suit = ["H", "C", "D", "S"]
    deck = []

    for s in suit:
        for r in ranck:
            deck.append({"rank" : r, "suit" : s})

    return deck


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:

    for i in range(5000):
        while True:
            random_number_1 = random.randint(0, 51)
            random_number_2 = random.randint(0, 51)
            if random_number_1 != random_number_2:

                if deck[random_number_1]["suit"] == "H":
                    if random_number_2 % 5 == 0:
                        deck[random_number_1], deck[random_number_2] = deck[random_number_2], deck[random_number_1]
                        break
                if deck[random_number_1]["suit"] == "C":
                    if random_number_2 % 3 == 0:
                        deck[random_number_1], deck[random_number_2] = deck[random_number_2], deck[random_number_1]
                        break
                if deck[random_number_1]["suit"] == "D":
                    if random_number_2 % 2 == 0:
                        deck[random_number_1], deck[random_number_2] = deck[random_number_2], deck[random_number_1]
                        break
                if deck[random_number_1]["suit"] == "S":
                    if random_number_2 % 7 == 0:
                        deck[random_number_1], deck[random_number_2] = deck[random_number_2], deck[random_number_1]
                        break
    return deck




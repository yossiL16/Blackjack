import random

def build_standard_deck() -> list[dict]:
    ranck = ["A", "2", "3", "4", "5", "6", "7" ,"8" ,"9" ,"10", "J", "Q", "K"]
    suit = ["H", "C", "D", "S"]
    deck = []

    for s in suit:
        for r in ranck:
            deck.append({r : s})

    return deck


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:

    random_number = random.randint(1, 52)




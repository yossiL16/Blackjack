

def calculate_hand_value(hand: list[dict]) -> int:
    hand_value = {"A": 1, "2": 2, "3": 3, "4": 4, "5" : 5, "6" : 6, "7": 7, "8": 8, "9" : 9, "10": 10, "J": 10, "Q":10, "K":10}
    sum_hans = 0
    for i in hand:
        value = i["rank"]
        sum_hans += hand_value[value]
    return sum_hans


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:



def dealer_play(deck: list[dict], dealer: dict) -> bool:
    pass
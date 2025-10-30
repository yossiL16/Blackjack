
def calculate_hand_value(hand: list[dict]) -> int:
    hand_value = {"A": 1, "2": 2, "3": 3, "4": 4, "5" : 5, "6" : 6, "7": 7, "8": 8, "9" : 9, "10": 10, "J": 10, "Q":10, "K":10}
    sum_hans = 0
    for i in hand:
        value = i["rank"]
        sum_hans += hand_value[value]
    return sum_hans


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:

    card1 = deck.pop(0)
    card2 = deck.pop(0)
    card3 = deck.pop(0)
    card4 = deck.pop(0)

    player.update(card1)
    player.update(card2)
    dealer.update(card3)
    dealer.update(card4)

    print(f"hand player: {player}, hand dealer: {dealer}.")


def dealer_play(deck: list[dict], dealer: dict) -> bool:

    sum_diler = calculate_hand_value(dealer["hand"])
    while True:
        if not sum_diler <= 17:
            card1 = deck.pop(0)
            sum_diler += card1
        break
    if sum_diler > 21:
        print("Disqualified")
        return False
    else:
        print("The dealer has finished his turn. ")
        return True


from core.game_logic import calculate_hand_value
from core.game_logic import deal_two_each
from core.game_logic import dealer_play

def ask_player_action() -> str:

    while True:
        value = input("pleas enter H or S: ").upper()
        if value == "S" or value == "H":
            return value
        else:
            print("Invalid input")
            continue

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    while True:
        chois_player = ask_player_action()
        if chois_player == "H":
            card = deck.pop(0)
            player["hand"].append(card)
            sum_player = calculate_hand_value(player["hand"])
            print("player sum:", sum_player)
            if sum_player > 21:
                print("The player is disqualified.")
                print("The dealer won!!!")
                print("The game is over!")
                break
            else:
                continue
        elif chois_player == "S":
            resolt_dealer = dealer_play(deck, dealer)
            if resolt_dealer == False:
                print("The dealer is disqualified.")
                print("The player won!!!")
                print("The game is over!")
                break
            else:
                hand_player = calculate_hand_value(player["hand"])
                hand_dealer = calculate_hand_value(dealer["hand"])
                if hand_player > hand_dealer:
                    print("The dealer won!!!")
                    print("The game is over!")
                    break
                elif hand_player < hand_dealer:
                    print("The player won!!!")
                    print("The game is over!")
                    break
                else:
                    print("Equality")
                    break






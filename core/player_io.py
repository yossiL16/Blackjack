

def ask_player_action() -> str:

    while True:
        value = input("pleas enter H or S: ").upper()
        if value == "S" or value == "H":
            return value
        else:
            print("Invalid input")
            continue

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:

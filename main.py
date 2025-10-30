from core.deck import *
from core.game_logic import *
from core.player_io import *

if __name__ == "__main__":

    deck = build_standard_deck()
    mix_deck = shuffle_by_suit(deck)
    player = {"hand": []}
    dealer  = {"hand": []}
    run_full_game(deck, player, dealer)

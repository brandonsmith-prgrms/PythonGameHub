import pygame

images = {
    "blackjack_background":"",
    "cards":[]
}


class BlackjackUI:
    def __init__(self):
        #state = 0: setting up game options
        #state = 1: running game
        #state = 2: exiting game
        self._state = 0

    def get_game_opts(self) -> None:
        pass

    def __display_game_opts(self) -> None:
        #



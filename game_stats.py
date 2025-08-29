from typing import TYPE_CHECKING
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Main

class Gamestats:

    def __init__(self, game: "Main"):
        self.settings = game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
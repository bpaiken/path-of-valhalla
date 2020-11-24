from character_stats import CharacterStats
from character_gear import CharacterGear

class Character:
    def __init__(self, args):
        self._stats = CharacterStats()
        self._gear = CharacterGear(args['character_gear'])
from models.stat import Stat


class Character:

    def __init__(self, setting: str, name: str, goal: str):
        self.setting = setting
        self.name = name
        self.goal = goal
        self.stats = []

    def add_stat(self, stat: Stat):
        """
        Adds a new stat to the character.
        """
        self.stats.append(stat)

    def get_stat(self, name: str) -> Stat:
        """
        Retrieves a stat by its name.
        :param name: The name of the stat to retrieve
        :return: The Stat object, or None if not found
        """
        for stat in self.stats:
            if stat.name == name:
                return stat
        return None

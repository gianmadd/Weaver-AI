from typing import Optional

from models.stat import Stat


class Character:
    setting: str
    name: str
    goal: str
    stats: list[Stat]

    def __init__(self, setting: str, name: str, goal: str) -> None:
        self.setting = setting
        self.name = name
        self.goal = goal
        self.stats = []

    def add_stat(self, stat: Stat) -> None:
        self.stats.append(stat)

    def get_stat(self, name: str) -> Optional[Stat]:
        for stat in self.stats:
            if stat.name == name:
                return stat
        return None

    def __str__(self) -> str:
        stats_str = ", ".join(str(stat) for stat in self.stats)
        return (
            f"Character: {self.name}, Setting: {self.setting}, Goal: {self.goal}, "
            f"Stats: [{stats_str}]"
        )

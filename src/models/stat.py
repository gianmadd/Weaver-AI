class Stat:
    name: str
    value: int

    def __init__(self, name: str) -> None:
        self.name = name
        self.value = 0  # Default value

    def increment(self, amount: int) -> None:
        self.value += amount

    def decrement(self, amount: int) -> None:
        self.value -= amount

    def __str__(self) -> str:
        return f"Stat: {self.name}, Value: {self.value}"

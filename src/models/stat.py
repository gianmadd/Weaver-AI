class Stat:
    def __init__(self, name: str):
        """
        :param name: The name of the stat (e.g., "Strength")
        """
        self.name = name
        self.value = 5  # Default value

    def increment(self, amount: int):
        """
        Increases the stat value by a given amount.
        """
        self.value += amount

    def decrement(self, amount: int):
        """
        Decreases the stat value by a given amount.
        """
        self.value -=  amount

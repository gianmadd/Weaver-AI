class Choice:

    def __init__(self, choice1: str, choice2: str, selected_choice: str = None):
        """
        :param choice1: The first choice available.
        :param choice2: The second choice available.
        :param selected_choice: The choice selected by the player.
        """
        self.choice1 = choice1
        self.choice2 = choice2
        self.selected_choice = selected_choice

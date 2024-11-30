from typing import Optional


class Choice:
    choice1: str
    choice2: str
    selected_choice: Optional[str]

    def __init__(
        self, choice1: str, choice2: str, selected_choice: Optional[str] = None
    ) -> None:
        self.choice1 = choice1
        self.choice2 = choice2
        self.selected_choice = selected_choice

    def __str__(self) -> str:
        return (
            f"Choice 1: {self.choice1}, Choice 2: {self.choice2}, "
            f"Selected Choice: {self.selected_choice if self.selected_choice else 'None'}"
        )

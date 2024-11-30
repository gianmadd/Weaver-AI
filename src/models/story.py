from typing import Optional

from models.choice import Choice


class Story:
    plot: str
    summary: str
    choices: list[Choice]
    current_choice: Optional[Choice]

    def __init__(self) -> None:
        self.plot = ""
        self.summary = ""
        self.choices = []
        self.current_choice = None

    def __str__(self) -> str:
        choices_str = ", ".join(str(choice) for choice in self.choices)
        current_choice_str = str(self.current_choice) if self.current_choice else "None"
        return (
            f"Story:\nPlot: {self.plot}\nSummary: {self.summary}\n"
            f"Choices: [{choices_str}]\nCurrent Choice: {current_choice_str}"
        )

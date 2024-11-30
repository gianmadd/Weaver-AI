from client import send_prompt
from prompts import (
    prompt_choices,
    prompt_conclusion,
    prompt_continue,
    prompt_introduction,
    prompt_statistics,
    prompt_summarize,
)


class ModelHandler:
    def __init__(self, language: str = "en"):
        self.language = language

    def set_language(self, language: str):
        """
        Update the language for the model handler.
        """
        self.language = language

    def generate_statistics(self, setting: str, name: str, goal: str):
        """
        Generates character statistics based on the setting, name, goal, and language.
        """
        return (
            send_prompt(prompt_statistics(setting, name, goal, self.language))
            .strip()
            .split("\n")
        )

    def generate_introduction(self, setting: str, name: str, goal: str):
        """
        Generates the story introduction based on the setting, character, goal, and language.
        """
        return send_prompt(
            prompt_introduction(setting, name, goal, self.language)
        ).strip()

    def generate_choices(self, plot: str):
        """
        Generates possible choices for the next part of the story based on the plot and language.
        """
        return [
            choice.strip()
            for choice in send_prompt(prompt_choices(plot, self.language))
            .strip()
            .split("\n")
            if choice.strip()
        ]

    def continue_story(self, plot: str, choice: str):
        """
        Continues the story based on the current plot, user's choice, and language.
        """
        return send_prompt(prompt_continue(plot, choice, self.language)).strip()

    def generate_conclusion(self, plot: str):
        """
        Generates the conclusion for the story based on the plot and language.
        """
        return send_prompt(prompt_conclusion(plot, self.language)).strip()

    def summarize_story(self, plot: str):
        """
        Summarizes the story to a shorter version based on the plot and language.
        """
        return send_prompt(prompt_summarize(plot, self.language)).strip()

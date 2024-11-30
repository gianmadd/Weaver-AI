from typing import List

from client import send_prompt
from prompts import PromptGenerator


class ModelHandler:
    language: str
    prompt_generator: PromptGenerator

    def __init__(self, language: str = "en") -> None:
        self.language = language
        self.prompt_generator = PromptGenerator(self.language)

    def set_language(self, language: str) -> None:
        self.language = language

    def generate_statistics(self, setting: str, name: str, goal: str) -> List[str]:
        return (
            send_prompt(
                self.prompt_generator.prompt_statistics(
                    setting=setting, character=name, goal=goal
                )
            )
            .strip()
            .split("\n")
        )

    def generate_introduction(self, setting: str, name: str, goal: str) -> str:
        return send_prompt(
            self.prompt_generator.prompt_introduction(
                setting=setting, character=name, goal=goal
            )
        ).strip()

    def generate_choices(self, plot: str) -> List[str]:
        return [
            choice.strip()
            for choice in send_prompt(
                self.prompt_generator.prompt_choices(current_story=plot)
            )
            .strip()
            .split("\n")
            if choice.strip()
        ]

    def continue_story(self, plot: str, choice: str) -> str:
        return send_prompt(
            self.prompt_generator.prompt_continue(
                current_story=plot, user_choice=choice
            )
        ).strip()

    def generate_conclusion(self, plot: str) -> str:
        return send_prompt(
            self.prompt_generator.prompt_conclusion(current_story=plot)
        ).strip()

    def summarize_story(self, plot: str) -> str:
        return send_prompt(
            self.prompt_generator.prompt_summarize(current_story=plot)
        ).strip()

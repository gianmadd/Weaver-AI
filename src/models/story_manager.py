from models.character import Character
from models.choice import Choice
from models.model_handler import ModelHandler
from models.stat import Stat
from models.story import Story
from typing import List


class StoryManager:
    character: Character
    story: Story
    model_handler: ModelHandler

    def __init__(self, character: Character, story: Story, model_handler: ModelHandler) -> None:
        self.character = character
        self.story = story
        self.model_handler = model_handler

    def start_story(self) -> None:
        stats_names: List[str] = self.model_handler.generate_statistics(
            setting=self.character.setting, 
            name=self.character.name, 
            goal=self.character.goal
        )

        for name in stats_names:
            stat = Stat(name)
            self.character.add_stat(stat)

        self.story.plot = self.model_handler.generate_introduction(
            setting=self.character.setting, 
            name=self.character.name, 
            goal=self.character.goal
        )

        choices_text: List[str] = self.model_handler.generate_choices(plot=self.story.plot)
        self.story.current_choice = Choice(
            choice1=choices_text[0], 
            choice2=choices_text[1]
        )

    def continue_story(self, selected_choice: str) -> None:
        if self.story.current_choice:
            self.story.current_choice.selected_choice = selected_choice
            self.story.choices.append(self.story.current_choice)

        new_block: str = self.model_handler.continue_story(plot=self.story.plot, choice=selected_choice)
        self.story.plot += "\n\n" + new_block

        choices_text: List[str] = self.model_handler.generate_choices(plot=new_block)
        self.story.current_choice = Choice(
            choice1=choices_text[0], 
            choice2=choices_text[1]
        )

    def end_story(self) -> None:
        conclusion: str = self.model_handler.generate_conclusion(plot=self.story.plot)
        self.story.plot += "\n\n" + conclusion
        self.story.current_choice = None  # No choice after the story ends

    def reset(self) -> None:
        self.character.stats.clear()
        self.story.plot = ""
        self.story.summary = ""
        self.story.choices = []
        self.story.current_choice = None

    def summarize_story(self) -> None:
        self.story.summary = self.model_handler.summarize_story(plot=self.story.plot)

    def __str__(self) -> str:
        return (
            f"StoryManager(\n"
            f"  Character: {self.character},\n"
            f"  Story: {self.story},\n"
            f"  ModelHandler: {self.model_handler}\n"
            f")"
        )

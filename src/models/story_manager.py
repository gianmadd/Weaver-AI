from models.character import Character
from models.model_handler import ModelHandler
from models.story import Story
from models.stat import Stat


class StoryManager:

    def __init__(self, character: Character, story: Story, model_handler: ModelHandler):
        self.character = character
        self.story = story
        self.model_handler = model_handler

    def start_story(self):
        """
        Generates the character stats, story introduction, and initial choices.
        """
        # Generate stats using the LLM
        stats_names = self.model_handler.generate_statistics(
            self.character.setting, self.character.name, self.character.goal
        )

        # Create Stat object and adding them to character object
        for name in stats_names:
            stat = Stat(name)
            self.character.add_stat(stat)

        # Generate the introduction
        self.story.plot = self.model_handler.generate_introduction(
            self.character.setting, self.character.name, self.character.goal
        )

        # Generate the initial choices
        self.story.choices = self.model_handler.generate_choices(self.story.plot)

    def continue_story(self, choice: str):
        """
        Continues the story by appending a new block and generating the next set of choices.
        """
        new_block = self.model_handler.continue_story(self.story.plot, choice)
        self.story.plot += "\n\n" + new_block
        self.story.choices = self.model_handler.generate_choices(self.story.plot)

    def end_story(self):
        """
        Generates the conclusion of the story.
        """
        conclusion = self.model_handler.generate_conclusion(self.story.plot)
        self.story.plot += "\n\n" + conclusion
        self.story.choices = []  # No choices after the story ends

    def reset(self):
        """
        Resets the story and character to their initial states.
        """
        self.character.stats.clear()
        self.story.plot = ""
        self.story.summary = ""
        self.story.choices = []

    def summarize_story(self):
        """
        Summarizes the story using the model handler's summarize_story method.
        """
        self.story.summary = self.model_handler.summarize_story(self.story.plot)

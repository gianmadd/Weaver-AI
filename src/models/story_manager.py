from models.character import Character
from models.choice import Choice
from models.model_handler import ModelHandler
from models.stat import Stat
from models.story import Story


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
        choices_text = self.model_handler.generate_choices(self.story.plot)
        self.story.current_choice = Choice(
            choice1=choices_text[0], choice2=choices_text[1]
        )

    def continue_story(self, selected_choice: str):
        """
        Continues the story by appending a new block and generating the next set of choices.
        """
        # Update the selected choice in the current Choice object
        if self.story.current_choice:
            self.story.current_choice.selected_choice = selected_choice
            self.story.choices.append(self.story.current_choice)

        # Continue the story with the selected choice
        new_block = self.model_handler.continue_story(self.story.plot, selected_choice)
        self.story.plot += "\n\n" + new_block

        # Generate the next set of choices
        choices_text = self.model_handler.generate_choices(new_block)
        self.story.current_choice = Choice(choice1=choices_text[0], choice2=choices_text[1])

    def end_story(self):
        """
        Generates the conclusion of the story.
        """
        conclusion = self.model_handler.generate_conclusion(self.story.plot)
        self.story.plot += "\n\n" + conclusion
        self.story.current_choice = None  # No choice after the story ends

    def reset(self):
        """
        Resets the story and character to their initial states.
        """
        self.character.stats.clear()
        self.story.plot = ""
        self.story.summary = ""
        self.story.choices = []
        self.story.current_choice = None

    def summarize_story(self):
        """
        Summarizes the story using the model handler's summarize_story method.
        """
        self.story.summary = self.model_handler.summarize_story(self.story.plot)

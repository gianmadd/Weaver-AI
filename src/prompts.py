from typing import Dict


class PromptGenerator:
    LANGUAGE_INSTRUCTIONS: Dict[str, str] = {
        "en": "USE ENGLISH.",
        "it": "USA L'ITALIANO.",
        "es": "USA EL ESPAÑOL.",
        "fr": "UTILISEZ LE FRANÇAIS.",
        "de": "VERWENDE DEUTSCH.",
    }
    language: str

    def __init__(self, language: str = "en") -> None:
        self.language = language

    def get_language_instruction(self) -> str:
        return self.LANGUAGE_INSTRUCTIONS[self.language]

    def prompt_statistics(self, setting: str, character: str, goal: str) -> str:
        return (
            f"Setting: {setting}\n"
            f"Main Character: {character}\n"
            f"Goal: {goal}\n"
            f"{self.get_language_instruction()}\n"
            "Based on the setting, main character, and their goal, create four unique attributes that will define the character in this story. "
            "Each attribute should be relevant to the narrative and gameplay. "
            "Each attribute should highlight an important trait or skill of the main character that will aid them in achieving their goal. "
            "For each attribute, provide only the name (a single word).\n"
            "DO NOT include any additional text or commentary, only the attributes in this format:\n"
            "Attribute Name\n"
            "Attribute Name\n"
            "Attribute Name\n"
            "Attribute Name\n"
        )

    def prompt_introduction(self, setting: str, character: str, goal: str) -> str:
        return (
            f"Setting: {setting}\n"
            f"Main Character: {character}\n"
            f"Goal: {goal}\n"
            f"Write a short and captivating introduction (maximum 2 sentences) {self.get_language_instruction()} "
            "that introduces the main character, their goal, and the initial situation.\n"
            "The introduction must:\n"
            "- Establish the main character as the central figure.\n"
            "- Clearly define how the main character's goal drives the narrative forward.\n"
            "- Avoid mentioning secondary characters or events unless they directly relate to the main character's goal.\n"
            "Convey the tone of the story (e.g., epic, mysterious, or dramatic) and capture the reader's attention.\n"
            "DO NOT include any additional text, comments, or explanations—just the story itself."
        )

    def prompt_choices(self, current_story: str) -> str:
        return (
            f"Story so far:\n{current_story}\n\n"
            f"Provide two distinct and intriguing options for the reader to continue the story {self.get_language_instruction()}.\n"
            "Each option should:\n"
            "- Present a significant action or decision by the main character.\n"
            "- Directly relate to the main character's progress toward their goal.\n"
            "- Be concrete and distinct from one another.\n"
            "- Avoid introducing unrelated events or focusing on secondary characters.\n"
            "Write each option clearly using the following structure:\n"
            "1. [Description of choice 1, such as a significant action or decision]\n"
            "2. [Description of choice 2, such as an alternative action or decision]\n"
            "DO NOT add any extra information, explanations, or commentary—only the choices.\n"
            "DO NOT add any intro to the choices such as 'Here are the two options for the reader to continue the story:'"
        )

    def prompt_continue(self, current_story: str, user_choice: str) -> str:
        return (
            f"Story so far:\n{current_story}\n\n"
            f"The reader has chosen: {user_choice}\n\n"
            f"Continue the story {self.get_language_instruction()} by explicitly referencing the choice made. "
            f"Write a continuation that:\n"
            "- Begins by describing the choice explicitly in the narrative.\n"
            "- Shows how the main character takes action based on the choice.\n"
            "- Describes the immediate consequences of the choice in the story.\n"
            "- Includes emotional or descriptive details to enrich the scene.\n"
            "The continuation should:\n"
            "- Be concise (no more than 2 sentences).\n"
            "- Avoid introducing new choices or unrelated events.\n"
            "- Be fully focused on the chosen action and its direct impact on the story.\n"
            "DO NOT include introductions, commentary, or extra text—just the continuation."
        )

    def prompt_conclusion(self, current_story: str) -> str:
        return (
            f"Story so far:\n{current_story}\n\n"
            f"Write a short and compelling conclusion (maximum 3 sentences) {self.get_language_instruction()}.\n"
            "The conclusion should:\n"
            "- Resolve the story in a way that highlights the main character's actions and goal.\n"
            "- Keep the main character as the central figure in the resolution.\n"
            "- Reflect on how their journey and choices shaped the final outcome.\n"
            "- Avoid focusing on secondary characters or unrelated events.\n"
            "DO NOT include any introduction, additional text, commentary, or explanations. Only the conclusion."
        )

    def prompt_summarize(self, current_story: str) -> str:
        return (
            f"Story so far:\n{current_story}\n\n"
            f"Summarize the story so far {self.get_language_instruction()} in a concise manner while retaining the key events and the tone of the narrative.\n"
            "The summary must:\n"
            "- Focus on the main character's journey and actions.\n"
            "- Emphasize the progress made toward their goal.\n"
            "- Include only events that are directly related to the main character's goal.\n"
            "- Avoid unnecessary details or focus on secondary characters or unrelated events.\n"
            "DO NOT include any introductions, commentary, or unrelated text—only the summary itself."
        )

    def __str__(self) -> str:
        return f"Language: {self.language}, Language Instruction: {self.get_language_instruction()}"

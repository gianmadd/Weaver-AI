import logging

import gradio as gr

from models.character import Character
from models.model_handler import ModelHandler
from models.story import Story
from models.story_manager import StoryManager
from utils import get_random_triple

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

DATA_PATH = "../data"
START_TRIPLES_PATH = f"{DATA_PATH}/start_triples.json"

story_manager = None  # Global instance for StoryManager

LOG_DIVIDER = "=" * 50


def on_start_click(setting, character_name, goal, language):
    global story_manager
    logging.info(LOG_DIVIDER)
    logging.info(
        f"Starting a new story with setting='{setting}', character='{character_name}', goal='{goal}', language='{language}'"
    )

    # Set language in ModelHandler
    model_handler = ModelHandler(language=language)

    # Create Character and Story objects
    character = Character(setting, character_name, goal)
    story = Story()
    story_manager = StoryManager(character, story, model_handler)

    # Start the story
    story_manager.start_story()

    # Summarize the story
    story_manager.summarize_story()

    # Update outputs
    stats_table = [[stat.name, stat.value] for stat in character.stats]
    updated_story = story.plot
    updated_summary = story.summary

    if story.current_choice:
        updated_choices = gr.update(
            choices=[story.current_choice.choice1, story.current_choice.choice2],
            interactive=True,
        )
        logging.info(f"[on_start_click] Current choices: {updated_choices}")
    else:
        updated_choices = gr.update(choices=[], interactive=False)
        logging.info("[on_start_click] No choices available.")


    confirm_choice_interactive = gr.update(interactive=True if updated_choices else False)
    conclude_interactive = gr.update(interactive=True)

    return (
        updated_story,
        updated_summary,
        updated_choices,
        confirm_choice_interactive,
        conclude_interactive,
        stats_table,
    )


def on_refresh_start_values_click():
    logging.info(LOG_DIVIDER)
    new_setting, new_character, new_goal = get_random_triple(START_TRIPLES_PATH)

    logging.info(
        f"Refreshed start values: setting='{new_setting}', character='{new_character}', goal='{new_goal}'"
    )
    logging.info(LOG_DIVIDER)

    setting_input_update = gr.update(value=new_setting)
    character_input_update = gr.update(value=new_character)
    goal_input_update = gr.update(value=new_goal)

    return setting_input_update, character_input_update, goal_input_update


def on_confirm_choice_click(choice):
    global story_manager
    logging.info(LOG_DIVIDER)
    logging.info(f"User made a choice: {choice}")

    # Continue the story
    story_manager.continue_story(choice)

    for c in story_manager.story.choices:
        logging.info(f"@@@@@@@@@@@@@@@@@ {c.choice1} @@@@@@@@@@@@@@@@@ {c.choice2} @@@@@@@@@@@@@@@@@ {c.selected_choice}")

    # Update the story summary
    story_manager.summarize_story()

    updated_story = story_manager.story.plot
    updated_summary = story_manager.story.summary

    if story_manager.story.current_choice:
        updated_choices = gr.update(
            choices=[story_manager.story.current_choice.choice1, story_manager.story.current_choice.choice2],
            interactive=True,
        )
        logging.info(f"[on_confirm_choice_click] New Choices: {updated_choices}")
    else:
        updated_choices = gr.update(choices=[], interactive=False)
        logging.info("[on_confirm_choice_click] No further choices available.")

    confirm_choice_interactive = gr.update(interactive=True if updated_choices else False)

    return updated_story, updated_summary, updated_choices, confirm_choice_interactive


def on_conclude_click():
    global story_manager
    logging.info(LOG_DIVIDER)
    logging.info("Concluding the story.")

    # End the story
    story_manager.end_story()

    # Generate the final summary
    story_manager.summarize_story()

    logging.info(f"Final story: {story_manager.story.__dict__}")
    logging.info(LOG_DIVIDER)

    final_story = story_manager.story.plot
    final_summary = story_manager.story.summary
    choice_radio_update = gr.update(choices=[], interactive=False)
    confirm_choice_update = gr.update(interactive=False)
    conclude_update = gr.update(interactive=False)

    return (
        final_story,
        final_summary,
        choice_radio_update,
        confirm_choice_update,
        conclude_update,
    )


def on_reset_click():
    global story_manager
    logging.info(LOG_DIVIDER)
    logging.info("Resetting the story and character.")

    story_manager = None  # Reset the story manager

    logging.info("StoryManager has been reset.")
    logging.info(LOG_DIVIDER)

    story_output_reset = ""
    summary_reset = ""
    choice_radio_reset = gr.update(choices=[], interactive=False)
    setting_input_reset = gr.update(value="", interactive=True)
    character_input_reset = gr.update(value="", interactive=True)
    goal_input_reset = gr.update(value="", interactive=True)
    stats_table_reset = gr.update(value=[])

    return (
        story_output_reset,
        summary_reset,
        choice_radio_reset,
        setting_input_reset,
        character_input_reset,
        goal_input_reset,
        stats_table_reset,
    )



def gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# Interactive Story Generator", elem_id="title")
        gr.Markdown(
            "### Embark on your own adventure! Choose a setting, a main character, their goal, and a language. Then make decisions to shape your unique story as it unfolds.",
            elem_id="subtitle",
        )

        start_setting, start_character, start_goal = get_random_triple(
            START_TRIPLES_PATH
        )

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("#### Set up your story:")
                btn_refresh_start_values = gr.Button("🔄 Autofill Start Values")

                setting_input = gr.Textbox(label="Setting", placeholder=start_setting)
                character_input = gr.Textbox(
                    label="Character", placeholder=start_character
                )
                goal_input = gr.Textbox(label="Goal", placeholder=start_goal)
                language_input = gr.Dropdown(
                    label="Language",
                    choices=["en", "it", "es", "fr", "de"],
                )
                btn_start = gr.Button("🚀 Start Story", elem_id="start-button")

                gr.Markdown("#### Character Statistics:")
                stats_table = gr.Dataframe(
                    headers=["Statistic", "Value"], value=[], interactive=False
                )

            with gr.Column(scale=2):
                gr.Markdown("### Your Story So Far:")
                story_output = gr.Textbox(
                    label="Complete Story", interactive=False, lines=15, max_lines=15
                )

                gr.Markdown("### Story Summary:")
                story_summary = gr.Textbox(
                    label="Summary", interactive=False, lines=5, max_lines=5
                )

                gr.Markdown("### Make Your Choice:")
                choice_radio = gr.Radio(
                    label="Choose how to continue:", choices=[], interactive=False
                )
                btn_confirm_choice = gr.Button("✅ Confirm Choice", interactive=False)

                gr.Markdown("### Final Actions:")
                with gr.Row():
                    btn_conclude = gr.Button("🏁 Conclude Story", interactive=False)
                    btn_reset = gr.Button("🔄 Reset")

        btn_refresh_start_values.click(
            on_refresh_start_values_click,
            outputs=[setting_input, character_input, goal_input],
        )

        btn_start.click(
            on_start_click,
            inputs=[setting_input, character_input, goal_input, language_input],
            outputs=[
                story_output,
                story_summary,
                choice_radio,
                btn_confirm_choice,
                btn_conclude,
                stats_table,
            ],
        )

        btn_confirm_choice.click(
            on_confirm_choice_click,
            inputs=choice_radio,
            outputs=[
                story_output,
                story_summary,
                choice_radio,
                btn_confirm_choice,
            ],
        )

        btn_conclude.click(
            on_conclude_click,
            outputs=[
                story_output,
                story_summary,
                choice_radio,
                btn_confirm_choice,
                btn_conclude,
            ],
        )

        btn_reset.click(
            on_reset_click,
            outputs=[
                story_output,
                story_summary,
                choice_radio,
                setting_input,
                character_input,
                goal_input,
                stats_table,
            ],
        )

    return demo


if __name__ == "__main__":
    app = gradio_interface()
    app.launch()


if __name__ == "__main__":
    app = gradio_interface()
    app.launch()

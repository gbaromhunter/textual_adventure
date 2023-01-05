from node import *
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Vertical, Horizontal, Container
from textual.reactive import reactive
from textual.widgets import Label, Input
from rich.text import Text


main_text = "This is the main text box"
information_text = "This is the information text box"
possible_actions = "Here will be the possible actions and keywords"
user_input = "Here goes the console that the user will use to input the text"
possible_test = ["update main", "update secondary"]


class MainBox(Label):
    """Display a greeting."""

    main_text = reactive("This is the main text box")

    def render(self) -> RenderResult:
        return self.main_text


class InformationBox(Label):
    """Displays the additional information for the keywords"""

    def render(self) -> RenderResult:
        return information_text


class PossibleBox(Label):
    """Displays the possible actions and keywords"""

    def render(self) -> RenderResult:
        return possible_actions


class UserInput(Container):
    """Displays the possible actions and keywords"""

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Write here")


class Adventure(App):
    CSS_PATH = "main.css"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(MainBox(), InformationBox(), id="left"),
            Vertical(PossibleBox(), UserInput(), id="right")
        )

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.query_one(MainBox).main_text = event.input.value
        event.input.value = ""


if __name__ == "__main__":
    app = Adventure()
    app.run()

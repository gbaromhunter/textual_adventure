from textual.app import App, ComposeResult, RenderResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Label

main_text = "This is the main text box"
information_text = "This is the information text box"
possible_actions = "Here will be the possible actions and keywords"
user_input = "Here goes the console that the user will use to input the text"

class MainBox(Label):
    """Display a greeting."""

    def render(self) -> RenderResult:
        return main_text


class InformationBox(Label):
    """Displays the additional information for the keywords"""

    def render(self) -> RenderResult:
        return information_text


class PossibleBox(Label):
    """Displays the possible actions and keywords"""

    def render(self) -> RenderResult:
        return possible_actions


class UserInput(Label):
    """Displays the possible actions and keywords"""

    def render(self) -> RenderResult:
        return user_input


class Adventure(App):
    CSS_PATH = "textual_scratch.css"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(MainBox(), InformationBox(), id="left"),
            Vertical(PossibleBox(), UserInput(), id="right")
        )


if __name__ == "__main__":
    app = Adventure()
    app.run()


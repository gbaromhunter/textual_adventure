from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Label, Input

from node import *


class MainBox(Label):
    """Display a greeting."""

    main_text = reactive(current_node.current.text)

    def render(self) -> RenderResult:
        return self.main_text


class Information(Label):
    """Displays the additional information for the keywords"""

    informative = reactive(
        "Type an [red]action[/red] word to change node or an [green]informative[/green] word to inspect it")

    def render(self) -> RenderResult:
        return self.informative


class UserInput(Container):
    """Displays the possible actions and keywords"""

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Type an action (highlighted in red) or an informative word (highlighted in green)")


class Adventure(App):
    CSS_PATH = "main.css"

    def compose(self) -> ComposeResult:
        yield MainBox()
        yield Information()
        yield UserInput()

    @staticmethod
    def on_input_submitted(event: Input.Submitted) -> None:
        if event.input.value in current_node.current.actions:
            for node in nodes_list:
                if current_node.current.actions[event.input.value] == node.name:
                    current_node.change_node(node)
                    MainBox.main_text = current_node.current.text
                    break

        elif event.input.value in current_node.current.informative:
            for word in current_node.current.informative:
                if event.input.value == word:
                    Information.informative = current_node.current.informative[word]
        event.input.value = ""


if __name__ == "__main__":
    app = Adventure()
    app.run()

from textual.app import App, ComposeResult, RenderResult
from textual.containers import Vertical, Horizontal, Container
from textual.reactive import reactive
from textual.widgets import Label, Input

from node import *

test = Node(text="this is the first test node. The next one will be the second test",
            name="test",
            actions={
                "next": "test2"
            },
            informative={
                "first": "Wow, are you surprised i'm going to write the word test again? Test."
            })

test2 = Node(text="this is the second test node. The next one will be the third test",
             name="test2",
             actions={
                 "next": "test3"
             },
             informative={
                 "second": "Hey, Test is forever, right? Test."
             })

test3 = Node(text="this is the third test node.",
             name="test3",
             actions={
                 "next": "test3"
             },
             informative={
                 "third": "Test for life man! The Testcode!"
             })

nodes_list = [test, test2, test3]

current_node = test


class MainBox(Label):
    """Display a greeting."""

    main_text = reactive(current_node.text)

    def render(self) -> RenderResult:
        return self.main_text


class Information(Label):
    """Displays the additional information for the keywords"""

    informative = reactive("Type an action word to change node or an informative word for additional information")

    def render(self) -> RenderResult:
        return self.informative


class PossibleBox(Label):
    """Displays the possible actions and keywords"""

    def render(self) -> RenderResult:
        return "dummy text"


class UserInput(Container):
    """Displays the possible actions and keywords"""

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Write here")


class Adventure(App):
    CSS_PATH = "main.css"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(MainBox(), Information(), id="left"),
            Vertical(PossibleBox(), UserInput(), id="right")
        )

    @staticmethod
    def on_input_submitted(event: Input.Submitted) -> None:
        global current_node
        if event.input.value in current_node.actions:
            for node in nodes_list:
                if event.input.value == node.name:
                    current_node = node
        elif event.input.value in current_node.informative:
            for word in current_node.informative:
                if event.input.value == word:
                    Information.informative = current_node.informative[word]
        event.input.value = ""


if __name__ == "__main__":
    app = Adventure()
    app.run()

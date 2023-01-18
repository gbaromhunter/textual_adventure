from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container, Vertical, Horizontal
from textual.reactive import reactive
from textual.widgets import Label, Input, ListView, ListItem

from node_class import Node, Base

engine = create_engine('sqlite:///nodes_database.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
all_nodes = list(session.query(Node))


# Define the widget classes


class Choice(ListItem):
    def __init__(self, choice) -> None:
        super().__init__(Label(choice.name))
        self.choice = choice


class Choices(ListView):
    """Displays the node list."""

    def __init__(self, choices: list[Node]) -> None:
        super().__init__()
        self._choices = choices

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        for choice in self._choices:
            yield Choice(choice)

    def on_mount(self):
        self.index = 0


class MainInformation(Label):
    """Displays the main text."""

    main_information_text = reactive("Here goes the main information")

    def render(self) -> RenderResult:
        return self.main_information_text


class Actions(Label):
    """Displays the actions the user can perform."""

    actions_list = reactive("Here the actions of the user")

    def render(self) -> RenderResult:
        return self.actions_list


class UserInput(Container):
    """Displays the user input."""

    def compose(self) -> ComposeResult:
        yield Input(placeholder="This is the user input")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        event.input.value = ""


class Editor(App):
    """This is the main application"""
    CSS_PATH = "editor.css"
    current = reactive(None)
    all_nodes = reactive(all_nodes)

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Choices(self.all_nodes),
            Vertical(
                MainInformation(),
                UserInput(),
                id="middle"
            ),
            Actions()
        )

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.current = self.all_nodes[self.query_one(Choices).index]
        self.query_one(MainInformation).main_information_text = self.current.__repr__()


# Runs the app
if __name__ == "__main__":
    app = Editor()
    app.run()

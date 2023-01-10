from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container, Vertical
from textual.reactive import reactive
from textual.widgets import Label, Input

from node_class import Node, Base

engine = create_engine('sqlite:///nodes_database.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
all_nodes = session.query(Node)


# Define the widget classes
class NodesList(Label):
    """Displays the nodes list."""
    node_names = [node.name for node in all_nodes]
    nodes_names = "\n".join(node_names)
    nodes_list_text = reactive(nodes_names)

    def render(self) -> RenderResult:
        return self.nodes_list_text


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


class Editor(App):
    """This is the main application"""
    CSS_PATH = "editor.css"
    current = reactive(None)

    def compose(self) -> ComposeResult:
        yield NodesList()
        yield Vertical(MainInformation(), UserInput())
        yield Actions()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        for node in all_nodes:
            if event.input.value == node.name:
                self.current = node
        self.query_one(MainInformation).main_information_text = self.current.__repr__()
        event.input.value = ""


# Runs the app
if __name__ == "__main__":
    app = Editor()
    app.run()

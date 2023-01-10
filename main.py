# Import the required libraries
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Label, Input

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from node_class import Node, Base

engine = create_engine('sqlite:///nodes_database.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
nodes_list = session.query(Node)

# Define the widget classes
class MainBox(Label):
    """Display a greeting."""

    main_text = reactive(nodes_list[0].highlighted_text())

    def render(self) -> RenderResult:
        return self.main_text


class Information(Label):
    """Displays the additional information for the keywords"""

    informative = reactive(
        "Type an [italic bold purple]action[/italic bold purple] word to change node "
        "or an [italic bold green]main_information_text[/italic bold green] word to inspect it")

    def render(self) -> RenderResult:
        return self.informative


class UserInput(Container):
    """Displays the possible actions and keywords"""

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Type an action (highlighted in purple) or an main_information_text word (highlighted in green)")


class Adventure(App):
    """This is the main application"""
    CSS_PATH = "main.css"
    current_node = reactive(nodes_list[0])

    def change_node(self, new_node: Node):
        self.current_node = new_node

    def compose(self) -> ComposeResult:
        yield MainBox()
        yield Information()
        yield UserInput()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.value in self.current_node.actions:
            for node in nodes_list:
                if self.current_node.actions[event.input.value] == node.name:
                    self.change_node(node)
                    self.query_one(MainBox).nodes_list_text = self.current_node.highlighted_text()
                    break

        elif event.input.value in self.current_node.informative:
            for word in self.current_node.informative:
                if event.input.value == word:
                    self.query_one(Information).main_information_text = self.current_node.informative[word]
        event.input.value = ""


# Runs the app
if __name__ == "__main__":
    app = Adventure()
    app.run()

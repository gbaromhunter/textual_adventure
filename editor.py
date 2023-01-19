# import all the necessary components from external modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container, Vertical, Horizontal
from textual.reactive import reactive
from textual.widgets import Label, Input, ListView, ListItem

# import the Node and Base classes from the node_class.py file
from node_class import Node, Base

# create the engine and the connection to the database file
engine = create_engine('sqlite:///nodes_database.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# extract the list of all the nodes from the database. each element is an instance of Node class
all_nodes = list(session.query(Node))


class Choice(ListItem):
    """define the list item widget that will populate the ListView. the parameter choice is a Node instance"""

    def __init__(self, choice: Node) -> None:
        """initialise the class parameters"""

        super().__init__(Label(choice.name))
        self.choice = choice


class Choices(ListView):
    """Displays the node list"""

    def __init__(self, choices: list[Node]) -> None:
        """initialise the class parameters"""

        super().__init__()
        self._choices = choices

    def compose(self) -> ComposeResult:
        """Compose the child widgets into the ListView"""

        for choice in self._choices:
            yield Choice(choice)

    def on_mount(self):
        """as a bug is present, this ensures the first index is selected on mount"""

        self.index = 0


class MainInformation(Label):
    """Displays the main text"""


class Actions(Label):
    """Displays the actions the user can perform"""

    actions_list = reactive("Here the actions of the user")

    def render(self) -> RenderResult:
        return self.actions_list


class UserInput(Container):
    """Displays the user input"""

    def compose(self) -> ComposeResult:
        """compose the widget with a placeholder"""
        yield Input(placeholder="This is the user input")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """when the user press enter and there is text in the user input box, this function will be called."""
        event.input.value = ""


class Editor(App):
    """This is the main application"""
    CSS_PATH = "editor.css"
    current = reactive(None)
    all_nodes = reactive(all_nodes)

    def compose(self) -> ComposeResult:
        """compose the widget from all the following components"""
        yield Horizontal(
            Choices(self.all_nodes),
            Vertical(
                Vertical(MainInformation("Here goes the main information")),
                UserInput(),
                id="middle"),
            Actions())

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """when the user clicks on an item of the list, or press enter while it's selected, this will be called"""
        self.current = self.all_nodes[self.query_one(Choices).index]
        self.query_one(MainInformation).update(event.item.choice.__repr__())


# Runs the app
if __name__ == "__main__":
    app = Editor()
    app.run()

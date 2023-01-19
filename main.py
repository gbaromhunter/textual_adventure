# Import the required external libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.reactive import reactive
from textual.widgets import Label, Input

# import the Node and Base class from the node_class.py file
from node_class import Node, Base

# create the engine and the connection to the database file
engine = create_engine('sqlite:///nodes_database.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
nodes_list = list(session.query(Node))

# define the colors of the actions and the informative words
action_color = "red"
informative_color = "green"
welcome_instruction = "Welcome. Follow the instructions in the box below to go forward."
informative_instruction = f"Type an [italic bold {action_color}]action[/italic bold {action_color}] to change node " \
                          f"or an [italic bold {informative_color}]informative[/italic bold {informative_color}] " \
                          f"word to inspect it"


class MainBox(Label):
    """Displays the main text"""


class Information(Label):
    """Displays the additional information for the informative keywords"""


class UserInput(Container):
    """Displays the user input"""

    def compose(self) -> ComposeResult:
        """composes the widget with the provided placeholder"""
        yield Input(
            placeholder="Type an action (highlighted in purple) or an informative word (highlighted in green)")


class Adventure(App):
    """This is the main application"""

    # define the css file path and the initiates the current node as the first in the list
    CSS_PATH = "main.css"
    current_node = reactive(nodes_list[0])

    def change_node(self, new_node: Node):
        """this method changes the current node of the App instance"""
        self.current_node = new_node

    def compose(self) -> ComposeResult:
        """this method composes the App instance of widget children"""
        yield Vertical(MainBox(self.current_node.highlighted_text()), id="main")
        yield Vertical(Information(informative_instruction, id="informative"))
        yield UserInput()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """
        when the user types and then press enter this will be called.
        if the user types a word contained in the actions parameter, it will update the current node accordingly.
        if the typed word is an informative word, it will update the information box accordingly.
        it then resets the user input in the box.
        """
        if event.input.value in self.current_node.actions:
            for node in nodes_list:
                if self.current_node.actions[event.input.value] == node.name:
                    self.change_node(node)
                    self.query_one(MainBox).update(self.current_node.highlighted_text())
                    break

        elif event.input.value in self.current_node.informative:
            for word in self.current_node.informative:
                if event.input.value == word:
                    self.query_one(Information).update(self.current_node.informative[word])
        event.input.value = ""


# Runs the app
if __name__ == "__main__":
    app = Adventure()
    app.run()

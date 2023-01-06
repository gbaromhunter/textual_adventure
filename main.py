# Import the required libraries
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Label, Input

# Import the Node and Active classes
from node import Node, Active

# Create some test nodes and assign the first test one to the Active current_node
test = Node(text="this is the first test node. The next one will be the second test",
            name="test",
            actions={
                "second test": "test2",
            },
            informative={
                "first": "Wow, are you surprised i'm going to write the word test again? Test."
            })

test2 = Node(text="this is the second test node. The next one will be the third test. The previous one is the first",
             name="test2",
             actions={
                 "third test": "test3",
                 "first": "test",
             },
             informative={
                 "second": "Hey, Test is forever, right? Test.",
             })

test3 = Node(text="this is the third test node. The previous one is the second.",
             name="test3",
             actions={
                 "second": "test2"
             },
             informative={
                 "third": "Test for life man! The Testcode!"
             })

nodes_list = [test, test2, test3]
current_node = Active(test)


# Define the widget classes
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
    """This is the main application"""
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


# Runs the app
if __name__ == "__main__":
    app = Adventure()
    app.run()

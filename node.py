# This file describes the behaviour of the Node which contains information about the story.


from rich.text import Text


def color_word(word, color):
    return f"[{color}]{word}[/{color}]"


class Node:
    """
    The class describes the behaviour of the Node. Has various parameters. Some self explanatory, others less so.
    actions is a dictionary with words that needs to be actions and their colors.
    The actions words might be actions, in this case the color is red
    """

    def __init__(self, text="", name="", actions=None):
        """
        :type actions: dict
        :type name: str
        :type text: str
        """
        self.name = name
        self.actions = actions
        self.text = Text(text, justify="center")

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

    def set_text(self, new_text):
        self.text = new_text

    def set_actions(self, actions):
        self.actions = actions


inizio = Node(text="Questo è un nodo di prova per vedere come esce")

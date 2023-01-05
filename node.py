# This file describes the behaviour of the Node which contains information about the story.


def color_word(word: str, color: str) -> str:
    """
    This function add some tags to the word and returns a full tagged string
    """
    return f"[{color}]{word}[/{color}]"


class Node:
    """
    The class describes the behaviour of the Node. Has various parameters. Some self explanatory, others less so.
    actions is a dictionary with words as keys and as values, the name of the subsequent nodes
    informative is a dictionary with words as keys and as values, the text to display in the information panel
    """

    def __init__(self, text="", name="", actions=None, informative=None) -> None:
        """
        :type informative: dict
        :type actions: dict
        :type name: str
        :type text: str
        """
        self.informative = informative
        self.name = name
        self.actions = actions
        self.text = text

    def get_name(self) -> str:
        return self.name

    def get_text(self) -> str:
        return self.text

    def set_text(self, new_text: str) -> None:
        self.text = new_text

    def add_action(self, new_action: str, name_node: str) -> None:
        if self.actions is not None:
            self.actions[new_action] = name_node
        else:
            self.actions = {new_action: name_node}

    def add_informative(self, new_word: str, description: str) -> None:
        if self.informative is not None:
            self.informative[new_word] = description
        else:
            self.informative = {new_word: description}


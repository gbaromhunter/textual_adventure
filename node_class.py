# import the necessary external modules
import sqlalchemy_jsonfield
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

# import the Base class from SQLAlchemy
Base = declarative_base()

# define the colors of the actions and the informative words
action_color = "red"
informative_color = "green"

def format_dict(dictionary: dict):
    """format in a pleasant way the argument dictionary"""

    return "\n".join(f"{k}: {v}" for k, v in dictionary.items())


def highlight_keywords(text: str, words: list[str], color: str) -> str:
    """highlights the provided keywords in the argument text, with the argument color"""

    for word in words:
        text = text.replace(word, f"[italic bold {color}]{word}[/italic bold {color}]", 1)
    return text


# Create the Node class
class Node(Base):
    """
    The class describes the behaviour of the Node.
    actions is a dictionary with words as keys, and as values the name of the subsequent nodes
    main_information_text is a dictionary with words as keys, and as values the text to display in the information panel
    """

    # this is a parameter relative to SQLAlchemy to identify the class in a table object
    __tablename__ = 'nodes'

    # define the parameters of the class
    name = Column(String(), primary_key=True)
    text = Column(String())
    actions = Column(sqlalchemy_jsonfield.JSONField())
    informative = Column(sqlalchemy_jsonfield.JSONField())

    def __repr__(self) -> str:
        """
        this function represents the object Node by formatting it correctly.
        it will also highlight the action words and the informative words in their respective colors.
        """

        return f"Node attributes:\n" \
               f"\nName:\n{self.name}\n" \
               f"\nText:\n{self.highlighted_text()}\n" \
               f"\nActions:\n" \
               f"{self.formatted_dict_actions()}\n" \
               f"\nInformatives:\n" \
               f"{self.formatted_dict_informative()}\n"

    def get_name(self) -> str:
        """it gets the name of the node"""

        return self.name

    def get_text(self) -> str:
        """it gets the main text of the node, witch will contain the action and informative words"""

        return self.text

    def set_text(self, new_text: str) -> None:
        """it sets the main text of the node with the string argument provided"""

        self.text = new_text

    def add_action(self, new_action: str, name_node: str) -> None:
        """
        it adds an action to the node, composing a dictionary entry with the string arguments provided.
        it also checks if it has to add a new entry or create a new dictionary depending on self.actions being None.
        """

        if self.actions is not None:
            self.actions[new_action] = name_node
        else:
            self.actions = {new_action: name_node}

    def add_informative(self, new_word: str, description: str) -> None:
        """
        it adds an informative word to the node, composing a dictionary entry with the string arguments provided.
        it also checks if it has to add a new entry or create a new dictionary depending on self.informative being None.
        """

        if self.informative is not None:
            self.informative[new_word] = description
        else:
            self.informative = {new_word: description}

    def highlighted_text(self) -> str:
        """
        this method returns the highlighted main text of the node.
        It wraps those words with rich text tags so they get automatically colored
        """

        h_text = self.text
        h_text = highlight_keywords(h_text, list(self.actions.keys()), action_color)
        h_text = highlight_keywords(h_text, list(self.informative.keys()), informative_color)
        return h_text

    def formatted_dict_actions(self):
        """returns the highlighted formatted text of the actions"""

        text_actions = format_dict(self.actions)
        return highlight_keywords(text_actions, list(self.actions.keys()), action_color)

    def formatted_dict_informative(self):
        """returns the highlighted formatted text of the informative words"""

        text_informatives = format_dict(self.informative)
        return highlight_keywords(text_informatives, list(self.informative.keys()), informative_color)

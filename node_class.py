import sqlalchemy_jsonfield
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

# Import the Base class
Base = declarative_base()

action_color = "red"
informative_color = "green"


def format_dict(dictionary: dict):
    return "\n".join(f"{k}: {v}" for k, v in dictionary.items())


def highlight_keywords(text: str, words: list[str], color: str) -> str:
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
    __tablename__ = 'nodes'

    name = Column(String(), primary_key=True)
    text = Column(String())
    actions = Column(sqlalchemy_jsonfield.JSONField())
    informative = Column(sqlalchemy_jsonfield.JSONField())

    def __repr__(self) -> str:
        return f"Node attributes:\n" \
               f"\nName:\n{self.name}\n" \
               f"\nText:\n{self.highlighted_text()}\n" \
               f"\nActions:\n" \
               f"{self.formatted_dict_actions()}\n" \
               f"\nInformatives:\n" \
               f"{self.formatted_dict_informative()}\n"
        # "\n".join(f"{k}: {v}" for k, v in self.actions.items()) \
        # "\n".join(f"{k}: {v}" for k, v in self.informative.items())

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

    def highlighted_text(self) -> str:
        h_text = self.text
        h_text = highlight_keywords(h_text, list(self.actions.keys()), action_color)
        h_text = highlight_keywords(h_text, list(self.informative.keys()), informative_color)
        return h_text

    def formatted_dict_actions(self):
        text_actions = format_dict(self.actions)
        return highlight_keywords(text_actions, list(self.actions.keys()), action_color)

    def formatted_dict_informative(self):
        text_informatives = format_dict(self.informative)
        return highlight_keywords(text_informatives, list(self.informative.keys()), informative_color)

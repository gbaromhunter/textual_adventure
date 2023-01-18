import sqlalchemy_jsonfield
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

# Import the Base class
Base = declarative_base()


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
        return f"Node attributes:\n\n" \
               f"\n\nname:\n{self.name}\n\n" \
               f"\n\ntext:\n{self.text}\n\n" \
               f"\n\nactions:\n{self.actions}\n\n" \
               f"\n\ninformatives:\n{self.informative}\n\n"

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
        for word in self.actions:
            h_text = h_text.replace(word, f"[italic bold purple]{word}[/italic bold purple]", 1)
        for word in self.informative:
            h_text = h_text.replace(word, f"[italic bold green]{word}[/italic bold green]", 1)
        return h_text

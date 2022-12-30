"""Ti svegli nel tuo letto, come succede di solito, confuso e vuoto. È una vita piatta la tua e ormai lo hai capito
bene. Sei consapevole che c'è qualcosa che non va e senti di stare perdendo tempo prezioso. Stamattina ti alzato
stranamente all'alba con una strana sensazione. Ti senti irrequieto come se stesse per succedere qualcosa
d'inaspettato... È come se qualcuno avesse iniziato a osservarti, una specie di muto spettatore. Hai una insolita
energia, dato che di solito sei routinario e

Il giocatore deve poter scegliere le azioni da compiere che lo porteranno al passaggio successivo. Deve anche avere
la possibilità di approfondire parole chiave che riveleranno particolari ulteriori sulla storia.
Ogni macro decisione può essere negativa o positiva in base alla personalità scelta all'inizio e deve dare nel futuro
possibilità di rimediare all'errore.

Bisogna che crei una data structure apposita per i passaggi.
Ogni passaggio come attributo avrà il testo, le parole chiave da poter approfondire, e un dizionario che punta al nome
del passaggio successivo
"""
from rich import print
from rich.console import Console
from rich.layout import Layout, Panel
from rich.pretty import Pretty
from rich.text import Text

console = Console()


def create_splitted_layout(upper_title, lower_title, ratio):
    layout = Layout()
    layout.split_column(Layout(name=upper_title), Layout(name=lower_title))
    layout[upper_title].size = None
    layout[upper_title].ratio = ratio
    return layout


def color_word(word, color):
    return f"[{color}]{word}[/{color}]"


class Node:

    def __init__(self, upper_title="", lower_title="", ratio=3, text="", child=None, parent=None, highlighted=None):
        self.upper_title = upper_title
        self.lower_title = lower_title
        if child is None:
            child = {}
        if parent is None:
            parent = {}
        self.text = Text(text, justify="center")
        if highlighted:
            self.text.highlight_words(highlighted, "green")
        self.parent = parent
        self.child = child
        self.layout = create_splitted_layout(self.upper_title, self.lower_title, ratio)
        self.actions = list(highlighted)
        self.highlighted = highlighted

    def get_text(self):
        return self.text

    def get_parent(self):
        return self.parent

    def get_child(self):
        return self.child

    def set_highlighted(self, highlighted):
        self.highlighted = highlighted

    def set_text(self, new_text):
        self.text = new_text

    def add_child(self, new_childs, sub=False):
        if sub:
            self.child = new_childs
        else:
            for key, child in new_childs:
                self.child[key] = child

    def add_parent(self, new_parents, sub=False):
        if sub:
            self.parent = new_parents
        else:
            for key, parent in new_parents:
                self.parent[key] = parent

    def display(self):
        actions = Pretty(self.actions)
        self.layout[self.upper_title].update(Layout(Panel(self.text,
                                                          title_align="center",
                                                          title=color_word(self.upper_title, "red"),
                                                          highlight=True)))
        self.layout[self.lower_title].update(Layout(Panel(actions,
                                                          title_align="center",
                                                          title=color_word(self.lower_title, "red"),
                                                          highlight=True)))
        print(self.layout)


inizio = Node(upper_title="Nodo di prova",
              lower_title="Azioni",
              ratio=3,
              text="Questo è un nodo di prova per vedere come esce",
              highlighted={"prova": "green"})
inizio.display()

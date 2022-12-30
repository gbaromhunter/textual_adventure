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
from rich.console import Console

console = Console()


def color_word(word, color):
    return f"[{color}]{word}[/{color}]"


class Node:

    def __init__(self, title="", text="", child=None, parent=None, highlighted=None):
        if child is None:
            child = {}
        if parent is None:
            parent = {}
        self.title = title
        self.text = text
        self.parent = parent
        self.child = child
        if highlighted is None:
            highlighted = {}
        else:
            highlighted = {col: color_word(col, highlighted[col]) for col in highlighted}

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def get_parent(self):
        return self.parent

    def get_child(self):
        return self.child

    def set_title(self, new_title):
        self.title = new_title

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
        console.rule(f"[bold red]{self.title}")


inizio = Node("Nodo di prova", "Questo è un nodo di prova per vedere come esce")

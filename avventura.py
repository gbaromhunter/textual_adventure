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



possible concept:
costruire un minigioco: attivare un timer e far stoppare l'utente esattamente al momento giusto sui 10 secondi.
Tenere il tempo e vedere di quanto si allontana dalla cifra prestabilita (10). Sommare questi punteggi su 3 tentativi,

io lo faccio più volte e vedo quanto è il mio score, salvo gli esiti dei miei tentativi di modo tale da avere un
riscontro e poter, se l'utente gioca, avere già degli esiti che l'utente deve battere.
esempio: gioco 40 volte e il mio score medio è 343 punti. l'utente deve fare 344 punti per battermi

magari posso fare più livelli di difficoltà per il giocatore e dare risposte in accordo
"""
from rich import print
from rich.console import Console
from rich.layout import Layout, Panel
from rich.padding import Padding
from rich.text import Text


console = Console()


def create_splitted_layout(upper_title, lower_left_title, lower_right_title, ratio):
    layout = Layout()
    layout.split_column(Layout(name=upper_title, size=None, ratio=ratio), Layout(name="lower"))
    layout["lower"].split_row(Layout(name=lower_left_title, ratio=2), Layout(name=lower_right_title, ratio=1))
    return layout


def color_word(word, color):
    return f"[{color}]{word}[/{color}]"


class Node:

    def __init__(self, upper_title="", lower_left_title="", lower_right_title="", ratio=3, text="", name="",
                 parent=None, highlighted=None, child=None):
        self.name = name
        self.upper_title = upper_title
        self.lower_left_title = lower_left_title
        self.lower_right_title = lower_right_title
        if child is None:
            child = {}
        if parent is None:
            parent = {}
        self.highlighted = highlighted
        self.text = Text(text, justify="center")
        self.actions = Text(" - ".join(self.highlighted), justify="center")
        if highlighted:
            self.text.highlight_words(highlighted, "green")
            self.actions.highlight_words(highlighted, "green")
        self.parent = parent
        self.child = child
        self.layout = create_splitted_layout(self.upper_title, self.lower_left_title, self.lower_right_title, ratio)

    def get_name(self):
        return self.name

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
        padded_text = Padding(self.text, (1,))
        self.layout[self.upper_title].update(Layout(Panel(padded_text,
                                                          title_align="center",
                                                          title=color_word(self.upper_title, "red"),
                                                          highlight=True)))
        self.layout[self.lower_left_title].update(Layout(Panel(self.actions,
                                                               title_align="center",
                                                               title=color_word(self.lower_left_title, "red"),
                                                               highlight=True)))
        self.layout[self.lower_right_title].update(Layout(Panel("",
                                                                title_align="center",
                                                                title=color_word(self.lower_right_title, "red"),
                                                                highlight=True)))
        print(self.layout)
        return console.input()


inizio = Node(upper_title="Nodo di prova", lower_left_title="Azioni che puoi compiere", lower_right_title="Digita qui",
              ratio=3, text="Questo è un nodo di prova per vedere come esce", highlighted=["nodo", "prova"])
inizio.display()

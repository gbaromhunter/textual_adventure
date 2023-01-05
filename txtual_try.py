from textual import *


class InputBox(Widget):
    """takes typed input mostly for debugging"""
    has_focus: Reactive[bool] = Reactive(False)
    style: Reactive[str] = Reactive("")
    height: Reactive[int or None] = Reactive(None)
    text: Reactive[str] = Reactive("")

    def __init__(self, *, name: str or None = None, height: int or None = None, callback: Callable[[str], None] = None) -> None:
        super().__init__(name=name)
        self.height = height
        self.callback = callback

    def render(self) -> Panel:
        return Panel(
            self.text,
            title=self.name,
            box=box.HEAVY if self.has_focus else box.ROUNDED,
            style="cyan" if self.has_focus else "dim white",
            height=self.height,
            highlight=True
        )

    async def on_focus(self, event: events.Focus) -> None:
        self.has_focus = True

    async def on_blur(self, event: events.Blur) -> None:
        self.has_focus = False

    async def on_key(self, event: events.Key) -> None:
        """Handle key presses."""
        self.log(event)
        if event.key == "ctrl+h":
            self.text = self.text[:-1]
        elif event.key == "enter":
            # process input
            if self.callback:
                self.callback(self.text)
            self.text = ""
        elif len(event.key) == 1:
            self.text += str(event.key)

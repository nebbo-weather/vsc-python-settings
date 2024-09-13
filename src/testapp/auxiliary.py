from typing import Callable


class Client:
    def __init__(self):
        self.name: str = "User"
        self.method: Callable

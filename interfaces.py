from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, position: tuple[int, int] = (0, 0)):
        self.position = position

    @abstractmethod
    def move_forward(self): ...

    @abstractmethod
    def jump(self): ...

    @abstractmethod
    def move_backward(self): ...

    @abstractmethod
    def move_down(self): ...


class Command(ABC):
    def __init__(self, character: Character):
        self.character = character

    @abstractmethod
    def execute(self):
        pass

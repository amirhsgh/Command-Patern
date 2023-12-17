from interfaces import Character


class GameCharacter(Character):

    def move_forward(self):
        x, y = self.position
        self.position = (x + 1, y)

    def jump(self):
        x, y = self.position
        self.position = (x, y + 1)

    def move_backward(self):
        x, y = self.position
        self.position = (x - 1, y)

    def move_down(self):
        x, y = self.position
        self.position = (x, y - 1)

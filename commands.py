from interfaces import Command


class MoveForwardCommand(Command):
    def execute(self):
        return self.character.move_forward()


# TODO: Implement all other character moving commands


class JumpCommand(Command):
    def execute(self):
        return self.character.jump()



class MoveBackwardCommand(Command):
    def execute(self):
        return self.character.move_backward()



class MoveDownCommand(Command):
    def execute(self):
        return self.character.move_down()

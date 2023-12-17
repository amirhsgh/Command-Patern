import unittest
from character import GameCharacter
from commands import *


class TestCommandPatterns(unittest.TestCase):
    def setUp(self):
        self.character = GameCharacter(position=(0, 0))

    def test_jump(self):
        command = JumpCommand(self.character)
        command.execute()
        self.assertEqual(self.character.position, (0, 1))

class Game:
    def __init__(self):
        pass


######################################################################################


import unittest


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        pass


if __name__ == "__main__":
    unittest.main()

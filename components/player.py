class Player:
    def __init__(self):
        pass

    def choose_piece(self, board):
        # dumb algorithm to pass tests
        piece_attrs = board.pool[0].attributes
        return piece_attrs

    def choose_location(self, board, attrs):
        location = [-1, -1]
        for x in range(4):
            for y in range(4):
                if board.location_open((x, y)):
                    location = (x, y)
                    return location

        raise ValueError("No open places on board!")


######################################################################################


import unittest
from board import Board


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player = Player()
        pass

    def test_choose_piece(self):
        attrs = self.player.choose_piece(self.board)
        self.assertEqual(len(attrs), 4)
        self.assertTrue(all([attr in [0, 1] for attr in attrs]))
        self.assertTrue(self.board.piece_in_pool(attrs))
        pass

    def test_choose_location(self):
        attrs = [0, 0, 0, 0]
        location = self.player.choose_location(self.board, attrs)
        self.assertEqual(len(location), 2)
        self.assertTrue(all([loc in range(4) for loc in location]))
        self.assertTrue(self.board.location_open(location))


if __name__ == "__main__":
    unittest.main()

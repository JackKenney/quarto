import numpy as np

import piece
from piece import Piece


class Board:
    def __init__(self):
        self.dim = 4
        self.move_count = 0
        self.pool = []
        for color in range(2):
            for height in range(2):
                for indent in range(2):
                    for shape in range(2):
                        self.pool.append(Piece(color, height, indent, shape))
        self.board = np.array([[None] * self.dim] * self.dim, dtype=Piece)
        pass

    def __eq__(self, other):
        dim = self.dim == other.dim
        move_count = self.move_count == other.move_count
        if len(self.pool) != len(other.pool):
            return False
        pool = np.equal(self.pool, other.pool).all()
        board = np.equal(self.board, other.board).all()
        return dim and move_count and pool and board

    def piece_in_pool(self, color, height, indent, shape):
        comparison_piece = Piece(color, height, indent, shape)
        for pi in self.pool:
            if pi == comparison_piece:
                return True
        return False

    def place_piece(self, color, height, indent, shape, x, y):
        """Returns true if piece placed successfully false if piece unavailable."""
        if not self.piece_in_pool(color, height, indent, shape):
            return False
        pi_to_place = None
        for pi in self.pool:
            if pi == Piece(color, height, indent, shape):
                self.pool.remove(pi)
                pi_to_place = pi
                break
        self.board[x][y] = pi_to_place
        self.move_count += 1
        return True

    def check_finished(self):
        # moves
        if self.move_count == self.dim ** 2:
            return True
        # rows
        for row in range(self.dim):
            if Piece.matching_set(self.board[row]):
                return True
        # cols
        for col in range(self.dim):
            if Piece.matching_set(self.board[:, col]):
                return True
        # diags
        diag_set = []
        for space in range(self.dim):
            diag_set.append(self.board[space, space])
        if Piece.matching_set(diag_set):
            return True
        # failure
        return False


######################################################################################

import unittest


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        pass

    def test_init(self):
        self.assertEqual(len(self.board.pool), 16)
        self.assertEqual(len(self.board.board), 4)
        self.assertEqual(len(self.board.board[0]), 4)
        self.assertEqual(len(self.board.board[3]), 4)
        pass

    def test_piece_in_pool(self):
        self.assertTrue(self.board.piece_in_pool(0, 0, 0, 0))
        temp = self.board.pool[0]
        self.board.pool = self.board.pool[1:]
        self.assertFalse(self.board.piece_in_pool(0, 0, 0, 0))
        self.board.pool = [temp] + self.board.pool
        pass

    def test_place_piece(self):
        self.board.place_piece(0, 0, 0, 0, x=0, y=0)
        self.assertTrue(self.board.board[0][0])
        self.assertEqual(self.board.move_count, 1)
        pass

    def test_check_finished(self):
        self.assertFalse(self.board.check_finished())
        self.board.place_piece(0, 0, 0, 0, x=0, y=0)
        self.board.place_piece(0, 0, 0, 1, x=1, y=0)
        self.board.place_piece(0, 0, 1, 0, x=2, y=0)
        self.board.place_piece(0, 0, 1, 1, x=3, y=0)
        self.assertTrue(self.board.check_finished())
        pass

    def test_equal(self):
        board_a = Board()
        board_b = Board()

        self.assertTrue(board_a == board_b)
        board_a.place_piece(0, 0, 0, 1, 0, 1)
        self.assertFalse(board_a == board_b)
        pass


if __name__ == "__main__":
    unittest.main()

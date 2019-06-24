import numpy as np


class Piece:
    # attribute options
    DARK = 0
    LIGHT = 1
    ROUND = 0
    SQUARE = 1
    SHORT = 0
    TALL = 1
    FLAT = 0
    HOLE = 1

    def __init__(self, color, height, indent, shape):
        accepted = [0, 1]
        assert color in accepted
        assert shape in accepted
        assert height in accepted
        assert indent in accepted

        self.attributes = np.array([color, height, indent, shape])

    @classmethod
    def matching_set(cls, piece_array):
        try:
            attributes = [pi.attributes for pi in piece_array]
        except (AttributeError):
            return False

        total = np.sum(attributes, axis=0)
        for attribute in total:
            if attribute == len(piece_array) or attribute == 0:
                return True
        return False

    @classmethod
    def equal(cls, pi_a, pi_b):
        if all(pi_a.attributes == pi_b.attributes):
            return True
        return False


######################################################################################

import unittest


class TestPiece(unittest.TestCase):
    def setUp(self):
        self.piece = Piece(0, 0, 0, 0)
        pass

    def test_attributes(self):
        pi = Piece(
            color=Piece.DARK, height=Piece.SHORT, indent=Piece.FLAT, shape=Piece.ROUND
        )
        self.assertEqual(pi.attributes[0], 0)
        self.assertEqual(pi.attributes[1], 0)
        self.assertEqual(pi.attributes[2], 0)
        self.assertEqual(pi.attributes[3], 0)
        pass

    def test_equal(self):
        a = Piece(0, 0, 0, 0)
        b = Piece(0, 0, 0, 0)
        c = Piece(0, 0, 0, 1)
        self.assertTrue(Piece.equal(a, b))
        self.assertFalse(Piece.equal(a, c))
        self.assertFalse(Piece.equal(b, c))
        pass

    def test_matching_set(self):
        matching_pieces = []
        for color in range(2):
            for height in range(2):
                for indent in range(2):
                    matching_pieces.append(Piece(color, height, indent, 0))
        self.assertTrue(Piece.matching_set(matching_pieces))
        matching_pieces.append(None)
        self.assertFalse(Piece.matching_set(matching_pieces))

        mismatched_pieces = []
        for attr in range(2):
            mismatched_pieces.append(Piece(attr, attr, attr, attr))
        self.assertFalse(Piece.matching_set(mismatched_pieces))
        pass


if __name__ == "__main__":
    unittest.main()

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

    def __init__(self, attrs):
        accepted = [0, 1]
        assert len(attrs) == 4
        assert all([attr in accepted for attr in attrs])
        self.attributes = np.array(attrs)

    def __eq__(self, other):
        if all(self.attributes == other.attributes):
            return True
        return False

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


######################################################################################

import unittest


class TestPiece(unittest.TestCase):
    def setUp(self):
        self.piece = Piece([0, 0, 0, 0])
        pass

    def test_attributes(self):
        pi = Piece([Piece.DARK, Piece.SHORT, Piece.FLAT, Piece.ROUND])
        self.assertEqual(pi.attributes[0], 0)
        self.assertEqual(pi.attributes[1], 0)
        self.assertEqual(pi.attributes[2], 0)
        self.assertEqual(pi.attributes[3], 0)
        pass

    def test_equal(self):
        a = Piece([0, 0, 0, 0])
        b = Piece([0, 0, 0, 0])
        c = Piece([0, 0, 0, 1])
        self.assertTrue(a == b)
        self.assertFalse(a == c)
        self.assertFalse(b == c)
        pass

    def test_matching_set(self):
        matching_pieces = []
        for color in range(2):
            for height in range(2):
                for indent in range(2):
                    matching_pieces.append(Piece([color, height, indent, 0]))
        self.assertTrue(Piece.matching_set(matching_pieces))
        matching_pieces.append(None)
        self.assertFalse(Piece.matching_set(matching_pieces))
        pass

    def test_mismatched_set(self):
        mismatched_pieces = []
        for attr in range(2):
            mismatched_pieces.append(Piece([attr, attr, attr, attr]))
        self.assertFalse(Piece.matching_set(mismatched_pieces))
        pass


if __name__ == "__main__":
    unittest.main()

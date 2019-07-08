from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(), Player()]
        self.winner = None
        self.last_player = len(self.players) - 1
        pass

    def next_player(self):
        player = self.last_player + 1
        if player >= len(self.players):
            player = 0
        return player

    def make_move(self):
        placer = self.players[self.last_player]
        picker = self.players[self.next_player()]
        valid_move = False
        while not valid_move:
            piece_attrs = picker.choose_piece(self.board)
            location = placer.choose_location(self.board, piece_attrs)
            # compare boards
            in_pool = self.board.piece_in_pool(piece_attrs)
            location_open = self.board.location_open(location)
            if in_pool and location_open:
                placed = self.board.place_piece(piece_attrs, location)
                if placed:
                    valid_move = True

        if self.board.game_over():
            self.winner = self.last_player


######################################################################################


import unittest


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        pass

    def test_init(self):
        self.assertTrue(all(self.game.players))
        self.assertTrue(self.game.board)
        self.assertTrue(self.game.board.move_count == 0)
        pass

    def test_make_move(self):
        self.assertEqual(self.game.board.move_count, 0)
        self.game.make_move()
        self.assertEqual(self.game.board.move_count, 1)
        pass

    def test_full_game(self):
        for move in range(16):
            self.assertEqual(self.game.board.move_count, move)
            self.game.make_move()
            self.assertEqual(self.game.board.move_count, move + 1)
        self.assertTrue(self.game.winner)
        print("Winner is player", self.game.winner)
        pass


if __name__ == "__main__":
    unittest.main()

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

    def make_move(self, player_number=None):
        player = self.next_player() if not player_number else player_number
        player = self.players[player]
        proposed_board = player.choose_piece(self.board)
        # compare boards
        pass

    def over(self):
        pass


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
        player = 0
        for move in range(16):
            self.assertEqual(self.game.board.move_count, move)
            self.game.make_move(player)
            self.assertEqual(self.game.board.move_count, move + 1)
            player = 1 if player == 0 else 0
        self.assertTrue(self.game.over())
        print(self.game.winner)
        pass


if __name__ == "__main__":
    unittest.main()

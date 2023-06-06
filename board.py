import numpy as np
from constants import *


class Board:
    def __init__(self):
        self.inner_board = np.empty((ROWS, COLS), dtype=str)

    def is_valid_move(self, row, col):
        return self.inner_board[row][col] == ""

    def is_full(self):
        return np.count_nonzero(np.char.equal(self.inner_board, '')) == 0

    def is_winner(self, player):
        # Check rows
        for row in range(ROWS):
            if all(cell == player for cell in self.inner_board[row]):
                return player, ("row", row)

        # Check columns
        for col in range(COLS):
            if all(self.inner_board[row][col] == player for row in range(ROWS)):
                return player, ("col", col)

        # Check diagonals
        if all(self.inner_board[i][i] == player for i in range(ROWS)):
            return player, ("diagonal", "desc")
        elif all(self.inner_board[i][ROWS - i - 1] == player for i in range(ROWS)):
            return player, ("diagonal", "asc")

        return 0, None

    def get_available_moves(self):
        return [(row, col) for row in range(ROWS) for col in range(COLS) if self.inner_board[row][col] == '']

    def make_move(self, row, col, player):
        self.inner_board[row][col] = player

    def undo_move(self, row, col):
        self.inner_board[row][col] = ""

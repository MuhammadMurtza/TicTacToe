import random


class Player:
    def __init__(self, player_symbol):
        self.player_symbol = player_symbol

    def get_best_random_move(self, board):
        random_value = random.randint(1, 10)

        if random_value % 2 == 0:
            return self.get_best_move(board)
        else:
            return self.get_random_move(board)

    def get_random_move(self, board):
        available_moves = board.get_available_moves()
        random_move = random.randrange(0, len(available_moves))
        row, col = available_moves[random_move]
        return row, col

    def get_best_move(self, board):
        best_score = float('-inf')
        best_move = None

        available_moves = board.get_available_moves()

        for move in available_moves:
            row, col = move
            board.make_move(row, col, self.player_symbol)
            score = self.minimax(board, 0, False)
            board.undo_move(row, col)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, board, depth, is_maximizing, alpha=float('-inf'), beta=float('inf')):
        player_symbol = self.player_symbol if is_maximizing else self.get_opponent_symbol()

        if board.is_winner(self.player_symbol)[0]:
            return 1
        elif board.is_winner(self.get_opponent_symbol())[0]:
            return -1
        elif board.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for move in board.get_available_moves():
                row, col = move
                board.make_move(row, col, player_symbol)
                score = self.minimax(board, depth + 1, False, alpha, beta)
                board.undo_move(row, col)
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        else:
            best_score = float('inf')
            for move in board.get_available_moves():
                row, col = move
                board.make_move(row, col, player_symbol)
                score = self.minimax(board, depth + 1, True, alpha, beta)
                board.undo_move(row, col)
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break

        return best_score

    def get_opponent_symbol(self):
        return "O" if self.player_symbol == "X" else "X"

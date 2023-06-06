from board import Board


class Game:
    def __init__(self, human_player, ai_player, renderer):
        self.human_player = human_player
        self.ai_player = ai_player
        self.renderer = renderer
        self.board = Board()
        self.current_player = self.human_player

    def evaluate_move(self, row, col):
        if self.board.is_valid_move(row, col):
            self.board.make_move(row, col, self.current_player.player_symbol)
            self.renderer.draw_figure(row, col, self.current_player.player_symbol)
            self.toggle_player()

    def toggle_player(self):
        self.current_player = self.ai_player if self.current_player == self.human_player else self.human_player

    def is_over(self):
        player, line = self.board.is_winner(self.human_player.player_symbol)
        if player:
            self.renderer.draw_winner_line(player, line)
            return True
        player, line = self.board.is_winner(self.ai_player.player_symbol)
        if player:
            self.renderer.draw_winner_line(player, line)
            return True
        return self.board.is_full()

    def restart_game(self):
        self.board.__init__()
        self.current_player = self.human_player
        self.renderer.draw_lines()
        self.renderer.update_screen()

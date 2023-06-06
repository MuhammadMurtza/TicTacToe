import pygame
from player import Player
from constants import *
from game_logic import Game
from renderer import Renderer

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic Tac Toe (Easy Mode)')
    human_player = Player("O")
    ai_player = Player("X")
    renderer = Renderer(screen, GameMode.EASY)
    game = Game(human_player, ai_player, renderer)
    renderer.draw_lines()

    while True:
        row, col = renderer.handle_events()
        if renderer.restart_flag:
            game.restart_game()
            renderer.restart_flag = False
        elif not game.is_over():
            if row is not None and col is not None:
                game.evaluate_move(row, col)
            elif game.current_player == ai_player:
                renderer.update_screen()
                pygame.time.delay(500)
                if renderer.game_mode == GameMode.EASY:
                    pygame.display.set_caption('Tic Tac Toe (Easy Mode)')
                    row, col = ai_player.get_random_move(game.board)
                elif renderer.game_mode == GameMode.MEDIUM:
                    pygame.display.set_caption('Tic Tac Toe (Medium Mode)')
                    row, col = ai_player.get_best_random_move(game.board)
                elif renderer.game_mode == GameMode.HARD:
                    pygame.display.set_caption('Tic Tac Toe (Hard Mode)')
                    row, col = ai_player.get_best_move(game.board)
                game.evaluate_move(row, col)

        renderer.update_screen()

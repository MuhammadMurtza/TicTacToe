import sys
import pygame
from constants import *


class Renderer:
    def __init__(self, screen, game_mode):
        self.screen = screen
        self.restart_flag = False
        self.game_mode = game_mode

    def draw_lines(self):
        self.screen.fill(BG_COLOR)
        pygame.draw.line(self.screen, LINE_COLOR, (SQUARESPACE, 0), (SQUARESPACE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (WIDTH - SQUARESPACE, 0), (WIDTH - SQUARESPACE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARESPACE), (WIDTH, SQUARESPACE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, HEIGHT - SQUARESPACE), (WIDTH, HEIGHT - SQUARESPACE), LINE_WIDTH)

    def draw_figure(self, row, col, player_symbol):
        if player_symbol == "X":
            x = col * SQUARESPACE + SQUARESPACE // 2
            y = row * SQUARESPACE + SQUARESPACE // 2
            start_pos = (x - RADIUS, y - RADIUS)
            end_pos = (x + RADIUS, y + RADIUS)
            pygame.draw.line(self.screen, CROSS_COLOR, start_pos, end_pos, CROSS_WIDTH)
            start_pos = (x + RADIUS, y - RADIUS)
            end_pos = (x - RADIUS, y + RADIUS)
            pygame.draw.line(self.screen, CROSS_COLOR, start_pos, end_pos, CROSS_WIDTH)
        else:
            center = (col * SQUARESPACE + SQUARESPACE // 2, row * SQUARESPACE + SQUARESPACE // 2)
            pygame.draw.circle(self.screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)

    def draw_winner_line(self, player_symbol, line):
        if line is None:
            return
        color = CROSS_COLOR if player_symbol == "X" else CIRCLE_COLOR
        if line[0] == "row":
            row = line[1]
            start_pos = (0, (row + 0.5) * SQUARESPACE)
            end_pos = (WIDTH, (row + 0.5) * SQUARESPACE)
            pygame.draw.line(self.screen, color, start_pos, end_pos, LINE_WIDTH)
        elif line[0] == "col":
            col = line[1]
            start_pos = ((col + 0.5) * SQUARESPACE, 0)
            end_pos = ((col + 0.5) * SQUARESPACE, HEIGHT)
            pygame.draw.line(self.screen, color, start_pos, end_pos, LINE_WIDTH)
        elif line[0] == "diagonal":
            if line[1] == "asc":
                start_pos = (0, HEIGHT)
                end_pos = (WIDTH, 0)
            elif line[1] == "desc":
                start_pos = (0, 0)
                end_pos = (WIDTH, HEIGHT)
            pygame.draw.line(self.screen, color, start_pos, end_pos, LINE_WIDTH)

    def set_game_mode(self, game_mode):
        self.game_mode = game_mode
        print(f"Game mode set to {game_mode}.")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // SQUARESPACE
                col = event.pos[0] // SQUARESPACE
                return row, col
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.restart_flag = True
                elif event.key == pygame.K_e:
                    self.set_game_mode(GameMode.EASY)
                elif event.key == pygame.K_m:
                    self.set_game_mode(GameMode.MEDIUM)
                elif event.key == pygame.K_h:
                    self.set_game_mode(GameMode.HARD)
        return None, None

    def update_screen(self):
        pygame.display.update()

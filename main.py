from __future__ import absolute_import, division, print_function
import sys, time, math, random, os
import numpy as np
from game import Game
from connect4ai import AI

random.seed(0)

ROW_COUNT = 6
COL_COUNT = 7
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE/2 - 5)
BOARD_SIZE_HEIGHT = SQUARE_SIZE * COL_COUNT
BOARD_SIZE_WIDTH = SQUARE_SIZE * ROW_COUNT

PADDING = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class GameRunner:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Connect 4")
        self.surface = pygame.display.set_mode((BOARD_SIZE_HEIGHT, BOARD_SIZE_WIDTH), 0, 32)
        self.gameoverfont = pygame.font.SysFont("arial", 70)
        self.restartfont = pygame.font.SysFont("arial", 25)
        self.player = 1
        
        self.game = Game()
        self.auto = False
    
    def loop(self):
        while True:
            game_over = self.game.game_over(1) or self.game.game_over(2)
            if game_over:
                self.auto = False
            
            column = None
            for event in pygame.event.get():
                if not game_over:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, _ = pygame.mouse.get_pos()
                        player_col = (x % 1000) // 100
                        #print(posY)
                        if not self.auto and self.game.can_place(player_col):
                            if self.player == 1:
                                self.game.place(player_col, self.player)
                                self.player = 2
                            else:
                                self.game.place(player_col, self.player)
                                self.player = 1
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.auto = not self.auto
                    if event.key == pygame.K_r:
                        self.game.set_state()
                        self.auto = False
                    #if event.key == pygame.K_s: (**optional**)
                    #    self.game.save_state()
                    #elif event.key == pygame.K_l: (**optional**)
                    #    self.game.load_state()
                    #elif event.key == pygame.K_u: (**optional**)
                    #    self.game.undo()
            
            if self.auto and not game_over:
                ai = AI(self.game.current_state())
                column = ai.compute_decision()

            if column != None:
                self.game.dropPiece(column)
            
            self.print_board()
            if game_over:
                self.print_game_over()
            pygame.display.update()

    # prints the board of the game
    def print_board(self):
        board = self.game.matrix
        for col in range(COL_COUNT):
            for row in range(ROW_COUNT):
                pygame.draw.rect(self.surface, BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.circle(self.surface, BLACK, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    
        for col in range(COL_COUNT):
            for row in range(ROW_COUNT):
                if board[col][row] == 1:
                    pygame.draw.circle(self.surface, RED, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
                elif board[col][row] == 2:
                    pygame.draw.circle(self.surface, YELLOW, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    def draw_label_hl(self, pos, label, padding=PADDING, bg=WHITE, wd=2, border=True):
        specs = [(bg, 0)]
        if border:
            specs += [(BLACK, wd)]
        for color, width in specs:
            pygame.draw.rect(self.surface, color,
                (pos[0] - padding, pos[1] - padding, label.get_width() + padding * 2, label.get_height() + padding * 2), width)

    # lets user know that the game is over
    def print_game_over(self):
        game_over_label = self.gameoverfont.render("Game Over!", 1, BLACK, WHITE)
        restart_label = self.restartfont.render("Press r to restart!", 1, BLACK, WHITE)

        for lbl, pos in [ (game_over_label, (160, 200)), (restart_label, (253, 400))]:
            self.draw_label_hl(pos, lbl)
            self.surface.blit(lbl, pos)
                

if __name__ == '__main__':
    import pygame
    from pygame.locals import *
    game = GameRunner()
    game.loop()

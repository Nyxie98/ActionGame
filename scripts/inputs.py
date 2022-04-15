import pygame, sys
from pygame.locals import *

class Input():
    def __init__(self, game):
        self.game = game
    
    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.game.world.player.rmove = True
                    self.game.world.player.left = False
                if event.key == K_LEFT:
                    self.game.world.player.lmove = True
                    self.game.world.player.left = True
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.game.world.player.rmove = False
                if event.key == K_LEFT:
                    self.game.world.player.lmove = False
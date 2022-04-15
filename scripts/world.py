import pygame
from scripts.player import Player

class World():
    def __init__(self, game):
        self.player = Player()
        self.renderer = game.renderer
        self.renderer.add_object(self.player)

    def update(self):
        self.player.update()
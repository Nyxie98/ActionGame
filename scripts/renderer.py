import pygame

class Renderer():
    def __init__(self, game):
        self.group = pygame.sprite.Group()
        self.surface = pygame.Surface((400, 300))
        self.game = game
        self.display = self.game.screen.display
    
    def add_object(self, obj):
        self.group.add(obj)
    
    def update(self):
        self.surface.fill((0,0,0))

        for entity in self.group:
            self.surface.blit(entity.rsurf, entity.rect)

        self.display.blit(pygame.transform.scale(self.surface, self.game.screen.size), (0,0))
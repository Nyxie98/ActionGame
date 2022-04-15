import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__() 
        self.position = {
            'x': 30,
            'y': 30
        }
        self.lmove = False
        self.rmove = False
        self.speed = 2
        self.left = False

        self.surf = pygame.image.load("assets/Player/Stand.png").convert()
        self.surf.set_colorkey((255,255,255))
        self.rsurf = self.surf
        self.rect = self.surf.get_rect(center = (self.position['x'], self.position['y']))
        self.name = "Player"

    def update(self):
        if self.lmove:
            self.position['x'] -= self.speed
        elif self.rmove:
            self.position['x'] += self.speed
        
        self.rsurf = pygame.transform.flip(self.surf, self.left, False) 

        self.rect = self.surf.get_rect(center = (self.position['x'], self.position['y']))
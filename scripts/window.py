import pygame

class Window():
    def __init__(self, width: int, height: int, caption: str):
        self.size = (width, height)
        self.caption = caption
        pygame.init()
        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(caption)

    def update(self) -> None:
        pygame.display.update()
        pygame.time.Clock().tick(60)
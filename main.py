from scripts.window import Window
from scripts.inputs import Input
from scripts.renderer import Renderer
from scripts.world import World

class Game():
    def __init__(self):
        self.screen = Window(800, 600, "Game")
        self.input = Input(self)
        self.renderer = Renderer(self)
        self.world = World(self)

    def update(self):
        self.input.update()
        self.world.update()
        self.renderer.update()
        self.screen.update()

    def run(self):
        while True:
            self.update()

if __name__ == "__main__":
    Game().run()
import sys
#esto es para descargar el pygame en caso de que no se tenga
try:
    import pygame
except ImportError:
    print("Pygame not found, installing pygame")
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
        import pygame
    except Exception as e:
        print("Failed to install pygame",e )
        sys.exit(1)

from settings import * 
from level import Level
from debug import *

  

        
class Game:
    def __init__(self):

        #General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Forest Keepers')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__== '__main__':
    game = Game()
    game.run()

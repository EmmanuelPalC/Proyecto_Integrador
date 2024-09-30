import pygame, sys
from button import Button
from settings import * 
from level import Level
from debug import *

pygame.init()

SCREEN = pygame.display.set_mode((960, 620))
pygame.display.set_caption("Forest Keepers")

BG = pygame.image.load("assets\menu\Menu_1.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/menu/font.ttf", size)

def play():
    while True:

        SCREEN.fill("black")
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
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                self.level.toggle_menu()
                    
                    self.screen.fill('black')
                    self.level.run()
                    pygame.display.update()
                    self.clock.tick(FPS)

        if __name__== '__main__':
            game = Game()
            game.run()

        
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("brown")
        
        

        OPTIONS_TEXT = get_font(15).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 90))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_AUDIO = Button(image=None, pos=(500, 150), 
                            text_input="AUDIO", font=get_font(15), base_color="Black", hovering_color="Green")

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_AUDIO.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_AUDIO.update(SCREEN)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_BUTTON = Button(image=pygame.image.load("assets\menu\Play Rect.png"), pos=(500, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets\menu\Options Rect.png"), pos=(500, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets\menu\Quit Rect.png"), pos=(500, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
import pygame
from settings import *
import turtle

class UI:
    def __init__(self):
        # General setup
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        
        # Bar setup
        self.health_bar_rect = pygame.Rect(50, 20, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(50, 75, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # Load images to place over the health and energy bars
        self.heart_image = pygame.image.load('assets/Barras/animacion_barra_vida/Barra de vida1.5_0007.png').convert_alpha()
        self.heart_image = pygame.transform.scale(self.heart_image, (218, 50))  # Resize as needed
        
        self.energy_image = pygame.image.load('assets/Barras/anmacion_barra_tiempo/Barra de Tiempo1_0007.png').convert_alpha()
        self.energy_image = pygame.transform.scale(self.energy_image, (218, 50))  # Resize as needed

    def show_bar(self, current, max_amount, bg_rect, color):
        # Draw the background
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # Converting stat to pixels
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # Drawing the bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def show_exp(self,exp):
        text_surf = self.font.render(str(int(exp)),False,TEXT_COLOR)
        x = self.display_surface.get_size()[0] -20
        y = self.display_surface.get_size()[1] -20
        text_rect = text_surf.get_rect(bottomright = (x,y))

        self.display_surface.blit(text_surf,text_rect)

    def display(self, player):
        # Display health and energy bars
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)
        self.show_exp(player.exp)

        # Display the heart image over the health bar
        heart_position = (self.health_bar_rect.left - 40, self.health_bar_rect.centery - 30)  # Adjust position as needed
        self.display_surface.blit(self.heart_image, heart_position)

        # Display the energy image over the energy bar
        energy_position = (self.energy_bar_rect.left - 40, self.energy_bar_rect.centery - 30)  # Adjust position as needed
        self.display_surface.blit(self.energy_image, energy_position)



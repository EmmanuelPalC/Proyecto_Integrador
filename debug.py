import pygame
pygame.init()
font = pygame.font.Font(None,30)

def debug(info,y = 10, x = 10):
    display_surface = pygame.display.get_surface()
    debuf_surf = font.render(str(info),True,'White')
    debug_rect = debuf_surf.get_rect(topleft = (x, y))
    pygame.draw.rect(display_surface,'Black',debug_rect)
    display_surface.blit(debuf_surf,debug_rect)
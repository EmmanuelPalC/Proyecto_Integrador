import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)
        direction = player.status.split('_')[0]


        #graphic
        if direction == 'left':
            self.image = pygame.image.load('assets\weapon\hammer\left.png').convert_alpha()
        elif direction == 'right':
            self.image = pygame.image.load('assets/weapon/hammer/right.png').convert_alpha()
        elif direction == 'up':
            self.image = pygame.image.load('assets/weapon/hammer/up.png').convert_alpha()
        else:
            self.image = pygame.image.load('assets/weapon/hammer/down.png').convert_alpha()
        
        #placement
        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(-55,-10))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(55,-10))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(0,-65))
        else:
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(0,70))
        

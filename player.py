import pygame
from settings import *
from support import import_folder
from level import *



class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups,obstacle_sprites,create_attack):
        super().__init__(groups)
        self.image = pygame.image.load('assets\player\down.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-20,-50)

        #graphics setup
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 5

        #movement
        self.direction = pygame.math.Vector2()
        self.speed = 20
        self.attacking = False
        self.attack_cooldowns = 400
        self.attack_time = None
        self.obstacle_sprites = obstacle_sprites
        
        #weapon
        self.create_attack = create_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
       

    def import_player_assets(self):
        character_path ='assets\player'
        self.animations= {'up':[],'down':[],'left':[],'right':[],
                          'down_idle':[],'up_idle':[],'right_idle':[],'left_idle':[],
                          'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()
        #movement input
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

        #attack input
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time= pygame.time.get_ticks()
            self.create_attack()

    def get_status(self):
        if self.direction.x == 0 and self.direction.y ==0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
            
            if self.attacking:
                self.direction.x = 0
                self.direction.y = 0
                if not 'attack' in self.status:
                    if 'idle' in self.status:
                        self.status = self.status.replace('_idle','_attack')
                    else:
                        self.status = self.status + '_attack'
            else:
                if 'attack' in self.status:
                    self.status = self.status.replace('_attack','_idle')
        
        if self.status == 'left':
            self.image = pygame.image.load('assets\player\left.png').convert_alpha()
        if self.status == 'right':
            self.image = pygame.image.load('assets/player/right.png').convert_alpha()
        if self.status == 'down':
            self.image = pygame.image.load('assets\player\down.png').convert_alpha()
        if self.status == 'up':
            self.image = pygame.image.load('assets/player/up.png').convert_alpha()
        if self.status == 'left_idle':
            self.image = pygame.image.load('assets\player\left.png').convert_alpha()
        if self.status == 'right_idle':
            self.image = pygame.image.load('assets/player/right.png').convert_alpha()
        if self.status == 'down_idle':
            self.image = pygame.image.load('assets\player\down.png').convert_alpha()
        if self.status == 'up_idle':
            self.image = pygame.image.load('assets/player/up.png').convert_alpha()
        if self.status == 'right_attack':
            self.image = pygame.image.load('assets/player/ataque_derecha_0002.png').convert_alpha()
        if self.status == 'left_attack':
            self.image = pygame.image.load('assets/player/ataque_izquierda_0002.png').convert_alpha()
        if self.status == 'down_attack':
            self.image = pygame.image.load('assets/player/ataque_animación_0002.png').convert_alpha()
        if self.status == 'up_attack':
            self.image = pygame.image.load('assets/player/ataque_trasero_0002.png').convert_alpha()
        

        




    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed   
        self.collision('horizontal')   
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')    
        self.rect.center = self.hitbox.center 

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom
   
    def cooldowns(self):
        current_time=pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >=self.attack_cooldowns:
                self.attacking = False

    def animate(self):
        animation = self.animations[self.status]

        #loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        #set the image
        self.image = animation[self.frame_index]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.move(self.speed)
        

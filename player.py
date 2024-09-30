import pygame
import sys
from settings import *
from support import import_folder
from level import *
from entity import Entity



class Player(Entity):
    def __init__(self, pos, groups,obstacle_sprites,create_attack,destroy_attack):
        super().__init__(groups)
        self.image = pygame.image.load('assets\player\down.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-20,-50)

        #graphics setup
        self.import_player_assets()
        self.status = 'down'

        #movement
        self.speed = 20
        self.attacking = False
        self.attack_cooldowns = 5
        self.attack_time = None
        self.obstacle_sprites = obstacle_sprites
        
        #weapon
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]

        #stats
        self.stats = {'health': 100, 'energy': 500, 'attack':20}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
       
       #damage timer
        self.vulnerable = True
        self.hurt_time =None
        self.invulnerability_duration = 500
       

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

    def timer(self):
            if self.energy != 0:
                self.energy = self.energy - 1
            elif self.energy <= 0:
                self.image = pygame.image.load('assets/player/tired.png').convert_alpha()
                pygame.quit()
            if self.health <= 0:
                self.image = pygame.image.load('assets\player\death.png').convert_alpha()
                pygame.quit()
                

    
            
                

   
   
    def cooldowns(self):
        current_time=pygame.time.get_ticks()
        if self.attacking == True:
            if current_time - self.attack_time >=self.attack_cooldowns + weapon_data[self.weapon]['cooldown']:
                self.attacking = False
                self.destroy_attack()

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True

    def animate(self):
        animation = self.animations[self.status]

        #loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        #set the image
        self.image = animation[self.frame_index]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def get_full_weapon_damage(self):
        base_damage =  self.stats['attack']
        weapon_damage = weapon_data[self.weapon]['damage']
        return base_damage + weapon_damage

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.timer()
        self.move(self.speed)
        

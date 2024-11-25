import pygame
from settings import *
from entity import Entity

class Enemy3(Entity):
    def __init__(self,monster_name,pos,groups,obstacle_sprites,damage_player):

        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #graphics setup
        self.image = pygame.image.load('mapa3/pino_tronco.png').convert_alpha()

        #movement
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30,-30)
        self.obstacle_sprites = obstacle_sprites

        #stats
        self.monster_name = monster_name
        monster_info = monster_data['tree']
        self.health = monster_info['health']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        #player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 500
        self.damage_player = damage_player



    def import_graphics(self):
        self.animations = {'idle':[], 'move':[],'attack':[]}

    def get_player_distance_direction(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        
        return(distance,direction)

    def get_status(self,player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.image = pygame.image.load('mapa3\pino_tronco.png').convert_alpha()
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self,player):
        if self.status == 'attack':
            self.image = pygame.image.load('mapa3/pino_tronco.png').convert_alpha()
            if self.status == 'attack':
                self.attack_time = pygame.time.get_ticks()
                self.damage_player(self.attack_damage,self.attack_type)
                self.can_attack = False
                
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
            self.image = pygame.image.load('mapa3/pino_tronco.png').convert_alpha()
        else:
            self.direction = pygame.math.Vector2()
            self.image = pygame.image.load('mapa3/pino_tronco.png').convert_alpha()
        
    def cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

    def get_damage(self, player, attack_type):
        if attack_type == 'weapon':
            self.health = player.get_full_weapon_damage()

    def check_death(self):
        if self.health <=0:
            self.kill()

    def update(self):
        self.move(self.speed)
        self.cooldown()
    

    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)

 
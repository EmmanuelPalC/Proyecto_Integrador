import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from ui import UI
from enemy import Enemy
from menu_game import Upgrade


class Level:
    def __init__(self):

        #get the display surface
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False
        
        #sprite group setup
        self.visible_sprites = YsortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        #attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

        #user interface
        self.ui = UI()
        self.upgrade = Upgrade(self.player)

    def create_map(self):
        layout = {
            'boundary': import_csv_layout('assets\mapa\MAPAAAAA_boundaries.csv'),
            'bush1': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto.csv'),
            'bush2': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto_2.csv'),
            'bush3': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto_3.csv'),
            'bush4': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto_4.csv'),
            'entities1':import_csv_layout('assets\mapa\MAPAAAAA_entities.csv'),
        }


        for style,layout in layout.items():
            for row_index,row in enumerate(layout):
                    for col_index, col in enumerate(row):
                        if col != '-1':
                            x = col_index * TILESIZE
                            y = row_index * TILESIZE
                            if style == 'boundary':
                                Tile((x, y), [self.obstacles_sprites ],'invisible')
                            if style == 'bush1':
                                arbusto =pygame.image.load('assets/mapa/Art_PIXEL/PNG/arbusto.png')
                                Tile((650,400),[self.visible_sprites,self.obstacles_sprites],'bush1',arbusto)
                            if style == 'bush2':
                                arbusto =pygame.image.load('assets/mapa/Art_PIXEL/PNG/arbusto.png')
                                Tile((250,400),[self.visible_sprites,self.obstacles_sprites],'bush2',arbusto)
                            if style == 'bush3':
                                arbusto =pygame.image.load('assets/mapa/Art_PIXEL/PNG/arbusto.png')
                                Tile((650,200),[self.visible_sprites,self.obstacles_sprites],'bush3',arbusto)
                            if style == 'bush4':
                                arbusto =pygame.image.load('assets/mapa/Art_PIXEL/PNG/arbusto.png')
                                Tile((250,200),[self.visible_sprites,self.obstacles_sprites],'bush4',arbusto)


                            if style == 'entities1':
                                Enemy('bob',(x,y),[self.visible_sprites,
                                                   self.attackable_sprites],
                                                    self.obstacles_sprites,
                                                    self.damage_player)

                            
                                                     
        self.player = Player((450,280),[self.visible_sprites],self.obstacles_sprites,self.create_attack,self.destroy_attack)
       
    def create_attack(self):
        self.current_attack = Weapon(self.player ,[self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        target_sprite.kill()

    def damage_player(self,amount,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
               

    def toggle_menu(self):

        self.game_paused = not self.game_paused

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)
        if self.game_paused:
            self.upgrade.display()

            #display menu
        else:
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.player_attack_logic()
        #update and draw the game
        
        
       
        
        
        

class YsortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] //2
        self.half_height = self.display_surface.get_size()[1] //2
        self.offset = pygame.math.Vector2()

        #creating the floor
        self.floor_surf=pygame.image.load('assets\mapa\MAPAAAAA.png').convert()
        self.floor_rect=self.floor_surf.get_rect(topleft=(0,0))

    def custom_draw(self, player):
        #getting the offset
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image,sprite.rect)

        #drawing the floor
        floor_offset_pos=self.floor_rect.topleft -self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite:sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
        
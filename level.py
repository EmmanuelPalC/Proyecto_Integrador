import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon


class Level:
    def __init__(self):

        #get the display surface
        self.display_surface = pygame.display.get_surface()
        
        #sprite group setup
        self.visible_sprites = YsortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

    def create_map(self):
        layout = {
            'boundary': import_csv_layout('assets\mapa\MAPAAAAA_boundaries.csv'),
            'bush1': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto.csv'),
            'bush2': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto_2.csv'),
            'bush3': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto_3.csv'),
            'bush4': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto_4.csv'),
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
                            
                            if style == 'object':
                                surf = graphics['objects'][int(col)]
                                Tile((x,y),[self.visible_sprites,self.obstacles_sprites],'object',surf)
                            
                            self.player = Player((450,280),[self.visible_sprites],self.obstacles_sprites, self.create_attack)
       
    def create_attack(self):
        Weapon(self.player ,[self.visible_sprites])

    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.status)
        

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

        
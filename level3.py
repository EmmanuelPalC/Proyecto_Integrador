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
from enemy2 import Enemy2
from enemy3 import Enemy3
from player2 import Player2
from player3 import Player3
from menu_game import Upgrade


class Level3:
    def __init__(self):

        #get the display surface
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False
        
        self.total_enemies = 10
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
            'boundary': import_csv_layout('mapa3/MAPA3_boundaries.csv'),
            'bush1': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto.csv'),
            'bush2': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto_2.csv'),
            'bush3': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto_3.csv'),
            'bush4': import_csv_layout('assets/mapa/arbusto/MAPAAAAA_arbusto_4.csv'),
            'entities3':import_csv_layout('mapa3/MAPA3_entities.csv'),
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
                                Tile((650,400),[],'bush1',arbusto)
                            if style == 'bush2':
                                arbusto =pygame.image.load('assets/mapa/Art_PIXEL/PNG/arbusto.png')
                                Tile((250,400),[],'bush2',arbusto)
                            if style == 'bush3':
                                arbusto =pygame.image.load('assets/mapa/Art_PIXEL/PNG/arbusto.png')
                                Tile((650,200),[],'bush3',arbusto)
                            if style == 'bush4':
                                arbusto =pygame.image.load('assets/mapa/Art_PIXEL/PNG/arbusto.png')
                                Tile((250,200),[],'bush4',arbusto)


                            if style == 'entities3':
                                Enemy3('fire',(x,y),[self.visible_sprites,
                                                   self.attackable_sprites],
                                                    self.obstacles_sprites,
                                                    self.damage_player)

                            
                                                     
        self.player = Player3((450,280),[self.visible_sprites],self.obstacles_sprites,self.create_attack,self.destroy_attack)
       
    def create_attack(self):
        self.current_attack = Weapon(self.player ,[self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                    # Incrementar experiencia del jugador
                        self.player.exp += 1

                    # Guardar la posición del sprite eliminado
                        base_position = target_sprite.rect.center

                    # Definir el desplazamiento (offset)
                        offset_x = -10  # Cambia este valor según la dirección deseada
                        offset_y = -10  # Por ejemplo, hacia arriba y a la derecha
                        new_position = (base_position[0] + offset_x, base_position[1] + offset_y) 

                    # Eliminar el sprite objetivo
                        target_sprite.kill()

                    # Cargar la nueva imagen
                        new_image = pygame.image.load('mapa3/pino_chikito.png').convert_alpha()

                    # Crear un nuevo sprite utilizando la nueva imagen
                        new_sprite = Tile(new_position, [self.visible_sprites, self.obstacles_sprites], 'pino', new_image)


    def damage_player(self,amount,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
               

    def toggle_menu(self):

        self.game_paused = not self.game_paused

    def run(self):
        if self.game_over_condition():
            return  # Detiene el nivel en caso de Game Over
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

    def game_over_condition(self):
        """Comprueba si la salud del jugador ha llegado a cero o menos"""
        if self.player.health <= 0 or self.player.energy <= 0 :
            self.player_dead = True
            return True  # El jugador ha muerto
        return False  # El jugador sigue vivo
        
    def win_condition(self):
        """Verifica si el jugador ha ganado el nivel"""
        # Aquí verificamos si el número de enemigos derrotados alcanza el número total de enemigos
        if self.player.exp >= self.total_enemies:
            return True
        return False

        
       
        
        
        

class YsortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] //2
        self.half_height = self.display_surface.get_size()[1] //2
        self.offset = pygame.math.Vector2()

        #creating the floor
        self.floor_surf=pygame.image.load('mapa3/Mapa3.png').convert()
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
        
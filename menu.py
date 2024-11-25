import pygame, sys
from button import Button
from settings import * 
from level import Level
from level2 import Level2
from debug import *
import json

pygame.init()

SCREEN = pygame.display.set_mode((960, 620))
pygame.display.set_caption("Forest Keepers")

global game_over
game_over = False  # Variable global que indica si el jugador ha muerto

click_sound = pygame.mixer.Sound("assets/music/2.mp3")  
game_sound = pygame.mixer.Sound("assets/music/Pista1_Menu1.mp3")  
if not pygame.mixer.music.get_busy():  # Si no hay música sonando
        pygame.mixer.music.load("assets/music/Pista1_Menu1.mp3")  # Música de fondo
        pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.load("assets/music/Pista1_Menu1.mp3")  # Música de fondo

pygame.mixer.music.play(-1, 0.0)
# Control del volumen del efecto de sonido
click_sound.set_volume(0.2)  # Ajusta el volumen 
# Cargar las imágenes de las barras de volumen
VOLUME_BARS = [
    pygame.transform.scale(pygame.image.load("assets/botones/BotonesFinales/COMIC_mapa1_0001.png"), (200, 300)),
    pygame.image.load("assets/botones/BotonesFinales/COMIC_mapa1_0002.png"),
    pygame.image.load("assets/botones/BotonesFinales/COMIC_mapa1_0003.png"),
    pygame.image.load("assets/botones/BotonesFinales/COMIC_mapa1_0004.png"),
    pygame.image.load("assets/botones/BotonesFinales/COMIC_mapa1_0005.png")
]



# Fondos y recursos
#BG = pygame.image.load(f"assets/botones/{botones[idioma]['menu']}")
BG = pygame.image.load("assets/menu/Menu_Final.png")
OPTIONS_BG = pygame.image.load("assets/botones/BotonesFinales/Options_ingles.png")
OPCIONES_BG = pygame.image.load("assets/botones/BotonesFinales/Options_Español.png")
LANGUAGE_SCREEN = pygame.image.load("assets/menu/Menu_lenguage_Español.png")
LANGUAGE_SCREEN2 = pygame.image.load("assets/botones/BotonesFinales/Options_ingles_lan2.png")
HELP=pygame.image.load("assets/botones/Opciones_ayuda.png")
HELP2=pygame.image.load("assets/botones/BotonesFinales\Options_Help.png")
VOLUMEN=pygame.image.load("assets/botones/BotonesFinales/VOLFE.png")
VOLUMEN2=pygame.image.load("assets/botones/BotonesFinales/VOLFI.png")
GAMEOVER=pygame.image.load("assets/menu/Perdiste.png")
GAMEOVER2=pygame.image.load("assets/menu/gameover.png")


pygame.mixer.init()

fuente = pygame.font.Font(None, 74)
    
def __init__(self):
    self.font = pygame.font.Font(None, 74)

# Definición de la función de fuente
def get_font(size):
    return pygame.font.Font("assets/menu/font.ttf", size)

# Variable global para el idioma
idioma = "spanish" 



# Función para cargar botones según el idioma
def load_buttons():
    #with open("texto2.json", "r", encoding="utf-8") as archivo:
     #   botones = json.load(archivo)

    global idioma
    # Asegúrate de que las rutas sean correctas
    if idioma=="english":
        PLAY_BUTTON = Button(image=pygame.image.load("assets/botones/Play4.png"), pos=(140, 193), 
                         text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/botones/Options4.png"), pos=(148, 276), 
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/botones/Quit4.png"), pos=(140, 357), 
                         text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

    else:
        PLAY_BUTTON = Button(image=pygame.image.load("assets/botones/Jugar.png"), pos=(140, 193), 
                         text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/botones/Opciones.png"), pos=(148, 276), 
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/botones/Cerrar.png"), pos=(140, 357), 
                         text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

    return PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON



def help():
    global idioma
    while True:
        SCREEN.fill("black")
        if idioma=="spanish":
            SCREEN.blit(HELP, (0, 0))
        else:
            SCREEN.blit(HELP2, (0, 0))


        LANGUAGE_MOUSE_POS = pygame.mouse.get_pos()       
        BACK_BUTTON = Button(image=pygame.image.load("assets/botones/backFlecha.png"), pos=(220, 273), text_input="", font=get_font(40), base_color="Black", hovering_color="Green")
        BACK_BUTTON.changeColor(LANGUAGE_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(LANGUAGE_MOUSE_POS):
                    click_sound.play()
                    options()  # Regresa a las opciones si el usuario presiona "Back"

        pygame.display.update()

def volumen():
    global idioma
    volume = 1.0  # Volumen inicial

    while True:
        SCREEN.fill("black")
        
        
        if idioma=="spanish":
            SCREEN.blit(VOLUMEN, (0, 0))
        else:
            SCREEN.blit(VOLUMEN2, (0, 0))

        VOLUMEN_MOUSE_POS = pygame.mouse.get_pos()   
        INCREASE_BUTTON = Button(image=pygame.image.load("assets/botones/BotonesFinales/VOL+.png"), pos=(710, 395),  text_input="", font=get_font(40), base_color="Black", hovering_color="Green")
        DECREASE_BUTTON = Button(image=pygame.image.load("assets/botones/BotonesFinales/VOL-.png"), pos=(225, 395), text_input="", font=get_font(40), base_color="Black", hovering_color="Green")    
        BACK_BUTTON = Button(image=pygame.image.load("assets/botones/backFlecha.png"), pos=(219, 275), text_input="", font=get_font(40), base_color="Black", hovering_color="Green")
        BACK_BUTTON.changeColor(VOLUMEN_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)
        INCREASE_BUTTON.update(SCREEN)
        DECREASE_BUTTON.update(SCREEN)

          # Mostrar las barras de volumen en función del valor actual
        bar_index = int(volume * 5)  # Convertir el volumen a un índice entre 0 y 5
        for i in range(bar_index):
            SCREEN.blit(VOLUME_BARS[i], (350 + i * 40, 500))  # Coloca las barras de volumen


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(VOLUMEN_MOUSE_POS):
                    click_sound.play()
                    options()  # Regresa a las opciones si el usuario presiona "Back"
                if INCREASE_BUTTON.checkForInput(VOLUMEN_MOUSE_POS):
                    click_sound.play()
                    volume = min(1.0, volume + 0.2)  # Aumentar el volumen con un máximo de 1.0
                    game_sound.set_volume(volume)  # Cambiar volumen del sonido
                    pygame.mixer.music.set_volume(volume)  # Cambiar volumen de la música

                # Disminuir volumen
                if DECREASE_BUTTON.checkForInput(VOLUMEN_MOUSE_POS):
                    click_sound.play()
                    volume = max(0.0, volume - 0.2)  # Disminuir el volumen con un mínimo de 0.0
                    game_sound.set_volume(volume)
                    pygame.mixer.music.set_volume(volume)


        pygame.display.update()

# Función de la pantalla de selección de idioma
def language_selection():
    global idioma
    while True:
        SCREEN.fill("black")
        if idioma=="spanish":
            SCREEN.blit(LANGUAGE_SCREEN, (0, 0))
        else:
            SCREEN.blit(LANGUAGE_SCREEN2, (0, 0))

        LANGUAGE_MOUSE_POS = pygame.mouse.get_pos()

        # Crear los botones para seleccionar el idioma
        SPANISH_BUTTON = Button(image=pygame.image.load("assets/botones/BanderaMx.png"), pos=(603, 417), text_input="", font=get_font(50), base_color="Black", hovering_color="Green")
        ENGLISH_BUTTON = Button(image=pygame.image.load("assets/botones/BanderaUsa.png"), pos=(350, 417), text_input="", font=get_font(50), base_color="Black", hovering_color="Green")
        BACK_BUTTON = Button(image=pygame.image.load("assets/botones/backFlecha.png"), pos=(219, 275), text_input="", font=get_font(40), base_color="Black", hovering_color="Green")

        SPANISH_BUTTON.changeColor(LANGUAGE_MOUSE_POS)
        ENGLISH_BUTTON.changeColor(LANGUAGE_MOUSE_POS)
        BACK_BUTTON.changeColor(LANGUAGE_MOUSE_POS)

        SPANISH_BUTTON.update(SCREEN)
        ENGLISH_BUTTON.update(SCREEN)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SPANISH_BUTTON.checkForInput(LANGUAGE_MOUSE_POS):
                    click_sound.play()
                    idioma = "spanish"
                    print(f"Idioma seleccionado: {idioma}")
                    main_menu()  # Regresa al menú principal después de seleccionar el idioma
                if ENGLISH_BUTTON.checkForInput(LANGUAGE_MOUSE_POS):
                    click_sound.play()
                    idioma = "english"
                    print(f"Idioma seleccionado: {idioma}")
                    main_menu()  # Regresa al menú principal después de seleccionar el idioma
                if BACK_BUTTON.checkForInput(LANGUAGE_MOUSE_POS):
                    click_sound.play()
                    options()  # Regresa a las opciones si el usuario presiona "Back"

        pygame.display.update()



# Función de la pantalla de opciones
def options():
    global idioma
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        if idioma=="spanish":
            SCREEN.blit(OPCIONES_BG, (0, 0))
            OPTIONS_LANGUAGE = Button(image=pygame.image.load("assets/botones/Lenguage.png"), pos=(488, 374), 
                                  text_input="", font=get_font(25), base_color="Black", hovering_color="Green")
            OPTIONS_HELP = Button(image=pygame.image.load("assets/botones/Ayuda.png"), pos=(484, 430), 
                                  text_input="", font=get_font(25), base_color="Black", hovering_color="Green")
        else:
            SCREEN.blit(OPTIONS_BG, (0, 0))
            OPTIONS_LANGUAGE = Button(image=pygame.image.load("assets/botones/LanguageING.png"), pos=(488, 374), 
                                  text_input="", font=get_font(25), base_color="Black", hovering_color="Green")
            OPTIONS_HELP = Button(image=pygame.image.load("assets/botones/HelpING.png"), pos=(484, 430), 
                                  text_input="", font=get_font(25), base_color="Black", hovering_color="Green")


        OPTIONS_BACK = Button(image=pygame.image.load("assets/botones/backFlecha.png"), pos=(219, 275), 
                              text_input="", font=get_font(25), base_color="Black", hovering_color="Green")
        OPTIONS_VOLUMEN = Button(image=pygame.image.load("assets/botones/Volumen.png"), pos=(484, 310), 
                                  text_input="", font=get_font(25), base_color="Black", hovering_color="Green")
        

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_LANGUAGE.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_LANGUAGE.update(SCREEN)
        OPTIONS_HELP.update(SCREEN)
        OPTIONS_VOLUMEN.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    main_menu()
                if OPTIONS_LANGUAGE.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    language_selection()  # Ir a la pantalla de selección de idioma
                if OPTIONS_HELP.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    help()  
                if OPTIONS_VOLUMEN.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    volumen()  

        pygame.display.update()

# Función del menú principal
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Cargar los botones según el idioma actual
        PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON = load_buttons()

        # Cambiar el color de los botones
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_sound.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_sound.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_sound.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Función para jugar
WIDTH = 960
HEIGHT = 620



# Función para jugar con selector de niveles
def play():
    while True:
        global idioma
        SCREEN.fill("black")
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()

        # Fondos y textos para el selector de niveles
        SCREEN.blit(pygame.image.load("assets/botones/fondoNiveles.png"), (0, 0))
        LEVEL_1_BUTTON = Button(image=None, pos=(255, 360), 
                                 text_input="1", font=get_font(70), base_color="White", hovering_color="Green")
        LEVEL_2_BUTTON = Button(image=None, pos=(500, 350), 
                                 text_input="2", font=get_font(70), base_color="White", hovering_color="Green")
        LEVEL_3_BUTTON = Button(image=None, pos=(730, 350), 
                                 text_input="3", font=get_font(70), base_color="White", hovering_color="Green")
        
        if idioma=="spanish":
            BACK_BUTTON = Button(image=pygame.image.load("assets/Botones/BACKATRAS.png"), pos=(300, 550), 
                              text_input="", font=get_font(40), base_color="White", hovering_color="Green")
        else:
            BACK_BUTTON = Button(image=pygame.image.load("assets/Botones/BACKNIVELES.png"), pos=(300, 550), 
                              text_input="", font=get_font(40), base_color="White", hovering_color="Green")

        

        for button in [LEVEL_1_BUTTON, LEVEL_2_BUTTON, LEVEL_3_BUTTON, BACK_BUTTON]:
            button.changeColor(LEVEL_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_1_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    click_sound.play()
                    start_level(1)
                if LEVEL_2_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    click_sound.play()
                    start_level2(2)
                if LEVEL_3_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    click_sound.play()
                    start_level3(3)
                if BACK_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    click_sound.play()
                    main_menu()

        pygame.display.update()


def gameover():
    while True:
        
        
        SCREEN.fill(("black"))
        if idioma == "spanish":
            SCREEN.blit(GAMEOVER, (0, 0))
        else:
            SCREEN.blit(GAMEOVER2, (0, 0))

        GAMEOVER_MOUSE_POS = pygame.mouse.get_pos()
        
        # Crear botones para reiniciar o salir
        home_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/HOME.png"), pos=(280, 485), text_input="", font=get_font(50), base_color="White", hovering_color="Green")
        salir_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/salirr.png"), pos=(700, 487), text_input="", font=get_font(50), base_color="White", hovering_color="Green")
        RESTART_BUTTON = Button(image=pygame.image.load("assets/botones/BotonesFinales/RESTART.png"), pos=(495, 485), text_input="", font=get_font(40), base_color="White", hovering_color="Brown")
       
        
        RESTART_BUTTON.changeColor(GAMEOVER_MOUSE_POS)
        salir_button.changeColor(GAMEOVER_MOUSE_POS)
        
        # Actualizar los botones en la pantalla
        RESTART_BUTTON.update(SCREEN)
        salir_button.update(SCREEN)
        home_button.update(SCREEN)


        # Revisar eventos de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(GAMEOVER_MOUSE_POS):
                    click_sound.play()
                    return "restart"  # El jugador elige reiniciar
                if salir_button.checkForInput(GAMEOVER_MOUSE_POS):
                    click_sound.play()
                    pygame.quit()
                    sys.exit()
                if home_button.checkForInput(GAMEOVER_MOUSE_POS):
                    click_sound.play()
                    main_menu()

        pygame.display.update()

def win():
    while True:
        SCREEN.fill(("black"))
        WIN=pygame.image.load("assets/menu/Winfinal.png")
        WIN2=pygame.image.load("assets/menu/Ganastefinal.png")


        if idioma == "spanish":
            SCREEN.blit(WIN, (0, 0))
        else:
            SCREEN.blit(WIN2, (0, 0))

        WIN_MOUSE_POS = pygame.mouse.get_pos()
        
        # Crear botones para reiniciar o salir
        home_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/HOME.png"), pos=(280, 485), text_input="", font=get_font(50), base_color="White", hovering_color="Green")
        salir_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/salirr.png"), pos=(700, 487), text_input="", font=get_font(50), base_color="White", hovering_color="Green")
        RESTART_BUTTON = Button(image=pygame.image.load("assets/botones/BotonesFinales/RESTART.png"), pos=(495, 485), text_input="", font=get_font(40), base_color="White", hovering_color="Brown")
       
        
        RESTART_BUTTON.changeColor(WIN_MOUSE_POS)
        salir_button.changeColor(WIN_MOUSE_POS)
        
        # Actualizar los botones en la pantalla
        RESTART_BUTTON.update(SCREEN)
        salir_button.update(SCREEN)
        home_button.update(SCREEN)


        # Revisar eventos de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(WIN_MOUSE_POS):
                    click_sound.play()
                    return "restart"  # El jugador elige reiniciar
                if salir_button.checkForInput(WIN_MOUSE_POS):
                    click_sound.play()
                    pygame.quit()
                    sys.exit()
                if home_button.checkForInput(WIN_MOUSE_POS):
                    click_sound.play()
                    main_menu()

        pygame.display.update()


# Función para iniciar un nivel específico
def start_level(level):
    global idioma, game_over,win_game
    paused = False  # Variable que controla el estado de pausa
    level_game = Level()  # Crear una instancia del nivel
    win_game=False
    
    if not pygame.mixer.music.get_busy():  # Si no hay música sonando
        pygame.mixer.music.load("assets/music/Pista1_Menu1.mp3")  # Música de fondo
        pygame.mixer.music.play(-1, 0.0)

    # Botones de control (pausa, home, salir)
    if paused==False:
        pause_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/pausaa.png"), pos=(920, 50), text_input="", font=get_font(30), base_color="White", hovering_color="Green")
    
    home_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/HOME.png"), pos=(280, 370), text_input="", font=get_font(50), base_color="White", hovering_color="Green")
    salir_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/salirr.png"), pos=(650, 370), text_input="", font=get_font(50), base_color="White", hovering_color="Green")

    # Bucle principal del nivel
    while True:
        if game_over:
            pygame.mixer.music.stop()
            # Reproducir la música de "game over"
            pygame.mixer.music.load("assets/music/game-over-classic-206486.mp3")  # Música de Game Over
            pygame.mixer.music.play(0, 0.0)  # Reproducir una vez (0 indica no loop)
            # Llamar a la función de "game over" para mostrar la pantalla de Game Over
            result = gameover()
            if result == "restart":
                game_over = False
                start_level(level)  # Reinicia el nivel actual
                return  # Salir del bucle actual
            elif result == "exit":
                pygame.quit()
                sys.exit()  # Salir del juego

        if win_game:  # Verifica si el jugador ha ganado
            pygame.mixer.music.stop()  # Detiene la música de fondo
            return win()  # Llama a la pantalla de victoria
        
        pygame.display.set_caption(f"Forest Keepers - Nivel {level}")

        if not pygame.mixer.music.get_busy():  # Si no hay música sonando
            pygame.mixer.music.load("assets/music/Pista1_Menu1.mp3")  # Música de fondo
            pygame.mixer.music.play(-1, 0.0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused  # Alterna el estado de pausa

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if pause_button.checkForInput(mouse_pos):
                    click_sound.play()
                    paused = not paused  # Alterna el estado de pausa al presionar el botón de pausa

        if paused:
            # Muestra la pantalla de pausa
            if idioma == "spanish":
                SCREEN.blit(pygame.image.load("assets/botones/BotonesFinales/Pausa.png"), (0, 0))
            else:
                SCREEN.blit(pygame.image.load("assets/botones/BotonesFinales/Paused.png"), (0, 0))

            pause_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/RESUME.png"), pos=(470, 370), text_input="", font=get_font(30), base_color="White", hovering_color="Green")
            home_button.update(SCREEN)
            salir_button.update(SCREEN)
            pause_button.update(SCREEN)

            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if home_button.checkForInput(mouse_pos):
                            click_sound.play()
                            main_menu()
                        if salir_button.checkForInput(mouse_pos):
                            click_sound.play()
                            pygame.quit()
                            sys.exit()
                        if pause_button.checkForInput(mouse_pos):
                            click_sound.play()
                            paused = False  # Reanudar el juego

                pygame.display.update()
                pygame.time.Clock().tick(FPS)
        

        else:
            # Si el juego no está pausado, ejecutar la lógica del nivel
            pause_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/pausaa.png"), pos=(920, 50), text_input="", font=get_font(30), base_color="White", hovering_color="Green")
            level_game.run()  # Llama al método run del nivel

            # Verifica si el jugador ha muerto y activa "game over"
            if level_game.game_over_condition():
                game_over = True  # Activa el estado de "game over"
                continue
            if level_game.win_condition():  # Esta es la nueva función que debes definir en tu clase Level
                win_game = True 

            
            # Mostrar el botón de pausa
            pause_button.update(SCREEN)

            pygame.display.update()
            pygame.time.Clock().tick(FPS)


def start_level2(level):

    level_game = Level2()
    global idioma,game_over
    paused = False  # Variable que controla el estado de pausa

    if not pygame.mixer.music.get_busy():  # Si no hay música sonando
        pygame.mixer.music.load("assets/music/Pista1_Menu1.mp3")  # Música de fondo
        pygame.mixer.music.play(-1, 0.0)


    mouse_pos = pygame.mouse.get_pos()
    pause_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/pausaa.png"), pos=(920, 50), text_input="", font=get_font(30), base_color="White", hovering_color="Green")  # Botón de pausa
    home_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/HOME.png"), pos=(280, 370), text_input="", font=get_font(50), base_color="White", hovering_color="Green") 
    salir_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/salirr.png"), pos=(650, 370), text_input="", font=get_font(50), base_color="White", hovering_color="Green")  

    while True:
        if game_over:
            pygame.mixer.music.stop()
            # Reproducir la música de "game over"
            pygame.mixer.music.load("assets/music/game-over-classic-206486.mp3")  # Música de Game Over
            pygame.mixer.music.play(0, 0.0)  # Reproducir una vez (0 indica no loop)
            # Llamar a la función de "game over" para mostrar la pantalla de Game Over
            result = gameover()
            if result == "restart":
                game_over = False
                start_level2(level)  # Reinicia el nivel actual
                return  # Salir del bucle actual
            elif result == "exit":
                pygame.quit()
                sys.exit()  # Salir del juego

        pygame.display.set_caption(f"Forest Keepers - Nivel {level}")

        if not pygame.mixer.music.get_busy():  # Si no hay música sonando
            pygame.mixer.music.load("assets/music/Pista1_Menu1.mp3")  # Música de fondo
            pygame.mixer.music.play(-1, 0.0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused  # Alterna el estado de pausa

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if pause_button.checkForInput(mouse_pos):
                    click_sound.play()
                    paused = not paused 

        # Si el juego está pausado
        if paused:
            if idioma == "spanish":
                SCREEN.blit(pygame.image.load("assets/botones/BotonesFinales/Pausa.png"), (0, 0))
            else:
                SCREEN.blit(pygame.image.load("assets/botones/BotonesFinales/Paused.png"), (0, 0))

            # Botones de pausa, salir y volver al inicio
            pause_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/RESUME.png"), pos=(470, 370), text_input="", font=get_font(30), base_color="White", hovering_color="Green")
            pause_button.update(SCREEN)
            home_button.update(SCREEN)
            salir_button.update(SCREEN)

            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if home_button.checkForInput(mouse_pos):
                            click_sound.play()
                            main_menu()
                        if salir_button.checkForInput(mouse_pos):
                            click_sound.play()
                            pygame.quit()
                            sys.exit()
                        if pause_button.checkForInput(mouse_pos):
                            click_sound.play()
                            paused = False  # Reanudar el juego

                pygame.display.update()
                pygame.time.Clock().tick(FPS)

        else:
            # Si el juego no está pausado, ejecutar la lógica del nivel
            pause_button = Button(image=pygame.image.load("assets/botones/BotonesFinales/pausaa.png"), pos=(920, 50), text_input="", font=get_font(30), base_color="White", hovering_color="Green")
            level_game.run()  # Llama al método run del nivel

            # Verifica si el jugador ha muerto y activa "game over"
            if level_game.game_over_condition():
                game_over = True  # Activa el estado de "game over"
                continue

            
            # Mostrar el botón de pausa
            pause_button.update(SCREEN)

            pygame.display.update()
            pygame.time.Clock().tick(FPS)


def start_level3(level):
    while True:
        SCREEN.fill("black")
        pygame.display.set_caption(f"Forest Keepers - Nivel {level}")
        level_game = Level()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        level_game.toggle_menu()

            SCREEN.fill("black")
            level_game.run()
            pygame.display.update()
            pygame.time.Clock().tick(FPS)



# Iniciar el menú principal
main_menu()
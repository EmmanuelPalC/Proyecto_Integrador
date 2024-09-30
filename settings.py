WIDTH = 960
HEIGTH = 600
FPS = 60
TILESIZE = 64

#ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'assets/menu/font/joystix.ttf'
UI_FONT_SIZE = 18

#general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

#ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'yellow'
UI_BORDER_COLOR_ACTIVE = 'gold'

#menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

#weapon
weapon_data ={
    'hammer':{'cooldown':50, 'damage':15,'graphic':'assets\player\hammer.png'}
}

monster_data ={
    'bob':{'health':100,'damage':20,'attack_type':'slash','speed':5,'resistance':3,'attack_radius':60,'notice_radius':150}
}
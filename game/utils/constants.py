import pygame
import os

pygame.init()
pygame.font.init()

# Global Constants
TITLE = "Spaceship Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
SPACESHIP_MOV = 10
CONVEYOR_MOV = 7

## IMG_DIR es el camino a encontrar los "archivos" de imagenes
# sonido, etc

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants

# pygame.image.load --> carga la imagen en memoria y la guardamos en la variable ....por ejemplo ICON
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
BACKGROUND = pygame.image.load(os.path.join(IMG_DIR, 'Other/background.jpg'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
ENEMY_BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))

CONVEYOR = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/ships.png"))

HEARTS = pygame.image.load(os.path.join(IMG_DIR, 'Other', "hearts.png"))
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other', "heart.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'
FONT = pygame.font.Font(FONT_STYLE, 12)
COUTER_FONT = pygame.font.Font(FONT_STYLE, 8)

FONT_PATH = os.path.join(IMG_DIR, 'Other', 'Pixeltype.ttf')
FONT_2 = pygame.font.Font(FONT_PATH, 50)
FONT_3 = pygame.font.Font(FONT_PATH, 94)

BACKGROUND_MUSIC = os.path.join(IMG_DIR, 'Other', 'background.ogg')
SHOOT = os.path.join(IMG_DIR, 'Other', 'laser5.ogg')
ROUND_1_PATH = os.path.join(IMG_DIR, 'Other', 'round_1.mp3')

import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

RESET = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))

STAR = pygame.image.load(os.path.join(IMG_DIR, 'Other/Star.png'))

START = pygame.image.load(os.path.join(IMG_DIR, 'Other/Start.png'))

ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

BGSTART = pygame.image.load(os.path.join(IMG_DIR, 'Other/StartFond.jpg'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

BURST = pygame.image.load(os.path.join(IMG_DIR, 'Other/Boom.png'))

PLUS = pygame.image.load(os.path.join(IMG_DIR, 'Other/PlusAShip.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/HeartBad.png'))

VOLUMEN_DOWN = pygame.image.load(os.path.join(IMG_DIR, 'Sounds/volume_down.png'))
VOLUMEN_UP = pygame.image.load(os.path.join(IMG_DIR, 'Sounds/volume_up.png'))
VOLUMEN_MUTE = pygame.image.load(os.path.join(IMG_DIR, 'Sounds/volume_muted.png'))
VOLUMEN_MAX = pygame.image.load(os.path.join(IMG_DIR, 'Sounds/volume_max.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
BURST_TYPE = 'Burst'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

pygame.init()
pygame.mixer.init()
LASER_SOUND = pygame.mixer.Sound('Sounds/Bullet.wav')
BURST_SOUND = pygame.mixer.Sound('Sounds/Burst.wav')
BURST_ENEMY_SOUND = pygame.mixer.Sound('Sounds/BurstEnemy.wav')
MUSIC_BG = pygame.mixer.Sound('Sounds/MusicFond.mp3')
POWER_SOUND = pygame.mixer.Sound('Sounds/PowerUp.wav')
START_SOUND = pygame.mixer.Sound('Sounds/Start.wav')

FONT_STYLE = 'freesansbold.ttf'

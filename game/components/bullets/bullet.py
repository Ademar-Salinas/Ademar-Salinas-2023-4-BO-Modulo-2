import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY ,SCREEN_HEIGHT
class Bullet(Sprite):
    BULLET_SIZE = pygame.transform.scale(BULLET,(10, 20))
    BULLET_ENEMY_SIZE = pygame.transform.scale(BULLET_ENEMY,(9, 32))
    BULLET = {'player': BULLET_SIZE, 'enemy': BULLET_ENEMY_SIZE}
    SPEED = 15
    def __init__(self, spaceship):
        self.image = self.BULLET[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type
        
    def update(self,bullets):
        if self.owner == 'enemy':
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)
        if self.owner == 'player':
            self.rect.y -= self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)
    
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
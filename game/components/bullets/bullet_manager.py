import pygame

from game.components.enemies.enemy import Enemy

class BulletManager:
    ENEMY = Enemy()

    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner =='enemy':
                self.enemy_bullets.remove(bullet)
                game.death_count += 1
                game.playing = False
        for bullet in self.bullets:
            bullet.update(self.bullets)
            if bullet.rect.colliderect(self.ENEMY.rect) and bullet.owner =='player':
                bullet.owner =='player'
                game.update_score()
                self.bullets.remove(bullet)
        
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len (self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        if bullet.owner == 'player':
            self.bullets.append(bullet)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
            
import random
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy = Enemy
        
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)


    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 2:
            enemy = Enemy()
            self.enemies.append(enemy)
            type_enemy = random.randint(0,1)
            if type_enemy == 0:           
                self.enemy.NUMBER_ENEMY = 0
            elif type_enemy == 1:
                self.enemy.NUMBER_ENEMY = 1

    def reset(self):
        self.enemies = []
            

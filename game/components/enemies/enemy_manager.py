from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy = Enemy
    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 2:
            enemy = Enemy()
            self.enemies.append(enemy)
            if len(self.enemies) == 0:
                self.enemy.n_enemy = 0
            elif len(self.enemies) == 1:
                self.enemy.n_enemy = 1
    
            
            

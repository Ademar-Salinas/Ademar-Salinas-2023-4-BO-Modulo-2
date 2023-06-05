import pygame

from game.components.powerups.power_up import PowerUp
from game.utils.constants import BURST, BURST_TYPE

class Burst(PowerUp):
    def __init__(self):
        Burst = pygame.transform.scale(BURST, (80, 80))
        super().__init__(Burst, BURST_TYPE)
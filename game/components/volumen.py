import pygame

from game.utils.constants import MUSIC_BG, VOLUMEN_DOWN, VOLUMEN_MAX, VOLUMEN_MUTE, VOLUMEN_UP

class Volumen:
    def __init__(self):
        pygame.mixer.music.load('Sounds/MusicFond.mp3')
        pygame.mixer.music.play(-1)

    def update(self, user_input):
        #Baja volumen
        if user_input[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
            self.volumen_down(0)
        elif user_input[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
            self.volumen_muted(2)

        #Sube volumen
        if user_input[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
            self.volumen_up(1)
        elif user_input [pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
            self.volumen_max(3)

        #Desactivar sonido
        elif user_input[pygame.K_m]:
            self.volumen_muted(2)

        #Reactivar sonido
        elif user_input[pygame.K_COMMA]:
            self.volumen_max(3)

    def volumen_down(self, vol):
        self.vol = vol
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
    
    def volumen_up(self, vol):
        self.vol = vol
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)

    def volumen_muted(self, vol):
        self.vol = vol
        pygame.mixer.music.set_volume(0.0)
    
    def volumen_max(self, vol):
        self.vol = vol
        pygame.mixer.music.set_volume(1.0)
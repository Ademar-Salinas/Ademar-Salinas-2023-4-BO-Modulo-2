import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH, BGSTART, START_SOUND
  
class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH //2

    def __init__(self, screen):
        image = pygame.transform.scale(BGSTART, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(image, (0, 0))
        self.font = pygame.font.Font(FONT_STYLE,30)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen, message, x = HALF_SCREEN_WIDTH, y = HALF_SCREEN_HEIGHT, color = (255, 255, 255)):
        self.message = message
        self.color_text = color
        self.text = self.font.render(message, True, color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)
        screen.blit(self.text, self.text_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                pygame.mixer.Sound.play(START_SOUND)
                game.run()

    def reset_screen_color(self, screen):
        image = pygame.transform.scale(BGSTART, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(image, (0, 0))

    def update_message(self, message_score, message_death, message_best_score, screen):
        self.text1 = self.font.render(message_score, True, self.color_text)
        self.text1_rect = self.text1.get_rect()
        self.text1_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 40)
        screen.blit(self.text1, self.text1_rect)
        self.text2 = self.font.render(message_death, True, self.color_text)
        self.text2_rect = self.text2.get_rect()
        self.text2_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 120)
        screen.blit(self.text2, self.text2_rect)
        self.text3 = self.font.render(message_best_score, True, self.color_text)
        self.text3_rect = self.text3.get_rect()
        self.text3_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 80)
        screen.blit(self.text3, self.text3_rect)

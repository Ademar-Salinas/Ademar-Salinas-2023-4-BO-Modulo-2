import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH
  
class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH //2
    def __init__(self, message,message_score,message_death, message_best_score, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE,30)
        self.text = self.font.render(message, True,(0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH,self.HALF_SCREEN_HEIGHT)
        self.text1 = self.font.render(message_score, True, (0, 0, 0))
        self.text1_rect = self.text1.get_rect()
        self.text1_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 40)
        self.text2 = self.font.render(message_death, True, (0, 0, 0))
        self.text2_rect = self.text2.get_rect()
        self.text2_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 120)
        self.text3 = self.font.render(message_best_score, True, (0, 0, 0))
        self.text3_rect = self.text3.get_rect()
        self.text3_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 80)


    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text1, self.text1_rect)
        screen.blit(self.text2, self.text2_rect)
        screen.blit(self.text3, self.text3_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen):
        screen.fill((255,255,255))

    def update_message(self, message,message_score, message_death, message_best_score):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        self.text1 = self.font.render(message_score, True, (0, 0, 0))
        self.text1_rect = self.text1.get_rect()
        self.text1_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 40)
        self.text2 = self.font.render(message_death, True, (0, 0, 0))
        self.text2_rect = self.text2.get_rect()
        self.text2_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 120)
        self.text3 = self.font.render(message_best_score, True, (0, 0, 0))
        self.text3_rect = self.text3.get_rect()
        self.text3_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 80)


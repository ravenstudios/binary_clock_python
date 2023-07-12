import pygame
from constants import *

class Button_12_hour():
    def __init__(self, on_click=None):
        self.rect = None
        self.on_click = on_click
        self.clicked = False
        self.button_state = False
        self.font = pygame.font.Font("freesansbold.ttf", 32)

    def update(self):
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if not self.clicked:
                    self.clicked = True
                    self.button_state = not self.button_state
        if not pygame.mouse.get_pressed(num_buttons=3)[0]:
            self.clicked = False


    def draw(self, surface):



        if self.button_state:
            text = self.font.render("24 Hour Mode" , True , WHITE)
        else:
            text = self.font.render("12 Hour Mode" , True , WHITE)
        self.rect = text.get_rect()

        self.rect.center = (GAME_WIDTH // 2, GAME_HEIGHT - self.rect.bottom )
        pygame.draw.rect(surface, RED, self.rect)
        surface.blit(text, self.rect)

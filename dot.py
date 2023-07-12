from constants import *
import pygame

class Dot():
    def __init__(self, x, y, number=0):
        self.x = x
        self.y = y
        self.radius = 32
        self.is_on = False
        self.on_color = RED
        self.off_color = BLACK
        self.color = self.off_color
        self.number = number


    def update(self):
        self.color = self.on_color if self.is_on else self.off_color


    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        self.draw_numbers(surface)


    def turn_on(self):
        self.is_on = True


    def turn_off(self):
        self.is_on = False


    def draw_numbers(self, surface):
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render(str(self.number), True, WHITE, BLACK)
        textrect = text.get_rect()
        textrect.center = (self.x, self.y)
        surface.blit(text, textrect)

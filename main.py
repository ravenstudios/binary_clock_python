from constants import *
import binary_clock
import pygame
import button_12_hour

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()


binary_clock = binary_clock.Clock()
button_12_hour = button_12_hour.Button_12_hour()

is_24_mode = True

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((255, 255, 255))#background
    binary_clock.draw(surface)
    button_12_hour.draw(surface)
    pygame.display.flip()



def update():
    is_24_mode = True if button_12_hour.button_state == False else False
    binary_clock.update(is_24_mode)
    button_12_hour.update()





if __name__ == "__main__":
    main()

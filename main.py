from constants import *
import binary_clock
import pygame



clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()


binary_clock = binary_clock.Clock()
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
    pygame.display.flip()



def update():
    binary_clock.update()


if __name__ == "__main__":
    main()

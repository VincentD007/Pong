import pygame
import random

HEIGHT = 1000
WIDTH = 1600


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))



def main():
    player1_score = 0
    player2_score = 0

    play_game = True
    while play_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False




        SCREEN.fill((0, 0, 0))
        pygame.display.update()
    pygame.quit()



if __name__ == "__main__":
    main()

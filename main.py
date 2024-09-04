import pygame
import random
from pong_functions import *
HEIGHT = 800
WIDTH = 1200
clock = pygame.time.Clock()


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))



def main():
    ball_x, ball_y = 0, 200
    ball_velocity = 10
    player1_score = 0
    player2_score = 0
    walls = {
        "left_goal": pygame.rect.Rect(0, 0, 10, HEIGHT),
        "right_goal": pygame.rect.Rect(1190, 0, 10, HEIGHT),
        "top_boarder": pygame.rect.Rect(0, 0, WIDTH, 10),
        "bottom_boarder": pygame.rect.Rect(0, HEIGHT-10, WIDTH, 10)
        }

    ball_x, ball_y = 0, 200
    play_game = True

    while play_game:
        clock.tick(60)
        ball = pygame.rect.Rect(ball_x, ball_y, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
        SCREEN.fill((0, 0, 0))    

        pygame.draw.rect(SCREEN, (255, 255, 255), ball)
        ball_x += 10
        draw_boarders(SCREEN, walls)

        pygame.display.update()
    pygame.quit()



if __name__ == "__main__":
    main()

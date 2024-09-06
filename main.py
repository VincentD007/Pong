import pygame
from pong_functions import *

pygame.init()
HEIGHT = 800
WIDTH = 1200
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))



def main():
    ball = Ball()
    left_paddle = pygame.rect.Rect(100, 325, 20, 150)
    right_paddle = pygame.rect.Rect(1075, 325, 20, 150)
    left_player_score = 0
    right_player_score = 0
    play_game = True
    walls = {
        "left_goal": pygame.rect.Rect(0, 0, 10, HEIGHT),
        "right_goal": pygame.rect.Rect(1190, 0, 10, HEIGHT),
        "top_boarder": pygame.rect.Rect(0, 0, WIDTH, 10),
        "bottom_boarder": pygame.rect.Rect(0, HEIGHT-10, WIDTH, 10)
        }

    while play_game:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
        SCREEN.fill((0, 0, 0))

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_DOWN]:
            if right_paddle.y + 10 < 650:
                right_paddle.y += 10
        if keys_pressed[pygame.K_UP]:
            if right_paddle.y - 10 > 0:
                right_paddle.y -= 10
        if keys_pressed[pygame.K_LCTRL]:
            if left_paddle.y + 10 < 650:
                left_paddle.y += 10
        if keys_pressed[pygame.K_LSHIFT]:
            if left_paddle.y - 10 > 0:
                left_paddle.y -= 10
        pygame.draw.rect(SCREEN, (255, 255, 255), left_paddle)
        pygame.draw.rect(SCREEN, (255, 255, 255), right_paddle)
        ball.move()
        handle_collisions(ball, walls, left_paddle, right_paddle)
        if left_scored(walls, ball):
            left_player_score += 1
            ball.reset()
        elif right_scored(walls, ball):
            right_player_score += 1
            ball.reset()
        ball.draw(SCREEN)
        print(left_player_score)
        draw_boarders(SCREEN, walls)

        pygame.display.update()
    pygame.quit()



if __name__ == "__main__":
    main()

import pygame
import random
import math

pygame.init()


def draw_boarders(Screen, Walls):
    for wall in Walls:
        pygame.draw.rect(Screen, (255, 255, 255), Walls[wall])
    mid_spacing = 25
    for _ in range(16):
        pygame.draw.rect(Screen, (255, 255, 255), pygame.rect.Rect((Screen.get_width()/2) - 7, mid_spacing, 14, 50))
        mid_spacing += 100

# Handles all ball collisions with the exception of goals
def handle_collisions(ball, walls, left_paddle, right_paddle):
    def check_first_collision(ball_object):
        if not ball.first_hit:
            ball_object.velocity += 5
            ball_object.first_hit = True
    # Checks for ball collision with top boarder; Also checks if the ball is colliding with both the top boarder and a paddle at the same time
    if pygame.Rect.colliderect(ball.rect, walls["top_boarder"]):
        if pygame.Rect.colliderect(ball.rect, left_paddle) or pygame.Rect.colliderect(ball.rect, right_paddle):
            ball.direction += math.pi
            return
        else:
            ball.direction *= -1
    # Checks for ball collision with bottom boarder; Also checks if the ball is colliding with both the bottom boarder and a paddle at the same time
    elif pygame.Rect.colliderect(ball.rect, walls["bottom_boarder"]):
        if pygame.Rect.colliderect(ball.rect, left_paddle) or pygame.Rect.colliderect(ball.rect, right_paddle):
            ball.direction += math.pi
            return
        else:
            ball.direction *= -1

    mid_ball = ball.rect.y + 10
    # Update ball angle based on left paddle collision
    if pygame.Rect.colliderect(ball.rect, left_paddle):
        mid_paddle = left_paddle.y + 70
        # Checks if ball collision is on upper half of Left Paddle
        if mid_ball <= mid_paddle - 10:
            if mid_ball >= mid_paddle - 20 :
                ball.direction = math.pi/12
            elif mid_ball >= mid_paddle - 30:
                ball.direction = math.pi/6
            elif ball.rect.x + 10 < left_paddle.x + 15:
                ball.direction = 2 * math.pi/3
            else:
                ball.direction = math.pi/4
        # Checks if ball collision is on lower half of Left Paddle
        elif mid_ball >= mid_paddle + 10:
            if mid_ball <= mid_paddle + 20:
                ball.direction = -math.pi/12
            elif mid_ball <= mid_paddle + 40:
                ball.direction = -math.pi/6
            elif ball.rect.x + 10 < left_paddle.x + 15:
                ball.direction = -2 * math.pi/3
            else:
                ball.direction = -math.pi/4
        else:
            ball.direction = 0
        check_first_collision(ball)

    # Update ball angle based on right paddle collision
    elif pygame.Rect.colliderect(ball.rect, right_paddle):
        mid_paddle = right_paddle.y + 70
        # Checks if ball collision is on upper half of Right Paddle
        if mid_ball <= mid_paddle - 10:
            if mid_ball >= mid_paddle - 20 :
                ball.direction = 11 * math.pi/12
            elif mid_ball >= mid_paddle - 30:
                ball.direction = 5 * math.pi/6
            elif ball.rect.x + 10 > right_paddle.x + 5:
                ball.direction = math.pi/3
            else:
                ball.direction = 3 * math.pi/4
        # Checks if ball collision is on lower half of Right Paddle
        elif mid_ball >= mid_paddle + 10:
            if mid_ball <= mid_paddle + 20:
                ball.direction = -11 * math.pi/12
            elif mid_ball <= mid_paddle + 40:
                ball.direction = -5 * math.pi/6
            elif ball.rect.x + 10 > right_paddle.x + 5:
                ball.direction = -math.pi/3
            else:
                ball.direction = -3 * math.pi/4
        else:
            ball.direction = math.pi
        check_first_collision(ball)


class Ball:
    def __init__(self) -> None:
        self.first_hit = False
        self.direction = random.choice([0, math.pi])
        self.velocity = 3
        self.rect = pygame.rect.Rect(590, 390, 20, 20)
        self.color = (255, 255, 255)


    def move(self):
        distance_x = (math.cos(self.direction) * self.velocity)
        self.rect.x += distance_x
        distance_y = (math.sin(self.direction) * self.velocity)
        self.rect.y -= distance_y


    def draw(self, Screen):
        pygame.draw.rect(Screen, self.color, self.rect)

    # Resets the balls position back to the center
    # Only called when a player scores
    def reset(self):
        self.first_hit = False
        self.direction = random.choice([0, math.pi])
        self.velocity = 3
        self.rect = pygame.rect.Rect(590, 390, 20, 20)

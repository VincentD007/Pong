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


def left_scored(walls, ball):
    return pygame.Rect.colliderect(ball.rect, walls["right_goal"])


def right_scored(walls, ball):
    return pygame.Rect.colliderect(ball.rect, walls["left_goal"])


def handle_collisions(ball, walls, left_paddle, right_paddle):
    def check_first_collision(ball_object):
        if not ball.firsthit:
            ball_object.velocity += 6
            ball_object.firsthit = True

    if pygame.Rect.colliderect(ball.rect, walls["top_boarder"]):
        angle = ball.direction % math.pi
        if angle < math.pi/2:
            ball.direction -= ball.direction*2
        elif angle > math.pi/2:
            ball.direction += (math.pi - ball.direction) * 2
    elif pygame.Rect.colliderect(ball.rect, walls["bottom_boarder"]):
        angle = ball.direction % (2 * math.pi)
        if angle < 3 * math.pi/2:
            ball.direction -= (math.pi/2 - ((3 * math.pi/2) - angle)) * 2
        elif angle > 3 * math.pi/2:
            ball.direction += (2 * math.pi - angle) * 2
    if pygame.Rect.colliderect(ball.rect, left_paddle):
        ball.direction -= math.pi
        check_first_collision(ball)

    elif pygame.Rect.colliderect(ball.rect, right_paddle):
        ball.direction += math.pi
        check_first_collision(ball)


class Ball:
    def __init__(self) -> None:
        self.firsthit = False
        self.direction = random.choice([0, math.pi])
        self.velocity = 4
        self.rect = pygame.rect.Rect(590, 390, 20, 20)
        self.color = (255, 255, 255)


    def move(self):
        distance_x = (math.cos(self.direction) * self.velocity)
        self.rect.x += distance_x
        distance_y = (math.sin(self.direction) * self.velocity)
        self.rect.y -= distance_y


    def draw(self, Screen):
        pygame.draw.rect(Screen, self.color, self.rect)


    def reset(self):
        self.firsthit = False
        self.direction = random.choice([0, math.pi])
        self.velocity = 5
        self.rect = pygame.rect.Rect(590, 390, 20, 20)

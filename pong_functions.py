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
        if not ball.first_hit:
            ball_object.velocity += 8
            ball_object.first_hit = True

    if pygame.Rect.colliderect(ball.rect, walls["top_boarder"]):
        reference_angle = ball.direction % math.pi
        if reference_angle < math.pi/2:
            ball.direction -= reference_angle * 2
        elif reference_angle > math.pi/2:
            ball.direction += (math.pi - reference_angle) * 2
    elif pygame.Rect.colliderect(ball.rect, walls["bottom_boarder"]):
        reference_angle = ball.direction % (2 * math.pi)
        if reference_angle < 3 * math.pi/2:
            ball.direction -= (math.pi/2 - ((3 * math.pi/2) - reference_angle)) * 2
        elif reference_angle > 3 * math.pi/2:
            ball.direction += ((2 * math.pi) - reference_angle) * 2

    if pygame.Rect.colliderect(ball.rect, left_paddle):
        mid_paddle = left_paddle.y + 70
        mid_ball = ball.rect.y + 10
        if mid_ball <= mid_paddle - 10:
            if mid_ball >= mid_paddle - 20 :
                ball.direction = math.pi/12
            elif mid_ball >= mid_paddle - 30:
                ball.direction = math.pi/6
            else:
                ball.direction = math.pi/4
        elif mid_ball >= mid_paddle + 10:
            if mid_ball <= mid_paddle + 20:
                ball.direction = -math.pi/12
            elif mid_ball <= mid_paddle + 40:
                ball.direction = -math.pi/6
            else:
                if ball.rect.x < left_paddle.x + 10:
                    ball.direction = -3 * math.pi/4
                else:
                    ball.direction = -math.pi/4
        else:
            ball.direction = 0
        check_first_collision(ball)

    elif pygame.Rect.colliderect(ball.rect, right_paddle):
        mid_paddle = right_paddle.y + 70
        mid_ball = ball.rect.y + 10
        if mid_ball <= mid_paddle - 10:
            if mid_ball >= mid_paddle - 20 :
                ball.direction = 11 * math.pi/12
            elif mid_ball >= mid_paddle - 30:
                ball.direction = 5 * math.pi/6
            else:
                ball.direction = 3 * math.pi/4
        elif mid_ball >= mid_paddle + 10:
            if mid_ball <= mid_paddle + 20:
                ball.direction = -11 * math.pi/12
            elif mid_ball <= mid_paddle + 40:
                ball.direction = -5 * math.pi/6
            else:
                ball.direction = -3 * math.pi/4
        else:
            ball.direction = math.pi
        check_first_collision(ball)


class Ball:
    def __init__(self) -> None:
        self.first_hit = False
        self.direction = random.choice([0, math.pi])
        self.velocity = 5
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
        self.first_hit = False
        self.direction = math.pi
        self.velocity = 5
        self.rect = pygame.rect.Rect(590, 390, 20, 20)

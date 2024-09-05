import pygame

def draw_boarders(Screen, Walls):
    for wall in Walls:
        pygame.draw.rect(Screen, (255, 0, 0), Walls[wall])
    mid_spacing = 25
    for _ in range(16):
        pygame.draw.rect(Screen, (255, 255, 255), pygame.rect.Rect((Screen.get_width()/2) - 7, mid_spacing, 14, 50))
        mid_spacing += 100


def check_collision(ball, walls):
    for wall in walls:
        if pygame.Rect.colliderect(ball, wall):
            if walls[wall] == "left_goal":
                pass
            elif walls[wall] == "right_goal":
                pass
            elif walls[wall] == "top_boarder":
                pass  
            elif walls[wall] == "bottom_boarder":
                pass



class Ball:
    def __init__(self, spawn_direction) -> None:
        self.direction = spawn_direction
        self.spawn_velocity = 5
        self.x, self.y = 590, 390
        self.rise, self.run = 10, 10
        self.object = pygame.rect.Rect(self.x, self.y, 20, 20)
        self.color = (255, 255, 255)

    def move(self):
        self.y += self.rise
        self.x += self.run
        self.object = pygame.rect.Rect(self.x, self.y, 20, 20)


    def draw(self, Screen):
        pygame.draw.rect(Screen, self.color, self.object)



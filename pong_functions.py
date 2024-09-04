import pygame

def draw_boarders(Screen, Walls):
    for wall in Walls:
        pygame.draw.rect(Screen, (255, 0, 0), Walls[wall])
    mid_spacing = 25
    for _ in range(16):
        pygame.draw.rect(Screen, (255, 255, 255), pygame.rect.Rect((Screen.get_width()/2) - 12, mid_spacing, 20, 50))
        mid_spacing += 100

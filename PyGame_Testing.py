# ----------Скелет для PyGame-------------
import pygame
import random

WIDTH = 360
HEIGHT = 180
FPS = 30
# -----------------------
# ----------Создание окна-------------
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing Window for PyGame")
clock = pygame.time.Clock()
# -----------------------
# -----------------------
running = True
while running:
    clock.tick(FPS)

# -----------------------

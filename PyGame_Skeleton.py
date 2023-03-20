# --------||--Скелет для PyGame--||-----------
import pygame  # Предварительно установить: pip install pygame
import random

WIDTH = 360  # Ширина окна
HEIGHT = 180  # Высота окна
FPS = 30  # Частота обновления кадров

# Цвета для использования в программе (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

# -------1--Создание окна--1----------
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing Window for PyGame")
clock = pygame.time.Clock()
# -------1----------1------

# ---------2--Цикл игры--2----------
running = True
while running:
    # ---------Обновление---------
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():  # проверка закрытия окна
        if event.type == pygame.QUIT:
            running = False
    # -----------------------

    # Визуализация (сборка)

    # -------Рендеринг-------
    screen.fill(LIGHT_BLUE)
    pygame.display.flip()  # после отрисовки всего, переворачиваем экран
    # ---------------------

# -------2----------2------
pygame.quit()  # Закрытие окна
# -----||----Конец скелета----||-------

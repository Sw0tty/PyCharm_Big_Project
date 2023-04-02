# --------||--Скелет для PyGame--||-----------
# Скелет содержит в себе базовый набор для запуска окна и его редактирования
# Также имеет готовый 1 спрайт, который отрисовывается по центру окна

import pygame  # Предварительно установить: pip install pygame
import random
import os  # Для взаимодействия с системными файлами
import ctypes

# ----------Настройка папки ассетов-----------
project_folder = os.path.dirname(__file__)  # Сокращенная запись для указания папки с проектом
images_folder = os.path.join(project_folder, 'img')  # Соединение пути и папки в проекте
# ----------------------------

FULL_WIDTH = ctypes.windll.user32.GetSystemMetrics(0)  # Полная ширина экрана пользователя
FULL_HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)  # Полная высота экрана пользователя
WIDTH = FULL_WIDTH / 2  # Ширина окна по умолчанию
HEIGHT = FULL_HEIGHT / 2  # Высота окна по умолчанию
FPS = 30  # Частота обновления кадров

# -----Библиотека цветов----- (R, G, B)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
LIGHT_GREY = (211, 211, 211)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
# --------------------------------------

# --------Глобальные перменные--------
# ------------------------------------

# -------1--Создание окна--1----------
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# ---Инициализация изображений---
icon_img = pygame.image.load(os.path.join(images_folder, 'test_img.png')).convert()  # Загрузки фото из папки
# -------------------------------

pygame.display.set_caption("Testing Window for PyGame")  # Надпись
pygame.display.set_icon(icon_img)  # Иконка
clock = pygame.time.Clock()
# -------1----------1------


# ----------Классы для спрайтов------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Строка для запуска инициализатора встроенных классов Sprite
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def player_update(self):
        pass

# -----------------------------------------


# -------Добавление спрайтов----------
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# ------------------------


# ---------2--Цикл игры--2----------
running = True
while running:
    # ---------Задание скорости FPS---------
    clock.tick(FPS)
    # --------------------------------------

    # ---------Обработчик событий-----------
    for game_event in pygame.event.get():  # Цикл всех событий
        if game_event.type == pygame.QUIT:  # Проверка закрытия окна
            running = False
    # --------------------------------------

    # ---------Обновление---------
    player.player_update()  # Функция заглушка для отображения. Эквивалент update()
    # ----------------------------

    # -------Отрисовка-------
    screen.fill(LIGHT_GREY)  # Заливка фона
    all_sprites.draw(screen)  # Отрисвока спрайтов
    pygame.display.flip()  # После отрисовки всего, переворачиваем экран
    # ---------------------

# -------2----------2------
pygame.quit()  # Закрытие окна
# -----||----Конец скелета----||-------

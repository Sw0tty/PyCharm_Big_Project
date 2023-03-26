# --------||--Скелет для PyGame--||-----------
import pygame  # Предварительно установить: pip install pygame
import random
import os

# ----------Настройка папки ассетов-----------
game_folder = os.path.dirname(__file__)  # Сокращенная запись для указания папки с проектом
img_folder = os.path.join(game_folder, 'img')  # Соединение пути и папки в проекте
# ----------------------------

WIDTH = 760  # Ширина окна
HEIGHT = 380  # Высота окна
FPS = 60  # Частота обновления кадров

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
player_rect_reaction = 3
player2_rect_reaction = random.randint(1, 4)
# ------------------------------------

# -------1--Создание окна--1----------
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# ---Инициализация изображений---
player_img = pygame.image.load(os.path.join(img_folder, 'test_img.png')).convert()
# -------------------------------

pygame.display.set_caption("Testing Window for PyGame")
pygame.display.set_icon(player_img)
clock = pygame.time.Clock()
# -------1----------1------


# ----------Классы для спрайтов------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Строка для запуска инициализатора встроенных классов Sprite
        self.image = pygame.Surface((50, 50))  # Опредление поверхности image и ее размеров
        self.image.fill(LIGHT_BLUE)  # Закрашивание определенной поверхности image
        self.rect = self.image.get_rect()  # rect - сокращение от слова rectangle - прямоугольник
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # Задание атрибута center для расположения rect

    def update(self):  # Метод обновления спрайта
        self.rect.x += 5  # Задание спрайту каждый FPS передвинуться на 5 пикселей по X
        if self.rect.left == WIDTH:
            self.rect.right = 0

    def update_1(self):
        self.rect.x += 5
        if self.rect.right >= WIDTH:
            global player_rect_reaction
            player_rect_reaction = 1

    def update_2(self):
        self.rect.x -= 5
        if self.rect.left <= 0:
            global player_rect_reaction
            player_rect_reaction = 0


class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Строка для запуска инициализатора встроенных классов Sprite
        self.image = player_img
        self.image = pygame.transform.scale(player_img, (80, 80))
        # self.image.set_colorkey(WHITE)  # Исключение по цвету
        self.rect = self.image.get_rect()  # rect - сокращение от слова rectangle - прямоугольник
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # Задание атрибута center для расположения rect

    def update_1(self):
        self.rect.x += 2
        self.rect.y -= 2
        if self.rect.top <= 0:
            global player2_rect_reaction
            player2_rect_reaction = 2

    def update_2(self):
        self.rect.x += 2
        self.rect.y += 2
        if self.rect.right >= WIDTH:
            global player2_rect_reaction
            player2_rect_reaction = 3

    def update_3(self):
        self.rect.x -= 2
        self.rect.y += 2
        if self.rect.bottom >= HEIGHT:
            global player2_rect_reaction
            player2_rect_reaction = 4

    def update_4(self):
        self.rect.x -= 2
        self.rect.y -= 2
        if self.rect.top <= 0:
            global player2_rect_reaction
            player2_rect_reaction = 5

    def update_5(self):
        self.rect.x -= 2
        self.rect.y += 2
        if self.rect.left <= 0:
            global player2_rect_reaction
            player2_rect_reaction = 6

    def update_6(self):
        self.rect.x += 2
        self.rect.y += 2
        if self.rect.bottom >= HEIGHT:
            global player2_rect_reaction
            player2_rect_reaction = 1
# -----------------------------------------


# -------Отрисовка спрайтов-------
all_sprites = pygame.sprite.Group()
player = Player()
player2 = Player2()
all_sprites.add(player)  # Отображение спрайта player
all_sprites.add(player2)  # Отображение спрайта player2
# --------------------------------

# ---------2--Цикл игры--2----------
running = True
while running:
    # ---------Задание скорости FPS---------
    clock.tick(FPS)
    # ------------------

    # ---------Ввод процесса (события)-----------
    for event in pygame.event.get():  # Цикл всех событий
        if event.type == pygame.QUIT:  # Проверка закрытия окна
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Проверка нажатия кнопки мыши
            x, y = event.pos  # Передача переменным (x, y) координат с позиции нажатия мыши
            if player.rect.collidepoint(x, y):  # Проверка вхождения x, y в спрайт
                player_rect_reaction = 0
    # -----------------------

    # ---Обновление---
    if player_rect_reaction == 0:
        player.update_1()  # Применение спрайту функции
    if player_rect_reaction == 1:
        player.update_2()

    if player2_rect_reaction == 1:
        player2.update_1()
    elif player2_rect_reaction == 2:
        player2.update_2()
    elif player2_rect_reaction == 3:
        player2.update_3()
    elif player2_rect_reaction == 4:
        player2.update_4()
    elif player2_rect_reaction == 5:
        player2.update_5()
    elif player2_rect_reaction == 6:
        player2.update_6()

    # Визуализация (сборка)

    # -------Отрисовка-------
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()  # после отрисовки всего, переворачиваем экран
    # ---------------------

# -------2----------2------
pygame.quit()  # Закрытие окна
# -----||----Конец скелета----||-------

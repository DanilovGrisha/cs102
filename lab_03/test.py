import pygame
from pygame.locals import *
import random


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        # PUT YOUR CODE HERE

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


        def cell_list(self, randomize=True) -> list:
            """ Создание списка клеток.

            :param randomize: Если True, то создается список клеток, где
            каждая клетка равновероятно может быть живой (1) или мертвой (0).
            :return: Список клеток, представленный в виде матрицы
            """

            self.clist = []
            if randomize:
                for i in range(self.cell_width):
                    temp = []
                    for j in range(self.cell_height):
                        temp.append(random.randint(0,1))
                    self.clist.append(temp)
            else:
                for i in range(self.cell_width):
                    temp = []
                    for j in range(self.cell_height):
                        temp.append(0)
                    self.clist.append(temp)
            return self.clist
        print(self.cell_size)

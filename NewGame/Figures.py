# -*- coding:utf-8 -*-

"""В этом файле я просто поместил класс создания рандомных фигур."""

from pygame.draw import aalines
from math import cos, sin
from random import random, randint, choice

class Round_square(object):
    """В данном классе создаются фигуры, так как не требуется обнаруживать столкновения и все остальные функции спрайтов,
        то создается объект без image и rect. В конструкторе задаются step_radius = скорость увеличения радиуса,
        points = точки для отрисовки линий, step = скорость вращения фигуры, angle = начальный угол вращения (всегда начинается с нуля),
        num_angles = выбирается случайное количество углов из списка величин."""
    def __init__(self, x = 0, y = 0):
        self.radius = 0
        self.step_radius = random()
        self.points = []
        self.step = random()/10
        self.angle = 0
        self.x = x
        self.y = y
        self.color = (randint(10, 100), randint(10, 100), randint(10, 100))
        self.num_angles = choice([3, 4, 5, 6, 7, 30])

    def update(self):
        """При каждом обновлении объекта изменяется его радиус и угол на определенную величину.
            Points обнуляется, чтобы снова заполниться в цикле.
            Создание точек происходит очень просто - pi (3,14) это половина окружности, соответственно 3,14*2 это вся окружность.
            Окружность чертится с помощью sin и cos, остается только через определенные интервалы на окружности отметить точки и поместить их в список.
            Чтобы узнать через какой интервал на окружности точки отмечать, достаточно разделить 6.28 на количество углов.
            Потом эту величину прибавлять к начальному углу и таким образом будут найдены все точки."""
        self.points = []
        self.radius += self.step_radius
        self.angle += self.step
        v = 0
        for _ in range(self.num_angles):
            self.points.append((cos(self.angle+v)*self.radius+self.x,
                                sin(self.angle+v)*self.radius+self.y))
            v += 6.28/self.num_angles

    def blit(self, surface):
        """При отрисовке все точки объекта просто соединяются линиями, так получается фигура от треугольника, до круга.
        P.S. А если в процессе обновления объекта ему еще и количество углов увеличивать, то можно пронаблюдать как
        треугольник превращается в квадрат, в пятиунольник и так до круга."""
        self.update()
        aalines(surface, self.color, 1, self.points, 1)

    def update2(self, surface):
        """Данная функция является модификацией вышеописанной update, она принимает в качестве параметра поверхность
        на которую будет отрисовываться фигура. В ней не изменяется радиус фигуры, а также сразу производится отрисовка на поверхность.
        cos(self.angle+v)*(self.radius-2)+self.x+self.radius - тут от радиуса отнимается 2 для того, чтобы границы фигуры
        вмещались на поверхность отрисовки, а в конце прибалвяется радиус для того, чтобы фигура отрисовывалась по центру
        поверхности.
        """
        self.points = []
        self.angle += self.step
        v = 0
        for _ in range(self.num_angles):
            self.points.append((cos(self.angle+v)*(self.radius-2)+self.x+self.radius,
                                sin(self.angle+v)*(self.radius-2)+self.y+self.radius))
            v += 6.28/self.num_angles
        aalines(surface, self.color, 1, self.points, 1)
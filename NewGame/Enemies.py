# -*- coding:utf-8 -*-

from pygame import sprite, Surface, draw
from Figures import Round_square
from random import randint

class Enemy(sprite.Sprite):
    """Тут всё то же самое что и в классе Gun, за исключением нескольких отличий -
    радиус больше, цветовой диапазон меньше, координата Y изменяется в большую сторону.
    Создается объект, самый обыкновенный спрайт,
    но свойству self.f присваивается объект класса Round_square. Далее объекту self.f объекта
    задаются (по сути меняются, потому что они уже заданы по умолчанию) радиус и цвет.
    В методе update image текущего объекта перекрашивается, а потом с помощью update2
    объект self.f отображается на image текущего объекта.
    На объекты класса Enemy игрок не может влиять, поэтому они далее просто изменяют координату y.
    (Враги летят вниз, летят и вращаются.)."""
    def __init__(self, x, y, vel=1):
        sprite.Sprite.__init__(self)
        self.vel = vel
        self.xvel = 0
        self.yvel = 0
        self.image = Surface((30, 30))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.f = Round_square(0, 0)
        self.f.radius = 15
        self.f.color = (randint(150, 255), randint(150, 255), randint(150, 255))

    def update(self):
        self.image.fill((0, 0, 0))
        self.f.update2(self.image)

        self.yvel = self.vel

        self.rect.y += self.yvel
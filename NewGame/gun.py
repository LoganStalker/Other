# -*-coding:utf-8 -*-

from pygame import sprite, Surface
from Figures import Round_square
from random import randint

class Gun(sprite.Sprite):
    """Тут всё просто, создается объект, самый обыкновенный спрайт,
    но свойству self.f присваивается объект класса Round_square. Далее объекту self.f объекта
    задаются (по сути меняются, потому что они уже заданы по умолчанию) радиус и цвет.
    В методе update image текущего объекта перекрашивается, а потом с помощью update2
    объект self.f отображается на image текущего объекта.
    На объекты класса Gun игрок не может влиять, поэтому они далее просто изменяют координату y.
    (Пули летят вверх, летят и вращаются.)."""
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.image = Surface((20, 20))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.f = Round_square(0, 0)
        self.f.radius = 8
        self.f.color = (randint(100, 255), randint(100, 255), randint(100, 255))

    def update(self):
        self.image.fill((0, 0, 0))
        self.f.update2(self.image)

        self.yvel = -10

        self.rect.y += self.yvel
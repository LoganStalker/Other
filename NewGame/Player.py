# -*- coding:utf-8 -*-

from pygame import sprite, Surface, draw

MOVE_SPEED = 10

class Player(sprite.Sprite):
    def __init__(self, x, y):
        """Тут создается обыкновенный объект персонажа игрока, отличие от ранее создаваемых лишь в том,
        что для image не загружается изображение, а рисуется процедурно, по ранее заданным точкам."""
        sprite.Sprite.__init__(self)
        self.image = Surface((50, 50))
        self.image.set_colorkey((0, 0, 0))
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ochki = 0
        self.points = ((10, 15), (20, 15), (20, 26), (30, 26), (30, 15), (40, 15),
                       (40, 45), (10, 45), (10, 15), (20, 15), (20, 26), (15, 26),
                       (15, 38), (35, 38), (35, 26), (30, 26), (30, 7), (20, 7), (20, 15))

    def update(self, left, right):
        self.image.fill((0, 0, 0))
        draw.aalines(self.image, (150, 255, 150), 1, self.points, 1)

        if left:
            self.xvel = -MOVE_SPEED

        if right:
            self.xvel = MOVE_SPEED

        if not(left or right):
            self.xvel = 0

        self.rect.x += self.xvel
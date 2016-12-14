# -*- coding:utf-8 -*-

import pygame
from random import randint
from Player import Player
from gun import Gun
from Enemies import Enemy
from Figures import Round_square

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W = window.get_width()
H = window.get_height()

pygame.font.init()
ff = pygame.font.Font(None, 32)

hero = Player((W/2)-25, H-150)
global_group = pygame.sprite.Group()
global_group.add(hero)
update_group = pygame.sprite.Group()
upd_list = []
enemy_list = []

square_list = []
done = True
left = right = False
enemy_speed = 1
shot = False
timer = pygame.time.Clock()
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = False
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_SPACE:
                shot = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_SPACE:
                shot = False

    window.fill((30, 30, 50))

    '''Если пробел нажат, то shot будет True, а дальше проверяется, если в списке
    меньше 30 объектов класса Gun, то создаем новый объект и помещаем его в группу для отрисовки,
    и в список для обновления'''
    if shot == True:
        if len(upd_list) < 30:
            gn = Gun(hero.rect.x+20, hero.rect.y)
            update_group.add(gn)
            upd_list.append(gn)

    '''Это относится к фону.
    Если в списке фоновых фигур меньше 500 объектов, то в список объектов добавляется от 1 до 5
    объектов.'''
    if len(square_list) < 500:
        for i in range(randint(1, 5)):
            square_list.append(Round_square(randint(0, W), randint(0, H)))

    '''Обновление фоновых фигур, если радиус фигуры больше 50, то она удаляется из списка.'''
    for sq in square_list:
        if sq.radius >= 50:
            square_list.remove(sq)
        else:
            sq.blit(window)

    # Обновление героя.
    hero.update(left, right)

    '''Обновление всех объектов класса Gun (снарядов).
    Если Y-координата снаряда меньше -10, то снаряд удаляется из списка и группы.'''
    for g in upd_list:
        g.update()
        if g.rect.y < -10:
            upd_list.remove(g)
            update_group.remove(g)

    '''Респаун врагов.
    Если врагов меньше 50 штук, то создаем нового врага и добавляем его в группу обновления и список отображения'''
    if len(enemy_list) < 50:
        enemy = Enemy(randint(10, W-hero.rect.width), 20, enemy_speed)
        enemy_list.append(enemy)
        update_group.add(enemy)

    '''Обновление врагов и отслеживание столкновений со снарядами.
    Если враг и снаряд пересеклись, то оба удаляются из своих групп,
    снаряд удаляется из своего списка, а прежде чем удалить врага, производится проверка его
    существования в списке. Эта проверка нужна для того, чтобы не возникло ошибки итерации цикла.
    Так как цикл совершает проходку по этому списку, то при удалении объекта без проверки,
    может возникнуть ошибка, когда во внутреннем цикле попытаются удалить существующий объект.'''
    for enemy in enemy_list:
        enemy.update()
        for gn in upd_list:
            if pygame.sprite.collide_rect(enemy, gn):
                update_group.remove(gn)
                update_group.remove(enemy)
                upd_list.remove(gn)
                if enemy in enemy_list:
                    enemy_list.remove(enemy)
                # ведется подсчет очков, но они ни где не используются. По сути просто ведется подсчет сбитых врагов.
                hero.ochki += 1

    update_group.draw(window)
    global_group.draw(window)

    window.blit(ff.render(str(hero.ochki), 1, (255, 255, 255)), (10, 10))
    window.blit(ff.render(str(enemy_speed), 1, (255, 255, 255)), (150, 10))

    pygame.display.flip()
    timer.tick(40)

pygame.quit()
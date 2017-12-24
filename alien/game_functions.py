import sys
import pygame
from bullet import Bullet
from enemy import Enemy

__author__ = 'heshipeng'


def check_events(ship, ali_settings, screen, bullets):
    # 监视鼠标和键盘事件
    for event in pygame.event.get():
        check_move_event(event, ship, ali_settings, screen, bullets)


# 监听移动事件
def check_move_event(event, ship, ali_settings, screen, bullets):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:

        if event.key == pygame.K_RIGHT:
            ship.move_right = True
        elif event.key == pygame.K_LEFT:
            ship.move_left = True

        elif event.key == pygame.K_SPACE:
            fire(ali_settings, screen, ship, bullets)

        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.move_right = False
        elif event.key == pygame.K_LEFT:
            ship.move_left = False


def fire(ali_settings, screen, ship, bullets):
    # 创建一颗子弹，并将其加入到编组bullets 中
    if len(bullets) < ali_settings.bullet_max_num:
        new_bullet = Bullet(ali_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ali_settings, background, screen, ship, enemys, bullets):

    # 每次循环时都重新绘制屏幕
    # screen.fill(ali_settings.bg_color)
    screen.blit(background, (0, 0))

    # 在外星人和飞船后面重新画子弹,这个必须在重新绘制屏幕之前
    # for bullet in bullets:
    #     bullet.draw_bullet()
    bullets.draw(screen)

    ship.blitme()
    enemys.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(enemys, bullets):
    bullets.update()

    # 删除消息的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)


def create_enemy(ali_settins, screen, enemys):
    if len(enemys) <= 0:
        enemy = Enemy(ali_settins, screen)
        enemys.add(enemy)


def update_enemy(enemys):
    """ 敌方飞机移动 """
    enemys.update()

def delete_enemy_out(enemys, screen, ali_settings):
    # 删除消失在屏幕外的飞机
    for enemy in enemys:
        if enemy.rect.left > screen.get_rect().right:
            enemys.remove(enemy)

        if enemy.rect.top > screen.get_rect().bottom:
            enemys.remove(enemy)

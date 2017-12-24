import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

__author__ = 'heshipeng'


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ali_settings = Settings()
    screen = pygame.display.set_mode((ali_settings.screen_width, ali_settings.screen_height))
    pygame.display.set_caption("飞机大战 不服就是搞")
    background = pygame.image.load('images/star_bg.jpg')
    background = pygame.transform.scale(background, (1200, 800))

    ship = Ship(screen, ali_settings)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 敌方飞机
    enemys = Group()

    # 设置背景颜色
    # bg_color = (230, 230, 230)

    # 开始游戏主循环
    while True:

        gf.check_events(ship, ali_settings, screen, bullets)

        ship.update()

        gf.create_enemy(ali_settings, screen, enemys)
        gf.delete_enemy_out(enemys, screen, ali_settings)

        gf.update_bullets(enemys, bullets)

        gf.update_enemy(enemys)

        gf.update_screen(ali_settings, background, screen, ship, enemys, bullets)

run_game()


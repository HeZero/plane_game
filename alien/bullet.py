import pygame
from pygame.sprite import Sprite

__author__ = 'heshipeng'


class Bullet(Sprite):
    """ 飞机子弹类"""

    def __init__(self, ali_settings, screen, ship):
        """ 在飞机位置新建子弹对象 """
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        # self.rect = pygame.Rect(0, 0, ali_settings.bullet_width, ali_settings.bullet_height)
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/bullet.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.bottom = ship.rect.top
        self.rect.left = ship.rect.left + 42.5

        # 用小数表示子弹位置
        self.y = float(self.rect.y)
        self.color = ali_settings.bullet_color
        self.speed_factor = ali_settings.bullet_speed_factor

    # def draw_bullet(self):
    #     """ 在屏幕上绘制子弹 """
    #     # pygame.draw.rect(self.screen, self.color, self.rect)
    #     self.rect.x = 0
    #     self.rect.y = 0

    def update(self, *args):
        """ 向上移动子弹 """
        self.y -= self.speed_factor
        # 更新子弹位置
        self.rect.y = self.y

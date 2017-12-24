from random import random
import pygame
from pygame.sprite import Sprite

__author__ = 'heshipeng'


class Enemy(Sprite):
    """ 敌方飞机类 """

    def __init__(self, ali_settings, screen):
        """ 初始化外星人并设置其初始位置 """
        super(Enemy, self).__init__()
        self.screen = screen
        self.ali_settings = ali_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/enemy_plane.png')
        self.rect = self.image.get_rect()

        # 根据敌方飞机出现位置判断移动方向
        self.move_right = True

        # 每个外星人初始都在屏幕左上角附近
        self.rect.x = self.get_width()
        self.rect.y = self.rect.height

        # 存储敌方飞机的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """ 在指定位置画敌方飞机 """
        self.screen.blit(self.image, self.rect)

    def update(self, *args):

        if self.move_right:
            self.x += self.ali_settings.enemy_speed_factor
        else:
            self.x -= self.ali_settings.enemy_speed_factor

        self.y += self.ali_settings.enemy_speed_factor

        self.rect.x = self.x
        self.rect.y = self.y

    def get_width(self):
        width_range = [0, self.screen.get_rect().right]
        if random() > 0.5:
            self.move_right = True
            return width_range[0]
        else:
            self.move_right = False
            return width_range[1]
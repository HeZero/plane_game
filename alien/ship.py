import pygame

__author__ = 'heshipeng'


class Ship():

    def __init__(self, screen, ali_settings):
        """ 初始化飞船并设置其初始位置 """
        self.screen = screen
        self.ali_settings = ali_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/plane.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 用来存储小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.move_right = False
        self.move_left = False

    def blitme(self):
        """ 在指定位置绘制飞机 """
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ali_settings.ship_speed_factor

        if self.move_left and self.rect.left > 0:
            self.center -= self.ali_settings.ship_speed_factor

        self.rect.centerx = self.center
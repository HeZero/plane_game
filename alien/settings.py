__author__ = 'heshipeng'


class Settings():
    """ 存储外星人入侵的所有配置类 """

    def __init__(self):
        """ 初始化游戏设置 """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞机移动速度
        self.ship_speed_factor = 5

        # 子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 230, 230)
        # 屏幕上最多可以有5颗子弹
        self.bullet_max_num = 5

        # 敌方飞机移动速度
        self.enemy_speed_factor = 3
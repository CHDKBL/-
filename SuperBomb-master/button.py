import pygame

PAUSE = 1
CONTINUE = 2
BACKMENU = 3
RESTART = 4
START = 5
HELP = 6
CLOSE = 7


class Button(object):
    """docstring for Button"""

    def __init__(self, upimage, pos, screen, category, enabled):
        self.upimage = pygame.image.load(upimage).convert_alpha()  # 获取按钮图片
        self.pos = pos  # 按钮位置
        self.screen = screen  # 获取屏幕对象
        self.screen.blit(self.upimage, self.pos)  # 绘制按钮
        self.leave_btn = True
        self.category = category  # 按钮种类
        self.enabled = enabled

    def isOver(self):
        """判断鼠标是否在上面"""
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.pos
        w, h = self.upimage.get_size()
        return (x < point_x and point_x < x + w) and (y < point_y and point_y < y + h)

    def isClick(self):

        if self.isOver():  # and self.leave_btn:
            pressed_arr = pygame.mouse.get_pressed()  # 获取鼠标事件（左键、中键、右键）
            if pressed_arr[0] == 1:
                self.leave_btn = False
                return True
        return False

    @staticmethod
    def btn_deal(screen, is_pause, btn_pause, btn_continue, btn_backmenu, btn_restart):
        if is_pause:
            screen.blit(pygame.image.load(
                'resources/image/tips_board.png').convert_alpha(), (100, 100))
        if btn_pause.enabled is True:
            if btn_pause.render() is True:  # 按暂停按钮，显示继续、回菜单、重开按钮
                is_pause = True
                btn_continue.enabled = True
                btn_backmenu.enabled = True
                btn_restart.enabled = True

        if btn_continue.enabled is True:
            if btn_continue.render() is True:  # 按继续按钮，不显示继续、回菜单、重开按钮
                is_pause = False
                btn_continue.enabled = False
                btn_backmenu.enabled = False
                btn_restart.enabled = False

        is_mainmenu = False
        if btn_backmenu.enabled is True:
            if btn_backmenu.render() is True:  # 按回菜单按钮，不显示继续、回菜单、重开按钮
                is_mainmenu = True
                is_pause = False
                btn_continue.enabled = False
                btn_restart.enabled = False
                btn_backmenu.enabled = False
        is_restart = False
        if btn_restart.enabled is True:
            if btn_restart.render() is True:   # 按重开按钮，不显示继续、回菜单、重开按钮
                is_restart = True
                is_mainmenu = False
                is_pause = False
                btn_continue.enabled = False
                btn_restart.enabled = False
                btn_backmenu.enabled = False

        return is_pause, is_mainmenu, is_restart

    def render(self):
        """show which pic"""
        self.screen.blit(self.upimage, self.pos)
        if self.isClick():
            return True
        return False

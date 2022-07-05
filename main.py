import random
from turtle import *
from msvcrt import getch


N = 3

TurtleWindowHeight = 800
Border = 100
Scale = 0.8     # 骨牌大小 填满为1


class ChessCover:
    def __init__(self, side_length):
        self.orig_length = 2**side_length
        self.board = [['' for i in range(self.orig_length)] for i in range(self.orig_length)]
        self.special_point = [random.randint(1, self.orig_length - 1), random.randint(0, self.orig_length - 1)]

        self.special_point_to_print = [self.special_point[0]+1, self.special_point[1]+1]
        self.each_squar_length = TurtleWindowHeight//self.orig_length
        self.scale = (1-Scale)/2
        self.ZERO = -self.orig_length / 2 * self.each_squar_length

        self._init_canvas()
        self._paint_special_point()

        pensize(2)
        width(2)
        pencolor('red')

        self.ChessCover()

    def _init_canvas(self):
        setup(TurtleWindowHeight+Border, TurtleWindowHeight+Border)
        penup()
        pensize(1)
        width(1)
        pencolor('black')
        speed(100)

        goto(self.ZERO, self.ZERO)
        for i in range(self.orig_length):       # 以下为画行
            goto(self.ZERO, self.ZERO+i*self.each_squar_length)
            pendown()
            goto(-self.ZERO, self.ZERO+i*self.each_squar_length)
            penup()
            for j in [1, -1]:
                goto(j*(self.ZERO-Border/4), self.ZERO + i * self.each_squar_length+self.each_squar_length*(1/3))       # 写行标
                write(str(i+1), ['', 25])
        goto(self.ZERO, self.ZERO+(i+1)*self.each_squar_length)
        pendown()
        goto(-self.ZERO, self.ZERO + (i+1) * self.each_squar_length)
        penup()
        for i in range(self.orig_length):     # 以下为画列
            goto(self.ZERO+i*self.each_squar_length, self.ZERO)
            pendown()
            goto(self.ZERO+i*self.each_squar_length, -self.ZERO)
            penup()
            for j in [1, -1]:
                goto(self.ZERO + i * self.each_squar_length + self.each_squar_length * (1 / 3), j * (self.ZERO - Border/4))  # 写列标
                write(str(i + 1), ['', 25])
        goto(self.ZERO + (i+1) * self.each_squar_length, self.ZERO)
        pendown()
        goto(self.ZERO + (i+1) * self.each_squar_length, -self.ZERO)
        penup()

    def _paint_upper_vertical(self, _position):
        penup()
        goto(_position[0]+self.scale*self.each_squar_length, _position[1])
        pendown()
        goto(_position[0]+self.scale*self.each_squar_length, _position[1]+(1-self.scale)*self.each_squar_length)
        goto(_position[0]+(1-self.scale)*self.each_squar_length, _position[1]+(1-self.scale)*self.each_squar_length)
        goto(_position[0]+(1-self.scale)*self.each_squar_length, _position[1])
        penup()

    def _paint_lower_vertical(self, _position):
        penup()
        goto(_position[0] + self.scale * self.each_squar_length, _position[1]+self.each_squar_length)
        pendown()
        goto(_position[0] + self.scale * self.each_squar_length,
             _position[1] + self.scale * self.each_squar_length)
        goto(_position[0] + (1 - self.scale) * self.each_squar_length,
             _position[1] + self.scale * self.each_squar_length)
        goto(_position[0] + (1 - self.scale) * self.each_squar_length, _position[1]+self.each_squar_length)
        penup()

    def _paint_left_horizontal(self, _position):
        penup()
        goto(_position[0] + self.each_squar_length, _position[1]+(1 - self.scale) * self.each_squar_length)
        pendown()
        goto(_position[0] + self.scale * self.each_squar_length,
             _position[1] + (1 - self.scale) * self.each_squar_length)
        goto(_position[0] + self.scale * self.each_squar_length,
             _position[1] + self.scale * self.each_squar_length)
        goto(_position[0] + self.each_squar_length, _position[1] + self.scale * self.each_squar_length)
        penup()

    def _paint_right_horizontal(self, _position):
        penup()
        goto(_position[0], _position[1]+self.scale * self.each_squar_length)
        pendown()
        goto(_position[0] + (1 - self.scale) * self.each_squar_length,
             _position[1]+self.scale * self.each_squar_length)
        goto(_position[0] + (1 - self.scale) * self.each_squar_length,
             _position[1] + (1 - self.scale) * self.each_squar_length)
        goto(_position[0], _position[1]+(1 - self.scale) * self.each_squar_length)
        penup()

    def _paint_upper_left(self, _position):
        penup()
        goto(_position[0]+self.scale * self.each_squar_length, _position[1])
        pendown()
        goto(_position[0] + self.scale * self.each_squar_length,
             _position[1] + (1 - self.scale) * self.each_squar_length)
        goto(_position[0] + self.each_squar_length,
             _position[1] + (1 - self.scale) * self.each_squar_length)
        penup()
        goto(_position[0] + self.each_squar_length,
             _position[1] + self.scale * self.each_squar_length)
        pendown()
        goto(_position[0] + (1 - self.scale) * self.each_squar_length,
             _position[1] + self.scale*self.each_squar_length)
        goto(_position[0] + (1 - self.scale) * self.each_squar_length,
             _position[1])
        penup()

    def _paint_upper_right(self, _position):
        penup()
        goto(_position[0], _position[1] + (1 - self.scale) * self.each_squar_length)
        pendown()
        goto(_position[0] + (1 - self.scale) * self.each_squar_length,
             _position[1] + (1 - self.scale) * self.each_squar_length)
        goto(_position[0] + (1 - self.scale) * self.each_squar_length,
             _position[1])
        penup()
        goto(_position[0] + self.scale*self.each_squar_length,
             _position[1])
        pendown()
        goto(_position[0] + self.scale*self.each_squar_length,
             _position[1] + self.scale*self.each_squar_length)
        goto(_position[0],
             _position[1] + self.scale*self.each_squar_length)
        penup()

    def _paint_lower_left(self, _position):
        penup()
        goto(_position[0]+self.scale*self.each_squar_length, _position[1] + self.each_squar_length)
        pendown()
        goto(_position[0] + self.scale * self.each_squar_length,
             _position[1] + self.scale * self.each_squar_length)
        goto(_position[0] + self.each_squar_length,
             _position[1] + self.scale * self.each_squar_length)
        penup()
        goto(_position[0] + self.each_squar_length,
             _position[1] + (1 - self.scale) * self.each_squar_length)
        pendown()
        goto(_position[0] + (1 - self.scale)*self.each_squar_length,
             _position[1] + (1 - self.scale)*self.each_squar_length)
        goto(_position[0] + (1 - self.scale)*self.each_squar_length,
             _position[1] + self.each_squar_length)
        penup()

    def _paint_lower_right(self, _position):
        penup()
        goto(_position[0], _position[1] + self.scale * self.each_squar_length)
        pendown()
        goto(_position[0] + (1 - self.scale) * self.each_squar_length,
             _position[1] + self.scale * self.each_squar_length)
        goto(_position[0] + (1 - self.scale) * self.each_squar_length,
             _position[1] + self.each_squar_length)
        penup()
        goto(_position[0] + self.scale*self.each_squar_length,
             _position[1] + self.each_squar_length)
        pendown()
        goto(_position[0] + self.scale*self.each_squar_length,
             _position[1] + (1 - self.scale) * self.each_squar_length)
        goto(_position[0],
             _position[1] + (1 - self.scale) * self.each_squar_length)
        penup()

    def _paint_special_point(self):
        penup()
        pensize(5)
        width(5)
        pencolor('blue')
        goto(self.ZERO+self.special_point[0]*self.each_squar_length+self.scale*self.each_squar_length,
             self.ZERO+self.special_point[1]*self.each_squar_length+self.scale*self.each_squar_length)
        pendown()
        goto(self.ZERO+self.special_point[0]*self.each_squar_length+self.scale*self.each_squar_length,
             self.ZERO+self.special_point[1]*self.each_squar_length+(1-self.scale)*self.each_squar_length)
        goto(self.ZERO+self.special_point[0]*self.each_squar_length+(1-self.scale)*self.each_squar_length,
             self.ZERO+self.special_point[1]*self.each_squar_length+(1-self.scale)*self.each_squar_length)
        goto(self.ZERO+self.special_point[0]*self.each_squar_length+(1-self.scale)*self.each_squar_length,
             self.ZERO+self.special_point[1]*self.each_squar_length+self.scale*self.each_squar_length)
        goto(self.ZERO+self.special_point[0]*self.each_squar_length+self.scale*self.each_squar_length,
             self.ZERO+self.special_point[1]*self.each_squar_length+self.scale*self.each_squar_length)
        penup()

    def chess_cover(self, position, n_length, special_point):
        '''

        :param position: 该子棋盘左下角坐标
        :param n_length: 该子棋盘边长
        :param special_point: 该子棋盘特殊点坐标
        :return:
        '''
        a = special_point
        n = n_length
        if n == 1:
            return
        else:
            A_11 = [position[0],position[1]+n/2*self.each_squar_length]
            A_12 = [position[0]+n/2*self.each_squar_length,position[1]+n/2*self.each_squar_length]
            A_21 = [position[0],position[1]]
            A_22 = [position[0]+n/2*self.each_squar_length,position[1]]
            if special_point[0] <position[0]+ n / 2*self.each_squar_length:  # 特殊点位于棋盘左半边
                if special_point[1] <position[1]+ n / 2*self.each_squar_length:  # 特殊点位于棋盘左下角
                    a_11 = [position[0] + (n / 2 - 1) * self.each_squar_length,
                            position[1] + n / 2 * self.each_squar_length]
                    a_12 = [position[0] + n / 2 * self.each_squar_length, position[1] + n / 2 * self.each_squar_length]
                    a_21 = a
                    a_22 = [position[0] + n / 2 * self.each_squar_length,
                            position[1] + (n / 2 - 1) * self.each_squar_length]
                    self._paint_left_horizontal(a_11)
                    self._paint_upper_right(a_12)
                    self._paint_lower_vertical(a_22)
                    self.chess_cover(A_11, n/2, a_11)
                    self.chess_cover(A_12, n/2, a_12)
                    self.chess_cover(A_21, n/2, a_21)
                    self.chess_cover(A_22, n/2, a_22)
                else:  # 特殊点位于棋盘左上角
                    a_11 = a
                    a_12 = [position[0] + n / 2 * self.each_squar_length, position[1] + n / 2 * self.each_squar_length]
                    a_21 = [position[0] + (n / 2 - 1) * self.each_squar_length,
                            position[1] + (n / 2 - 1) * self.each_squar_length]
                    a_22 = [position[0] + n / 2 * self.each_squar_length,
                            position[1] + (n / 2 - 1) * self.each_squar_length]
                    self._paint_upper_vertical(a_12)
                    self._paint_left_horizontal(a_21)
                    self._paint_lower_right(a_22)

                    self.chess_cover(A_11, n/2, a_11)
                    self.chess_cover(A_12, n/2, a_12)
                    self.chess_cover(A_21, n/2, a_21)
                    self.chess_cover(A_22, n/2, a_22)
            else:  # 特殊点位于棋盘右半边
                if special_point[1] <position[1]+  n / 2*self.each_squar_length:  # 特殊点位于棋盘右下角
                    a_11 = [position[0] + (n / 2 - 1) * self.each_squar_length,
                            position[1] + n / 2 * self.each_squar_length]
                    a_12 = [position[0] + n / 2 * self.each_squar_length, position[1] + n / 2 * self.each_squar_length]
                    a_21 = [position[0] + (n / 2 - 1) * self.each_squar_length,
                            position[1] + (n / 2 - 1) * self.each_squar_length]
                    a_22 = a
                    self._paint_upper_left(a_11)
                    self._paint_right_horizontal(a_12)
                    self._paint_lower_vertical(a_21)

                    self.chess_cover(A_11, n/2, a_11)
                    self.chess_cover(A_12, n/2, a_12)
                    self.chess_cover(A_21, n/2, a_21)
                    self.chess_cover(A_22, n/2, a_22)
                else:  # 特殊点位于棋盘右上角
                    a_11 = [position[0] + (n / 2 - 1) * self.each_squar_length,
                            position[1] + n / 2 * self.each_squar_length]
                    a_12 = a
                    a_21 = [position[0] + (n / 2 - 1) * self.each_squar_length,
                            position[1] + (n / 2 - 1) * self.each_squar_length]
                    a_22 = [position[0] + n / 2 * self.each_squar_length,
                            position[1] + (n / 2 - 1) * self.each_squar_length]
                    self._paint_upper_vertical(a_11)
                    self._paint_lower_left(a_21)
                    self._paint_right_horizontal(a_22)

                    self.chess_cover(A_11, n/2, a_11)
                    self.chess_cover(A_12, n/2, a_12)
                    self.chess_cover(A_21, n/2, a_21)
                    self.chess_cover(A_22, n/2, a_22)
        return

    def ChessCover(self):
        special_point = [self.ZERO+self.special_point[0]*self.each_squar_length,
                         self.ZERO+self.special_point[1]*self.each_squar_length]
        self.chess_cover([self.ZERO,self.ZERO], self.orig_length, special_point)
        goto(2*(TurtleWindowHeight+Border),2*(TurtleWindowHeight+Border))


if __name__ == '__main__':
    a = ChessCover(N)
    print(a.special_point)

    print('-' * 10 + '按任意键退出程序' + '-' * 10)
    getch()
    exit()

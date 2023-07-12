import dot
import pygame
from constants import *
import datetime

class Clock():
    def __init__(self):
        self.time = datetime.datetime.now()
        self.ten_hours_dots = []
        self.hours_dots = []
        self.ten_mins_dots = []
        self.mins_dots = []
        self.ten_seconds_dots = []
        self.seconds_dots = []
        self.all_dots = [self.ten_hours_dots, self.hours_dots, self.ten_mins_dots, self.mins_dots, self.ten_seconds_dots, self.seconds_dots]
        self.x_gap = BLOCK_SIZE
        self.y_gap = BLOCK_SIZE // 2
        self.y_padding = BLOCK_SIZE

        self.th = 0
        self.h = 0
        self.tm = 0
        self.m = 0
        self.ts = 0
        self.s = 0



        self.make_clock()




    def convert_dec_to_bin(self, dec):
        # print(f"dec:{dec}")
        bin = [8, 4, 2, 1]
        result = []
        for b in range(len(bin)):
            if dec >= bin[b]:
                result.append(1)
                dec = dec - bin[b]
            else:
                result.append(0)
        # print(result)
        return result



    def update(self):
        print(self.time.strftime("%H:%M:%S"))

        self.time = datetime.datetime.now()


        self.th = int(self.time.strftime("%H")) // 10
        self.h = int(self.time.strftime("%H"))   % 10
        self.tm = int(self.time.strftime("%M")) // 10
        self.m = int(self.time.strftime("%M"))  % 10
        self.ts = int(self.time.strftime("%S")) // 10
        self.s = int(self.time.strftime("%S")) % 10
        # print(f"{self.th}{self.h}:{self.tm}{self.m}:{self.ts}{self.s}")


        th_binary_list = self.convert_dec_to_bin(self.th)
        h_binary_list = self.convert_dec_to_bin(self.h)
        tm_binary_list = self.convert_dec_to_bin(self.tm)
        m_binary_list = self.convert_dec_to_bin(self.m)
        ts_binary_list = self.convert_dec_to_bin(self.ts)
        s_binary_list = self.convert_dec_to_bin(self.s)
        all_binary_list = [th_binary_list, h_binary_list, tm_binary_list, m_binary_list, ts_binary_list, s_binary_list]


        for i in range(len(all_binary_list)):
            for j in range(len(self.all_dots[i]) - 1, -1, -1):
                print(f"i:{i}, j:{j}")
                if all_binary_list[i][j] == 1:
                        self.all_dots[i][j].turn_on()
                else:
                    self.all_dots[i][j].turn_off()


        for list in self.all_dots:
            for dot in list:
                dot.update()


    def turn_all_off(self):
        for list in self.all_dots:
            for dot in list:
                dot.turn_off()

    def draw(self, surface):
        for list in self.all_dots:
            for dot in list:
                dot.draw(surface)


    def make_clock(self):
        x = BLOCK_SIZE
        y = BLOCK_SIZE
        binary_list = [8, 4, 2, 1]


        for i in range(2):
            # x = (x * i) + (self.x_gap * i)
            y = (BLOCK_SIZE * i) + (i * self.y_gap) + self.y_padding + (BLOCK_SIZE * 1.5) * 2
            self.ten_hours_dots.append(dot.Dot(x, y, binary_list[i]))
        x = BLOCK_SIZE * 2.5
        for i in range(4):
            y = (BLOCK_SIZE * i) + (i * self.y_gap) + self.y_padding
            self.hours_dots.append(dot.Dot(x, y, binary_list[i]))
        x = BLOCK_SIZE * 4.5
        for i in range(3):
            y = (BLOCK_SIZE * i) + (i * self.y_gap) + self.y_padding + (BLOCK_SIZE * 1.5)
            self.ten_mins_dots.append(dot.Dot(x, y, binary_list[i]))
        x = BLOCK_SIZE * 6.5
        for i in range(4):
            y = (BLOCK_SIZE * i) + (i * self.y_gap) + self.y_padding
            self.mins_dots.append(dot.Dot(x, y, binary_list[i]))

        x = BLOCK_SIZE * 8.5
        for i in range(2, -1, -1):
            y = (BLOCK_SIZE * i) + (i * self.y_gap) + self.y_padding
            self.ten_seconds_dots.append(dot.Dot(x, y, binary_list[i + 1]))

        x = BLOCK_SIZE * 10.5
        for i in range(3, -1, -1):
            y = (BLOCK_SIZE * i) + (i * self.y_gap) + self.y_padding
            self.seconds_dots.append(dot.Dot(x, y, binary_list[i]))

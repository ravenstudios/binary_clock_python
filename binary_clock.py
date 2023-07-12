import dot
import pygame
from constants import *
import datetime

class Clock():
    def __init__(self):

        self.all_dots = [[], [], [], [], [], []]
        self.x_gap = BLOCK_SIZE
        self.y_gap = BLOCK_SIZE // 2
        self.y_padding = BLOCK_SIZE

        self.binary_list = [8, 4, 2, 1]
        self.list_size = [1, 3, 2, 3, 2, 3]
        self.y_offset = [3, 0, 1.5, 0, 1.5, 0]
        self.x_offset = [1, 2.1, 4, 5.1, 7, 8.1]
        self.display_number_list_offset = [2, 0, 1, 0, 1, 0]
        self.is_24_mode = True
        self.make_clock()


    def update(self, is_24_mode):
        self.is_24_mode = is_24_mode
        self.tick()

        for list in self.all_dots:
            for dot in list:
                dot.update()


    def draw(self, surface):
        for list in self.all_dots:
            for dot in list:
                dot.draw(surface)


    def make_clock(self):

        for i in range(len(self.all_dots)):
            for j in range(self.list_size[i], -1, -1):
                y = (BLOCK_SIZE * j) + (j * self.y_gap) + self.y_padding + (BLOCK_SIZE * self.y_offset[i])
                x = (BLOCK_SIZE * (self.x_offset[i]))

                self.all_dots[i].append(dot.Dot(x, y, self.binary_list[j + self.display_number_list_offset[i]]))

    def tick(self):
        d = datetime.datetime.now()
        th, h = None, None

        if self.is_24_mode:
            th = f'{(int(d.strftime("%H")) // 10):02b}'[::-1]
            h = f'{(int(d.strftime("%H")) % 10):04b}'[::-1]

        else:
            hour = int(d.strftime("%H"))
            if hour > 12:
                hour = hour - 12
            if hour == 0:
                hour = 12
            th = f'{hour // 10:02b}'[::-1]
            h = f'{hour % 10:04b}'[::-1]


        all_binary_list = [
            th,
            h,
            f'{(int(d.strftime("%M")) // 10):03b}'[::-1],
            f'{(int(d.strftime("%M")) % 10):04b}'[::-1],
            f'{(int(d.strftime("%S")) // 10):03b}'[::-1],
            f'{(int(d.strftime("%S")) % 10):04b}'[::-1]
            ]

        for i in range(len(all_binary_list) - 1, -1, -1):
            for j in range(len(self.all_dots[i]) - 1, -1, -1):
                self.all_dots[i][j].turn_on() if all_binary_list[i][j] == "1" else self.all_dots[i][j].turn_off()

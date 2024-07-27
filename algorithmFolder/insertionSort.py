import time
from colors import *


class InsertionSort:
    def __init__(self, data, draw_data, time_tick, pause_var):
        self.data = data[:]
        self.draw_data = draw_data
        self.time_tick = time_tick
        self.pause_var = pause_var

    def sort(self):
        n = len(self.data)

        for i in range(1, n):
            key = self.data[i]
            j = i - 1

            while j >= 0 and key < self.data[j]:
                if self.pause_var.get():
                    while self.pause_var.get():
                        time.sleep(0.1)
                        
                self.data[j + 1] = self.data[j]
                j -= 1

            self.data[j + 1] = key
            self.draw_data(self.data, [YELLOW if x == i or x == j + 1 else BLUE for x in range(len(self.data))])
            time.sleep(self.time_tick)

        self.draw_data(self.data, [BLUE for x in range(len(self.data))])

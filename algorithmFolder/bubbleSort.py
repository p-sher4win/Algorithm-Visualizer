import time
from colors import *


class BubbleSort:
    def __init__(self, data, draw_data, time_tick, pause_var):
        self.data = data
        self.draw_data = draw_data
        self.time_tick = time_tick
        self.pause_var = pause_var

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.pause_var.get():
                    while self.pause_var.get():
                        time.sleep(0.1)
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    color_array = [YELLOW if x == j or x == j+1 else BLUE for x in range(len(self.data))]
                    self.draw_data(self.data, color_array)
                    time.sleep(self.time_tick)
        self.draw_data(self.data, [BLUE for x in range(len(self.data))])

        

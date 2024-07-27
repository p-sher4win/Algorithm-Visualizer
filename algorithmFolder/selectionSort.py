import time
from colors import *


class SelectionSort:
    def __init__(self, data, draw_data, time_tick, pause_var):
        self.data = data[:]
        self.draw_data = draw_data
        self.time_tick = time_tick
        self.pause_var = pause_var

    def sort(self):
        self._selection_sort()
        self.draw_data(self.data, [BLUE for x in range(len(self.data))])

    def _selection_sort(self):
        for i in range(len(self.data) - 1):
            minimum = i
            for k in range(i + 1, len(self.data)):
                if self.data[k] < self.data[minimum]:
                    minimum = k

            self.data[minimum], self.data[i] = self.data[i], self.data[minimum]
            self.draw_data(self.data, [YELLOW if x == minimum or x == i else BLUE for x in range(len(self.data))])
            time.sleep(self.time_tick)

            if self.pause_var.get():
                while self.pause_var.get():
                    time.sleep(0.1)

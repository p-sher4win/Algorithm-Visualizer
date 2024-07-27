import time
from colors import *


class QuickSort:
    def __init__(self, data, draw_data, time_tick, pause_var):
        self.data = data[:]
        self.draw_data = draw_data
        self.time_tick = time_tick
        self.pause_var = pause_var

    def sort(self):
        self._quick_sort(0, len(self.data) - 1)
        self.draw_data(self.data, [BLUE for x in range(len(self.data))])

    def _quick_sort(self, start, end):
        if start < end:
            pivot_position = self._partition(start, end)
            self._quick_sort(start, pivot_position - 1)
            self._quick_sort(pivot_position + 1, end)

            self.draw_data(self.data, [
                PURPLE if x >= start and x < pivot_position else YELLOW if x == pivot_position
                else DARK_BLUE if x > pivot_position and x <= end else BLUE for x in range(len(self.data))
            ])
            time.sleep(self.time_tick)

            if self.pause_var.get():
                while self.pause_var.get():
                    time.sleep(0.1)

    def _partition(self, start, end):
        i = start + 1
        pivot = self.data[start]

        for j in range(start + 1, end + 1):
            if self.data[j] < pivot:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                i += 1
        self.data[start], self.data[i - 1] = self.data[i - 1], self.data[start]
        return i - 1

import time
from colors import *


class MergeSort:
    def __init__(self, data, draw_data, time_tick, pause_var):
        self.data = data[:]
        self.draw_data = draw_data
        self.time_tick = time_tick
        self.pause_var = pause_var

    def sort(self):
        self._merge_sort(0, len(self.data) - 1)
        self.draw_data(self.data, [BLUE for x in range(len(self.data))])

    def _merge(self, start, mid, end):
        p = start
        q = mid + 1
        temp_array = []

        for i in range(start, end + 1):
            if p > mid:
                temp_array.append(self.data[q])
                q += 1
            elif q > end:
                temp_array.append(self.data[p])
                p += 1
            elif self.data[p] < self.data[q]:
                temp_array.append(self.data[p])
                p += 1
            else:
                temp_array.append(self.data[q])
                q += 1

        for p in range(len(temp_array)):
            self.data[start] = temp_array[p]
            start += 1

    def _merge_sort(self, start, end):
        if start < end:
            mid = int((start + end) / 2)
            self._merge_sort(start, mid)
            self._merge_sort(mid + 1, end)

            self._merge(start, mid, end)

            self.draw_data(self.data, [PURPLE if x >= start and x < mid else YELLOW if x == mid
                                        else DARK_BLUE if x > mid and x <= end else BLUE for x in range(len(self.data))])
            time.sleep(self.time_tick)

            if self.pause_var.get():
                while self.pause_var.get():
                    time.sleep(0.1)

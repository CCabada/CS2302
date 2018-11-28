'''
  Carlos Cabada
  CS 2302 - Fall 2018
  Lab Assignment No.5 : Heap.py
  Date: November 11, 2018
  Instructor: Diego Aguirre
  Purpose: Heap class definition/implemintation.

'''

import pdb
class Heap:
    # Initializing heap array
    def __init__(self):
        self.heap_array = []
    # Insert method for heaps
    def insert(self, k):
        self.heap_array.append(k)
        i = len(self.heap_array) - 1
        while (i - 1 // 2) > 0:

            if self.heap_array[i] < self.heap_array[(i - 1) // 2]:
                temp = self.heap_array[(i - 1) // 2]
                self.heap_array[(i - 1) // 2] = self.heap_array[i]
                self.heap_array[i] = temp
            i = (i - 1) // 2
        return self.heap_array

    # Extracts the root of the heap/ Minimum element.
    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]
        min = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = min
            self.perc_down(0)

        return min_elem

    def perc_down(self, k):
        c = 2 * k + 1
        item = self.heap_array[k]
        while c < len(self.heap_array):
            min = item
            min_index = -1
            i = 0
            while i < 2 and i + c < len(self.heap_array):
                if self.heap_array[i + c] < min:
                    min = self.heap_array[i + c]
                    min_index = i + c
                i = i + 1
            if min == item:
                return
            else:
                temp = self.heap_array[k]
                self.heap_array[k] = self.heap_array[min_index]
                self.heap_array[min_index] = temp
                k = min_index
                c = 2 * k + 1

    def is_empty(self):
        return len(self.heap_array) == 0

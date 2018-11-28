'''
  Carlos Cabada
  CS 2302 - Fall 2018
  Lab Assignment No.5 : Main.py
  Date: November 24, 2018
  Instructor: Diego Aguirre
  Purpose: Implementation heap sort using the Heap class.
'''

from Heap import Heap


def main():
    filename = "Numbers.txt"
    '''numbers = [30, 98, 46, 44, 41, 83, 38, 35, 46, 75, 40, 53, 95, 60, 41, 59, 7, 65, 48, 4, 5, 26, 45, 58, 34, 8, 86,
               56, 32, 63, 5, 13, 99, 21, 47, 8, 50, 9, 89, 98, 95, 38, 23, 73, 88, 39, 75, 56, 71, 79, 12, 92, 9, 24,
               54, 68, 23, 78, 49, 62, 7, 9, 8, 10, 95, 8, 43, 77, 95, 45, 63, 25, 52, 82, 7, 43, 33, 52, 23, 14, 21,
               99, 94, 72, 40, 10, 13, 59, 67, 54, 40, 95, 42, 5, 43, 64, 55, 34, 52]
    '''

    numbers = [3, 2, 8, 6, 4, 2, 1, 89, 62, 18, 65, 1, 56, 31, 86, 13, 5]
    heap = Heap()

    # numbers = read(filename)
    print("Original Array with Numbers " + str(numbers))
    print("Size of list " + str(len(numbers)))
    print("Sorting Elements using Heap Sort: ")
    print(heap_sort(numbers))




def read(filename):
    numbers = []
    with open(filename, encoding='UTF8') as file:
        for line in file:
            items = line.split(',')
            # print(items)
            numbers.append(items)

    return numbers


def heap_sort(numbers):
    heap = Heap()
    result = []
    for elem in numbers:
        print(heap.insert(elem))

    for i in range(len(heap.heap_array)):
        if heap.is_empty():
            return
        result.append(heap.extract_min())
    print("Sorted Array : ")
    print(result)


main()

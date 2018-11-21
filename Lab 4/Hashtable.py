'''
  Carlos Cabada
  CS 2302 - Fall 2018
  Lab Assignment No.4 : Hashatable.py
  Date: November 11, 2018
  Instructor: Diego Aguirre
  Purpose: Hash table class definition/implemintation.

'''
import pdb


class hashNode:
    def __init__(self, word, embedding, next=None):
        self.word = word
        self.embedding = embedding
        self.next = next


class HashTable:

    def __init__(self, table_size):
        self.table = [None]
        for i in range(table_size):
            self.table.append([])

    def hash(self, k):  # hashes words, using each letter to the power of 26.
        index = 0  # then it adds all of them together. returning the index.
        temp = ord('a')
        for i in range(len(k)):
            base = ord(k[i]) - temp
            index += base * pow(26, (len(k) - 1) - i)
        return index % len(self.table)

    def insert(self, k, embedding):
        pos = self.hash(k)
        list = self.table[pos]
        node = hashNode(k, embedding, list)
        list.append(node)

    def search(self, k):
        pos = self.hash(k)
        for i in self.table:
            t = self.table[pos]
            while t != None:
                if t.item == k:
                    return t

        return None

    def number_comparisons(self):
        total_elem = 0
        num_occupied = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            if temp is not None:
                num_occupied += 1

            for temp in self.table[i]:
                total_elem += 1
                temp = temp.next

        return total_elem / num_occupied

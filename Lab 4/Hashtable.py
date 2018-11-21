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
        self.table = [None]*table_size

    def hash(self, k):  # hashes words, using each letter to the power of 26.
        h = 0  # then it adds all of them together. returning the index.
        temp = ord("a") # lower case letters in the ascii start
        for i in range(len(k)):# at 97, so a == 1, b == 2, c == 3, and so on.
            base = ord(k[i]) - temp
            h = (h ** 26 + base) % len(self.table)
        return h

    def hash1(self, k):
        pos =  k % len(self.table)
        self.table[pos] = k

    def insert(self, k, embedding):

        pos = self.hash(k)
        self.table[pos] = hashNode(k, embedding, self.table[pos])

    def search(self, word):
        pos = self.hash(word)

        for i in self.table:
            t = self.table[pos]
            while t != None:
                if t.word == word:
                    return t

        return None

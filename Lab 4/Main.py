'''
  Carlos Cabada
  CS 2302 - Fall 2018
  Lab Assignment No.4 : Main.py
  Date: November 11, 2018
  Instructor: Diego Aguirre
  Purpose: Implementation of Lab 3 using Hash tables.

'''
from Hashtable import HashTable
import math
import pdb


# Creates hash table and inserts the words and its embedding.
def create_hash(filename,hash):
    with open(filename, encoding='UTF8') as file:
        for line in file:
            items = line.split(' ')
            if items[0].isalpha():
                word = line.split(" ")[0]
                embedding = items[1:51]
                print(word, embedding)
                hash.insert(word, embedding)

    return hash

# counts the node in the hash table.
def count_nodes(table):
    counter = 0
    for item in table.table:
        counter += len(item)
    return str(counter)


# computes the load factor of the hash table.
def load_factor(table):
    return str(count_nodes(table) / len(table.table))


# compares the similarities in the second word file with the ones in the hash table.
def compare(filename, table):
    with open(filename) as support:
        for line in support:
            print(line.split()[0] + " " + line.split()[1] + " " + str(similarity(table, line.split()[0], line.split()[1])))


# converts each word into a integer. It uses the ascii value of letters.
# Then adds each value, returns the integer that would represent the word.
def word_to_int(word):
    output = []
    number = 0
    for character in word:
        number += ord(character) - 96 # lower case letters in the ascii start
    output.append(number)             # at 97, so a == 1, b == 2, c == 3, and so on.
    print(output)


# computes the similarity of words using the cosine distance formula.
def similarity(table, word1, word2):

    wo1 = table.search(word_to_int(word1))
    wo2 = table.search(word_to_int(word2))
    top = 0
    bottom_a = 0
    bottom_b = 0
    for i in range(len(wo1.embedding)):
        top += wo1.embedding[i] + wo2.embedding[i]

    for i in range(len(wo1.embedding)):
        bottom_a += wo1.embedding[i] ** 2

    for i in range(len(wo2.embedding)):
        bottom_b += wo2.embedding[i] ** 2

    bottom_a = math.sqrt(bottom_a)
    bottom_b = math.sqrt(bottom_b)

    return top / (bottom_a * bottom_b)


# converts a string to a float, this is for the embeddings
def string_to_float(holding_array):
    converted = []
    length = (len(holding_array))
    for i in range(length):
        converted.append(float(holding_array[i])) # convert to float
    # print(converted)
    return converted


def avg_num_comparisons(table):
    total = 0
    occupied = 0
    for i in range(len(table.table)):
        temp = table.table[i]
        if temp is not None:
            occupied += 1

        for temp in table.table[i]:
            total += 1
            temp = temp.next

    return total / occupied


def main():
    file = "smaller_file.txt"
    # file = "glove.6B.50d.txt"
    table = HashTable(1000)
    create_hash(file, table)

    # compare("similarities.txt", table)

    print("Average number of Comparisons: " + avg_num_comparisons(table))
    print("Table's Load Factor: " + load_factor(table))


main()

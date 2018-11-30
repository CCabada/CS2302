'''
  Carlos Cabada
  CS 2302 - Fall 2018
  Lab Assignment No.7 : EditDistance.py
  Date: November 30, 2018
  Instructor: Diego Aguirre
  Purpose: Implementation of Edit Distance.
'''


def edit_distance(string1, string2, len1, len2):
    d = [[0 for x in range(len2 + 1)] for x in range(len1 + 1)]

    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i# deletion
            elif string1[i-1] == string2[j-1]:
                d[i][j] = d[i-1][j-1]

            else:
                d[i][j] = 1 + min(d[i][j-1], d[i-1][j],d[i-1][j-1])
    return d[len1][len2]




string1 = "lost"
string2 = "money"


print("Edit Distance of " + string1 + " and " + string2 + " is " + str(edit_distance(string1, string2, len(string1), len(string2))))

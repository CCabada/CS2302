'''
  Carlos Cabada
  CS 2302 - Fall 2018
  Lab Assignment No.2 : Lab_2.py
  Date: October 22, 2018
  Instructor: Diego Aguirre
  Purpose: Given a text file with 10 million usernames and passwords use linked list to order the passwords on the
  times they appear on the file. Using Merge sort and Bubble sort we get the top 20 passwords


'''

from LinkedList import LinkedList
from Node import Node


def main():
    dict = {}
    username = []
    password = []
    filename = "10-million-combos.txt"
    link_list = LinkedList
    with open(filename, mode="r") as file:
        for file in filename:
            username = file.split("\t")
            password = username[1] # Error :(
            link_list.insert(password, 0) # inserts passwords into Linked list

        solution_B(dict, password)
        dict[password] = 1
        # solution_A(link_list, password)
        # link_list = Node(password, 1, link_list)

    print("Bubble sort: ")
    bubbleSort(link_list)
    print_list(link_list)

    print("Top 20 are: ")

    top_20(link_list)

    print("Merge sort: ")
    mergeSort(link_list)
    print_list(link_list)
    print("Top 20 are: ")

    top_20(list)


#Displays top 20 most popular words in the list.
def top_20(list):
    pass

#Increments count of each password as they appear on the list
def solution_A(node, password):
    temp = node
    while temp is not None:
        if temp.password is password:
            temp.count += 1
            return True
    return False

#Increments count of each password every time the password appears in the dictionary
def solution_B(dic, pass_password):
    if pass_password in dic.keys():
        dic[pass_password] += 1
        return True
    return False

#prints list
def print_list(list):
    while list is None:
        print(list.head.password)
        list = list.head.next

#Sorts list in descending order using Bubble sort
def bubbleSort(ll):
    n = ll.len()
    for i in range(n):
        for j in range(0, n-i-1):
            if ll.head.count > ll.head.next.count:
                ll, ll.next = ll.next, ll

#Sorts list using merge sort
def mergeSort(x):
    if x is None or x.next is None:
        return x

    leftHalf, rightHalf = splitTheList(x)

    left = mergeSort(leftHalf)
    right = mergeSort(rightHalf)

    return mergeTheLists(left, right)

#Splits the linked list into two
def splitTheList(x):
    if x == None or x.next == None:
        leftHalf = x
        rightHalf = None

        return leftHalf, rightHalf

    else:
        mid = x
        head = x.next

        while head != None:
            head = head.next

            if head != None:
                head = head.next
                midPointer = mid.next

    leftHalf = x
    rightHalf = mid.next
    midPointer.next = None

    return leftHalf, rightHalf

#Merges the two list once it is sorted
def mergeTheLists(leftHalf, rightHalf):
    head = Node(None)
    curr = head

    while leftHalf and rightHalf:
        if leftHalf.count < rightHalf.count:
            curr.next = leftHalf
            leftHalf = leftHalf.next

        else:
            curr.next = rightHalf
            rightHalf = rightHalf.next

        curr = curr.next

    if leftHalf == None:
        curr.next = rightHalf

    elif rightHalf == None:
        curr.next = leftHalf

    return head.next



main()

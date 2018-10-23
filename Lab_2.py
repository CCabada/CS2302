'''
  Carlos Cabada
  CS 2302 - Fall 2018
  Lab Assignment No.1 : Lab1.py
  Date: September 18, 2018
  Instructor: Diego Aguirre
  Purpose: Given a text file containing user, salt values and hashed passwords, generate the equivalent password to each user.

'''


from Node import Node


def main():
    dict = {}
    filename = "10-million-combos.txt"

    with open(filename, mode="r") as file:
        for file in filename:
            username = file.split("\t")
            password = username[1] # Error :(

            if not solution_B(dict, password):
                dict[password] = 1
            if not solution_A(link_list, password):
                link_list = Node(password, 1, link_list)
        print(password)
    print("Bubble sort: ")
    bubbleSort(link_list)
    print_list(link_list)


    print("Merge sort: ")
    mergeSort(link_list)
    print_list(link_list)


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


from Node import Node


class LinkedList:
    count = -1
    password = ""

    def __init__(self, head=None):
        self.head = head

    def insert(self, passwords, count):
        new_node = Node(passwords, count)
        new_node.next = self.head
        self.head = new_node

    def len(self):
        self.curr = self.head
        total = 0
        while self.curr.next != None:
            total += 1
            self.curr = self.curr.next
        return total

    def get(self, index):
        if index >= self.len():
            print("Error")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.password
            cur_idx += 1


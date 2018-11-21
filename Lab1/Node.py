class Node(object):
    password = ""

    count = -1
    next = None

    def __init__(self, password, count):
        self.password = password

        self.count = count
        self.next = next



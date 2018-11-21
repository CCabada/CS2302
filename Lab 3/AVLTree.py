class AVLNode:
    
    def __init__(self, item, embedding=None):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
        self.embedding = embedding

    def get_balance(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        return left_height - right_height
    
    def update_height(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        self.height = max(left_height, right_height) + 1

    def set_child(self, which_child, child):
        if which_child != "left" and which_child != "right":
            return False

        if which_child == "left":
            self.left = child
        else:
            self.right = child

        if child is not None:
            child.parent = self

        self.update_height()
        return True

    def replace_child(self, curr_child, new_child):
        if self.left is curr_child:
            return self.set_child("left", new_child)
        elif self.right is curr_child:
            return self.set_child("right", new_child)

        return False


class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, AVLNode):
        if self.root is None:
            self.root = AVLNode
            AVLNode.parent = None

        else:
            curr_AVLNode = self.root
            while curr_AVLNode is not None:
                if AVLNode.item < curr_AVLNode.item:
                    if curr_AVLNode.left is None:
                        curr_AVLNode.left = AVLNode
                        AVLNode.parent = curr_AVLNode
                        curr_AVLNode = None
                    else:
                        curr_AVLNode = curr_AVLNode.left
                else:
                    if curr_AVLNode.right is None:
                        curr_AVLNode.right = AVLNode
                        AVLNode.parent = curr_AVLNode
                        curr_AVLNode = None
                    else:
                        curr_AVLNode = curr_AVLNode.right

            AVLNode = AVLNode.parent
            while AVLNode is not None:
                self.rebalance(AVLNode)
                AVLNode = AVLNode.parent


    def find(self,item):
        curr_node = self.root
        while curr_node is not None:

            if curr_node.item == item:
                return curr_node
            elif curr_node.item < item:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left


    def remove_item(self, item):
        node = self.search(item)
        if node is None:
            return False
        else:
            return self.remove_node(node)

    def rebalance(self, AVLNode):
        AVLNode.update_height()
        if AVLNode.get_balance() == -2:
            if AVLNode.right.get_balance() == 1:
                self.rotate_right(AVLNode.right)
            return self.rotate_left(AVLNode)

        elif AVLNode.get_balance() == 2:
            if AVLNode.left.get_balance() == -1:
                self.rotate_left(AVLNode.left)
            return self.rotate_right(AVLNode)
        return AVLNode

    def rotate_right(self, AVLNode):
        left_right_child = AVLNode.left.right

        if AVLNode.parent != None:
            AVLNode.parent.replace_child(AVLNode, AVLNode.left)
        else:
            self.root = AVLNode.left
            self.root.parent = None
        AVLNode.left.set_child("right", AVLNode)
        AVLNode.set_child("left", left_right_child)

    def rotate_left(self, AVLNode):
        right_left_child = AVLNode.right.left
        if AVLNode.parent != None:
            AVLNode.parent.replace_child(AVLNode, AVLNode.right)
        else:
            self.root = AVLNode.right
            self.root.parent = None
        AVLNode.right.set_child("left", AVLNode)
        AVLNode.set_child("right", right_left_child)

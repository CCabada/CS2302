# RBTRBNode class - represents a RBNode in a red-black tree
class RBNode:
    def __init__(self, item, parent, embedding=None, is_red=False, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent
        self.embedding = embedding

        if is_red:
            self.color = "red"
        else:
            self.color = "black"

    def are_both_children_black(self):
        if self.left is not None and self.left.is_red():
            return False
        if self.right is not None and self.right.is_red():
            return False
        return True

    def count(self):
        count = 1
        if self.left is not None:
            count = count + self.left.count()
        if self.right is not None:
            count = count + self.right.count()
        return count

    def get_grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent


    def get_predecessor(self):
        RBNode = self.left
        while RBNode.right is not None:
            RBNode = RBNode.right
        return RBNode

    def get_sibling(self):
        if self.parent is not None:
            if self is self.parent.left:
                return self.parent.right
            return self.parent.left
        return None

    def get_uncle(self):
        grandparent = self.get_grandparent()
        if grandparent is None:
            return None
        if grandparent.left is self.parent:
            return grandparent.right
        return grandparent.left

    def is_black(self):
        return self.color == "black"

    def is_red(self):
        return self.color == "red"

    def replace_child(self, curr_child, new_child):
        if self.left is curr_child:
            return self.set_child("left", new_child)
        elif self.right is curr_child:
            return self.set_child("right", new_child)
        return False

    def set_child(self, which_child, child):
        if which_child != "left" and which_child != "right":
            return False

        if which_child == "left":
            self.left = child
        else:
            self.right = child

        if child is not None:
            child.parent = self

        return True


class Red_Black_Tree:
    def __init__(self):
        self.root = None

    def __len__(self):
        if self.root is None:
            return 0
        return self.root.count()

    def insert(self, item):
        new_RBNode = RBNode(item, None, None, True, None, None)
        self.insert_RBNode(new_RBNode)

    def insert_RBNode(self, RBNode):
        import pdb
        if self.root is None:
            self.root = RBNode
        else:
            curr_RBNode = self.root
            while curr_RBNode is not None:

                if RBNode.item.item < curr_RBNode.item.item:
                    if curr_RBNode.left is None:
                        curr_RBNode.set_child("left", RBNode)
                        break
                    else:
                        curr_RBNode = curr_RBNode.left
                else:
                    if curr_RBNode.right is None:
                        curr_RBNode.set_child("right", RBNode)
                        break
                    else:
                        curr_RBNode = curr_RBNode.right

        RBNode.color = "red"


        self.insertion_balance(RBNode)

    def insertion_balance(self, RBNode):
        if RBNode.parent is None:
            RBNode.color = "black"
            return

        if RBNode.parent.is_black():
            return

        parent = RBNode.parent
        grandparent = RBNode.get_grandparent()
        uncle = RBNode.get_uncle()

        if uncle is not None and uncle.is_red():
            parent.color = uncle.color = "black"
            grandparent.color = "red"
            self.insertion_balance(grandparent)
            return

        if RBNode is parent.right and parent is grandparent.left:
            self.rotate_left(parent)
            RBNode = parent
            parent = RBNode.parent

        elif RBNode is parent.left and parent is grandparent.right:
            self.rotate_right(parent)
            RBNode = parent
            parent = RBNode.parent

        parent.color = "black"
        grandparent.color = "red"

        if RBNode is parent.left:
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

    def rotate_left(self, RBNode):
        right_left_child = RBNode.right.left
        if RBNode.parent is not None:
            RBNode.parent.replace_child(RBNode, RBNode.right)
        else:  # RBNode is root
            self.root = RBNode.right
            self.root.parent = None
        RBNode.right.set_child("left", RBNode)
        RBNode.set_child("right", right_left_child)

    def rotate_right(self, RBNode):
        left_right_child = RBNode.left.right
        if RBNode.parent is not None:
            RBNode.parent.replace_child(RBNode, RBNode.left)
        else:  # RBNode is root
            self.root = RBNode.left
            self.root.parent = None
        RBNode.left.set_child("right", RBNode)
        RBNode.set_child("left", left_right_child)

    def _bst_remove(self, item):
        RBNode = self.search(item)
        self._bst_remove_RBNode(RBNode)

    def _bst_remove_RBNode(self, RBNode):
        if RBNode is None:
            return

        if RBNode.left is not None and RBNode.right is not None:

            successor_RBNode = RBNode.right
            while successor_RBNode.left is not None:
                successor_RBNode = successor_RBNode.left

            successor_item = successor_RBNode.item

            self._bst_remove_RBNode(successor_RBNode)

            RBNode.item = successor_item

        elif RBNode is self.root:
            if RBNode.left is not None:
                self.root = RBNode.left
            else:
                self.root = RBNode.right

            if self.root is not None:
                self.root.parent = None

        elif RBNode.left is not None:
            RBNode.parent.replace_child(RBNode, RBNode.left)

        else:
            RBNode.parent.replace_child(RBNode, RBNode.right)

    def is_none_or_black(self, RBNode):
        if RBNode is None:
            return True
        return RBNode.is_black()

    def is_not_none_and_red(self, RBNode):
        if RBNode is None:
            return False
        return RBNode.is_red()

    def prepare_for_removal(self, RBNode):
        if self.case1(RBNode):
            return

        sibling = RBNode.get_sibling()
        if self.case2(RBNode, sibling):
            sibling = RBNode.get_sibling()
        if self.case3(RBNode, sibling):
            return
        if self.case4(RBNode, sibling):
            return
        if self.case5(RBNode, sibling):
            sibling = RBNode.get_sibling()
        if self.case6(RBNode, sibling):
            sibling = RBNode.get_sibling()

        sibling.color = RBNode.parent.color
        RBNode.parent.color = "black"
        if RBNode is RBNode.parent.left:
            sibling.right.color = "black"
            self.rotate_left(RBNode.parent)
        else:
            sibling.left.color = "black"
            self.rotate_right(RBNode.parent)

    def remove(self, item):
        RBNode = self.search(item)
        if RBNode is not None:
            self.remove_RBNode(RBNode)
            return True
        return False

    def remove_RBNode(self, RBNode):
        if RBNode.left is not None and RBNode.right is not None:
            predecessor_RBNode = RBNode.get_predecessor()
            predecessor_item = predecessor_RBNode.item
            self.remove_RBNode(predecessor_RBNode)
            RBNode.item = predecessor_item
            return

        if RBNode.is_black():
            self.prepare_for_removal(RBNode)
        self._bst_remove(RBNode.item)

        if self.root is not None and self.root.is_red():
            self.root.color = "black"

    def find(self, item):
        curr_RBnode = self.root
        while curr_RBnode is not None:

            if curr_RBnode.item == item:
                return curr_RBnode

            elif item < curr_RBnode.item:
                curr_RBnode = curr_RBnode.left

            else:
                curr_RBnode = curr_RBnode.right

        return


# Prepare-for-removal-algorithm case code
    
    def case1(self, RBNode):
        if RBNode.is_red() or RBNode.parent is None:
            return True


    def case2(self, RBNode, sibling):
        if sibling.is_red():
            RBNode.parent.color = "red"
            sibling.color = "black"
            if RBNode is RBNode.parent.left:
                self.rotate_left(RBNode.parent)
            else:
                self.rotate_right(RBNode.parent)
            return True


    def case3(self, RBNode, sibling):
        if RBNode.parent.is_black() and sibling.are_both_children_black():
            sibling.color = "red"
            self.prepare_for_removal(RBNode.parent)
            return True


    def case4(self, RBNode, sibling):
        if RBNode.parent.is_red() and sibling.are_both_children_black():
            RBNode.parent.color = "black"
            sibling.color = "red"
            return True


    def case5(self, RBNode, sibling):
        if self.is_not_none_and_red(sibling.left):
            if self.is_none_or_black(sibling.right):
                if RBNode is RBNode.parent.left:
                    sibling.color = "red"
                    sibling.left.color = "black"
                    self.rotate_right(sibling)
                    return True


    def case6(self, RBNode, sibling):
        if self.is_none_or_black(sibling.left):
            if self.is_not_none_and_red(sibling.right):
                if RBNode is RBNode.parent.right:
                    sibling.color = "red"
                    sibling.right.color = "black"
                    self.rotate_left(sibling)
                    return True

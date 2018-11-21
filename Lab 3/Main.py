import AVLTree
import Red_Black_Tree
import pdb
import math


def main():
    user = int(input("What type of binary search tree do you want to use? \n 1: AVL Tree \n 2: Red-Black Tree \n"))

    if user == 1:
        print("Creating AVL tree")
        avl = create_AVL_Tree("glove.6B.50d.txt", AVLTree)
        # avl = create_AVL_Tree("smaller_file.txt", AVLTree)
        print("There are : ", count_nodes(avl.root), " nodes in this AVL Tree. ")
        print("The height of this tree is :", height(avl.root), ".")

        d = int(input("What d do you want to look at?"))
        print("Creating file with the words at the d: ", d)
        with open("words_at_d.txt", "w", encoding='UTF8') as file:
            words_at_d(avl, d, file)

        print("Creating file with the words in the tree: ")
        with open("words_in_tree.txt", "w", encoding='UTF8') as words_in_tree_file:
            words_in_tree(avl, words_in_tree_file)

        print("Comparing words: ")
        compare("similarities.txt", avl)



    elif user == 2:
        print("Creating Red-Black tree")
        # red_black = create_Red_Black_Tree("smaller_file.txt", Red_Black_Tree)
        red_black = create_Red_Black_Tree("glove.6B.50d.txt", Red_Black_Tree)

        print("There are : ", count_nodes(red_black.root), " nodes in this Red-Black Tree. ")
        print("The height of this tree is :", height(red_black.root), ".")


        d = int(input("What d do you want to look at?"))
        print("Creating file with the words at the d: ", d)
        with open("words_at_d.txt", "w", encoding='UTF8') as file:
            words_at_d(red_black, d, file)

        print("Creating file with the words in the tree: ")
        with open("words_in_tree.txt", "w", encoding='UTF8') as words_in_tree_file:
            words_in_tree(red_black, words_in_tree_file)

        print("Comparing words: ")
        compare("similarities.txt", red_black)


# Puts together the AVL tree
def create_AVL_Tree(filename, type_of_tree):

    tree = type_of_tree.AVLTree()
    with open(filename, encoding='UTF8') as dictionary:
        for line in dictionary:
            items = line.split()
            if items.pop(0).isalpha():
                items = string_to_float(items[1:51])
                tree.insert(type_of_tree.AVLNode(items.pop(0), items))

    return tree


# Puts together the Red-Black tree
def create_Red_Black_Tree(filename, type_of_tree):
    tree = type_of_tree.Red_Black_Tree()

    with open(filename, encoding='UTF8') as file:
        for line in file:
            items = line.split()
            if items.pop(0).isalpha():
                items = string_to_float(items[1:51])
                tree.insert(type_of_tree.RBNode(items.pop(0), None, items))
    return tree


# Finds the height of the Tree
def height(root):
    if root is None:
        return -1
    hr = height(root.right)
    hl = height(root.left)
    if hl < hr:
        return 1 + hl
    return 1 + hr

# Counts the nodes
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.right) + count_nodes(root.left)


def words_in_tree(root, file):
    if root is None:
        return None

    file.write(root.item, " ")
    words_in_tree(root.right)
    words_in_tree(root.left)


def words_at_d(root, new_file, d):

    if root is None:
        return
    if d < 0:
        new_file.write(root.key + "\n")
        return
    else:
        words_at_d(root.left, new_file, d - 1)
        words_at_d(root.right, new_file, d - 1)


def print_tree(root):
    pdb.set_trace()
    if root is not None:
        if root.right is not None and root.left is not None:
            print(root.item, " ")

        print_tree(root.right)
        print_tree(root.left)


#converts a string to a float, this is for the embeddings
def string_to_float(holding_array):
    converted = []
    length = (len(holding_array))
    for i in range(length):
        converted.append(float(holding_array[i])) # convert to float
    # print(converted)
    return converted



# compares the similarities of the words in the second file
def compare(filename, T):
    with open(filename) as support:
        for line in support:
            print(line.split()[0] + " " + line.split()[1] + " " + str(similarity(T, line.split()[0], line.split()[1])))



# Computes the similarities by using the formula provided
def similarity(tree, word1, word2):
    wo1 = tree.find(word1)
    wo2 = tree.find(word2)
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




main()

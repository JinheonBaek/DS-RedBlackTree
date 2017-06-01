from Node import Node

class RBT:
    def __init__(self):
        self.root = None

    def insert(self, tree, n):
        # init
        y = None
        x = self.root

        # search inserting place
        while x is not None:
            y = x
            if n.val < x.val:
                x = x.left
            else:
                x = x.right

        # insert new node
        n.parent = y
        if y is None:
            self.root = n
        elif n.val < y.val:
            y.left = n
        else:
            y.right = n

        # fix up RBT
        self.RBT_Insert_Fixup(self, n)

    def RBT_Insert_Fixup(self, tree, n):
        while n.parent is not None and n.parent.parent is not None and n.parent.color is 'RED':
            if n.parent == n.parent.parent.left:
                y = n.parent.parent.right
                if y is not None and y.color == "RED":
                    n.parent.color = "BLACK"
                    y.color = "BLACK"
                    n.parent.parent.color = "RED"
                    n = n.parent.parent
                else:
                    if n == n.parent.right:
                        n = n.parent
                        self.Left_Rotate(tree, n)
                    n.parent.color = "BLACK"
                    n.parent.parent.color = "RED"
                    self.Right_Rotate(tree, n.parent.parent)
            else:
                y = n.parent.parent.left
                if y is not None and y.color == "RED":
                    n.parent.color = "BLACK"
                    y.color = "BLACK"
                    n.parent.parent.color = "RED"
                    n = n.parent.parent
                else:
                    if n == n.parent.left:
                        n = n.parent
                        self.Right_Rotate(tree, n)
                    n.parent.color = "BLACK"
                    n.parent.parent.color = "RED"
                    self.Left_Rotate(tree, n.parent.parent)
        self.root.color = "BLACK"
        self.print(self.root, 0)
        print("")

    def Left_Rotate(self, tree, x):
        # set y
        y = x.right

        # insert subtree of y into x
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

       # link x's parent to y
        y.parent = x.parent
        if x.parent is None:
            tree.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        # put x on y's left
        y.left = x
        x.parent = y

    def Right_Rotate(self, tree, x):
        # set y
        y = x.left

        # insert subtree of y into x
        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        # link x's parent to y
        y.parent = x.parent
        if x.parent is None:
            tree.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        # put x on y's right
        y.right = x
        x.parent = y

    def print(self, tree, level):
        if tree.right is not None:
            self.print(tree.right, level + 1)
        for i in range(level):
            print('   ', end='')
        print(tree.val, tree.color)
        if tree.left is not None:
            self.print(tree.left, level + 1)

from Node import Node
from Tree import RBT

def getFileData(name = "input.txt"):
    data = []

    f = open(name, 'r')
    lines = f.readlines()

    for line in lines:
        data.append(int(line.strip("\n")))

    f.close()

    return data

def main():
    data = getFileData()
    rbt = RBT()

    for i in data:
        if i > 0:
            rbt.insert(rbt.root, Node(i))
        elif i < 0:
            rbt.delete(rbt.root, -i)
        else:
            break

    print("Number of Total Node")
    rbt.printNodeCount(rbt.root)

    print("Number of Black Node")
    rbt.printBlackNodeCount(rbt.root)

    print("Black Height")
    rbt.printBlackHeight(rbt.root)

    print("Inorder Traversal")
    rbt.inOrderTraversal(rbt.root)

main()
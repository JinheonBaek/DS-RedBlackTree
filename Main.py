import os
from Node import Node
from Tree import RBT

def search():
    filenames = os.listdir('./input/')
    filename_lst = []

    for filename in filenames:
        filename_lst.append(filename)

    return filename_lst

def getFileData(names):
    data = []
    _dir = './input/'

    for name in names:
        f = open(_dir + name, 'r')
        lines = f.readlines()
        tmp_data = []

        for line in lines:
            tmp_data.append(int(line.strip("\n")))

        data.append(tmp_data)
        f.close()

    return data

def main():
    #init
    names = search()
    datas = getFileData(names)
    sequence = 0

    for data in datas:
        rbt = RBT()

        for i in data:
            if i > 0:
                rbt.insert(rbt.root, Node(i))
            elif i < 0:
                rbt.delete(rbt.root, -i)
            else:
                break

        print("\nFile Name: " + names[sequence])

        print("Number of Total Node")
        rbt.printNodeCount(rbt.root)

        print("Number of Insert Node")
        rbt.printInsertNode(rbt.root)

        print("Number of Delete Node")
        rbt.printDeleteNode(rbt.root)

        print("Number of Miss Node")
        rbt.printMissNode(rbt.root)

        print("Number of Black Node")
        rbt.printBlackNodeCount(rbt.root)

        print("Black Height")
        rbt.printBlackHeight(rbt.root)

        print("Inorder Traversal")
        rbt.inOrderTraversal(rbt.root)

        sequence += 1

main()
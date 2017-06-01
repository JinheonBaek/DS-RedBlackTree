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
            #rbt.delete(rbt.root, Node(i))
            continue
        else:
            break

main()
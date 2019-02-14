from Node import Node
from Tree import RBT

def readFileData(name):
    data = []
    _dir = './bin/'

    f = open(_dir + name, 'r')
    lines = f.readlines()

    for line in lines:
        data.append(int(line.strip("\n")))

    f.close()

    return data

def writeFileData(name, datas):
    _dir = "./bin/"

    f = open(_dir + name, 'w')

    for i in range(len(datas['predecessor'])):
        data = str(datas['predecessor'][i]) + " / " + str(datas['searchData'][i]) + " / " + str(datas['successor'][i]) + "\n"
        f.write(data)

    f.close()

def main():
    #init
    inputDatas = readFileData("input.txt")
    searchDatas = readFileData("search.txt")
    sequence = 0

    rbt = RBT()

    #Input
    for i in inputDatas:
        if i > 0:
            rbt.insert(rbt.root, Node(i))
        elif i < 0:
            rbt.delete(rbt.root, -i)
        else:
            break

    rbt.print(rbt.root, 0)

    #Search
    writeData = {'predecessor' : [], 'searchData' : [], 'successor' : []}
    for i in searchDatas:

        if i == 0:
            break

        searchData = rbt.search(rbt.root, i)
        predecessor = rbt.findPredecessor(searchData)
        successor = rbt.findSuccessor(searchData)

        writeData['predecessor'].append(predecessor.val if predecessor is not None else "NIL")
        writeData['searchData'].append(searchData.val if searchData.val is not None else "NIL")
        writeData['successor'].append(successor.val if successor is not None else "NIL")

    writeFileData("output.txt", writeData)

main()

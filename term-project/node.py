class Node:
    def __init__(self, newval):
        self.val = newval
        self.left = NullNode(self)
        self.right = NullNode(self)
        self.parent = None
        self.color = 'RED'

# 값이 None이면 NullNode 임을 보여준다 - leafNode
class NullNode:
    def __init__(self, parent):
        self.val = None
        self.left = None
        self.right = None
        self.parent = parent
        self.color = "BLACK"

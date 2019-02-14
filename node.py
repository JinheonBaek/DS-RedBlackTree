class Node:
    def __init__(self, newval):
        self.val = newval
        self.left = NullNode()
        self.right = NullNode()
        self.parent = None
        self.color = 'RED'

# 값이 None이면 NullNode 임을 보여준다 - leafNode
class NullNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.parent = None
        self.color = "BLACK"
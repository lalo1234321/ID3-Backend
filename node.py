class Node:
    def __init__(self, path="", data="", nodes=[], parent=None, depth = 1, uniqueKey = 0):
        self.path = path
        self.data = data
        self.nodes = []
        self.parent = parent
        self.depth = depth
        self.uniqueKey = 0

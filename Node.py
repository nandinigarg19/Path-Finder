class Node:
    def __init__(self):
        gridX = 0
        gridY = 0
        walkable = False
        gcost = 0
        hcost = 0
        parent = None

    def createNode(self, gx, gy, walkable):
        self.gridX = gx
        self.gridY = gy
        self.walkable = walkable
        self.parent = None
        self.gcost = 0
        self.hcost = 0

    @property
    def fcost(self):
        return self.gcost + self.hcost

    
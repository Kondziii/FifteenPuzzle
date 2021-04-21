import copy

class Node:
    def __init__(self, state, parent, direction, depth):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth

    def getStateString(self):
        state = ''
        for row in self.state:
            for number in row:
                state += str(number)
        return state

    def isCorrect(self, destState):
        return self.state == destState

    def getZeroPosition(self):
        for w in range(len(self.state)):
            for k in range(len(self.state[0])):
                if self.state[w][k] == 0:
                    return [w, k]

    def getChildren(self, order):
        children = []
        zeroPosition = self.getZeroPosition()
        for o in order:
            child = None
            if o == 'L':
                child = self.getLeftChild(o, zeroPosition)
            elif o == 'R':
                child = self.getRightChild(o, zeroPosition)
            elif o == 'U':
                child = self.getTopChild(o, zeroPosition)
            elif o == 'D':
                child = self.getBottomChild(o, zeroPosition)
            if child:
                children.append(child)
        return children

    def getBottomChild(self, o, zeroPosition):
        bottomChild = None
        if zeroPosition[0] + 1 >= len(self.state):
            return bottomChild
        childState = copy.deepcopy(self.state)
        tmp = childState[zeroPosition[0] + 1][zeroPosition[1]]
        childState[zeroPosition[0] + 1][zeroPosition[1]] = 0
        childState[zeroPosition[0]][zeroPosition[1]] = tmp
        return Node(childState, self, o, self.depth + 1)

    def getTopChild(self, o, zeroPosition):
        topChild = None
        if zeroPosition[0] - 1 < 0:
            return topChild
        childState = copy.deepcopy(self.state)
        tmp = childState[zeroPosition[0] - 1][zeroPosition[1]]
        childState[zeroPosition[0] - 1][zeroPosition[1]] = 0
        childState[zeroPosition[0]][zeroPosition[1]] = tmp
        return Node(childState, self, o, self.depth + 1)

    def getRightChild(self, o, zeroPosition):
        rightChild = None
        if zeroPosition[1] + 1 >= len(self.state[0]):
            return rightChild
        childState = copy.deepcopy(self.state)
        tmp = childState[zeroPosition[0]][zeroPosition[1] + 1]
        childState[zeroPosition[0]][zeroPosition[1] + 1] = 0
        childState[zeroPosition[0]][zeroPosition[1]] = tmp
        return Node(childState, self, o, self.depth + 1)

    def getLeftChild(self, o, zeroPosition):
        leftChild = None
        if zeroPosition[1] - 1 < 0:
            return leftChild
        childState = copy.deepcopy(self.state)
        tmp = childState[zeroPosition[0]][zeroPosition[1] - 1]
        childState[zeroPosition[0]][zeroPosition[1] - 1] = 0
        childState[zeroPosition[0]][zeroPosition[1]] = tmp
        return Node(childState, self, o, self.depth + 1)


















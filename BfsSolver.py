from puzzle.Node import Node
from puzzle.Puzzle import Puzzle
import time


class BfsSolver:
    def __init__(self):
        self.visitedNodesAmount = None
        self.maxDepth = None
        self.statesProcessed = []
        self.nodes = []

    def _reset(self):
        self.visitedNodesAmount = 0
        self.maxDepth = 0
        self.statesProcessed = []
        self.nodes = []

    def _getSolutionPath(self, node):
        solutionMoves = node.direction
        while node.parent:
            if node.parent.direction:
                solutionMoves += str(node.parent.direction)
            node = node.parent
        return len(solutionMoves), solutionMoves

    def _writeStatsToFile(self, stats, statsFile):
        with open(statsFile, 'w') as file:
            for s in stats:
                file.write(str(s))
                file.write('\n')

    def _writeSolutionToFile(self, solution, solutionFile):
        with open(solutionFile, 'w') as file:
            if solution:
                for value in solution:
                    file.write(str(value))
                    file.write('\n')
            else:
                file.write('-1')

    def _bfs(self, puzzle, order):
        self.nodes.append(Node(puzzle.currState, None, None, 0))
        while self.nodes:
            node = self.nodes.pop(0)
            self.statesProcessed.append(node.getStateString())
            if node.isCorrect(puzzle.destState):
                return node
            children = node.getChildren(order)
            for child in children:
                self.visitedNodesAmount += 1
                if child.getStateString() not in self.statesProcessed:
                    self.nodes.append(child)
                if child.depth > self.maxDepth:
                    self.maxDepth = child.depth
                if child.isCorrect(puzzle.destState):
                    return child

    def run(self, puzzle, order, solutionFile=None, statsFile=None):
        self._reset()
        start = time.time()
        solutionNode = self._bfs(puzzle, order)
        end = time.time()

        if solutionNode:
            solution = self._getSolutionPath(solutionNode)
            self._writeSolutionToFile(solution, solutionFile)
            if statsFile:
                self._writeStatsToFile([solution[0], self.visitedNodesAmount, len(self.statesProcessed),
                                        self.maxDepth, round(end - start, 3)], statsFile)


input = []
w, k = 0, 0
with open('input.txt', 'r') as file:
    w, k = [int(x) for x in next(file).split()]
    for line in file:
        input.append([int(x) for x in line.split()])

puzzle = Puzzle(input)
BfsSolver().run(puzzle, 'LRDU', 'solution.txt', 'stats.txt')


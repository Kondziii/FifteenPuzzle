class Puzzle:
    def __init__(self, currState, destState=None):
        if self._isValid(currState) is False or (self._isValid(destState) is False and destState is not None):
            raise ValueError("Incorrect states")
        self.currState = currState
        self.destState = destState
        if not self.destState:
            self._generateDeafultDestState()

    def _isValid(self, state):
        numbers = set()
        if state is None:
            return False
        k = len(state[0])
        for row in state:
            if len(row) != k:
                return False
            for number in row:
                numbers.add(number)
                if not isinstance(number, int):
                    return False
        for i in range(len(state) * len(state[0])):
            if i not in numbers:
                return False
        return True

    def _generateDeafultDestState(self):
        self.destState = []
        w = len(self.currState)
        k = len(self.currState[0])
        state = list(range(1, w*k))
        state.append(0)
        for i in range(w):
            row = []
            for j in range(k):
                row.append(state[i*w + j])
            self.destState.append(row)






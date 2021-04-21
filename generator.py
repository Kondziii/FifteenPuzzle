import numpy as np
import random
import copy

def move(state, direction):
    new_state = copy.deepcopy(state)
    zero_pos = [[i, row.index(0)] for i, row in enumerate(new_state) if 0 in row][0]
    if (direction == 'R'):
        new_state[zero_pos[0]][zero_pos[1]] = new_state[zero_pos[0]][zero_pos[1]+1]
        new_state[zero_pos[0]][zero_pos[1]+1] = 0
    elif (direction == 'L'):
        new_state[zero_pos[0]][zero_pos[1]] = new_state[zero_pos[0]][zero_pos[1]-1]
        new_state[zero_pos[0]][zero_pos[1]-1] = 0
    elif (direction == 'U'):
        new_state[zero_pos[0]][zero_pos[1]] = new_state[zero_pos[0]-1][zero_pos[1]]
        new_state[zero_pos[0]-1][zero_pos[1]] = 0
    elif (direction == 'D'):
        new_state[zero_pos[0]][zero_pos[1]] = new_state[zero_pos[0]+1][zero_pos[1]]
        new_state[zero_pos[0]+1][zero_pos[1]] = 0
    return new_state

def new_state(col, row, move_min=10, move_max=10):

    state = list(range(col*row))
    state.append(state.pop(0))
    state = [state[i*col:i*col+col] for i in range(row)]

    move_amount = 0
    if (move_min > move_max):
        i = move_min
        move_min = move_max
        move_max = i
    if (move_min == move_max): move_amount = move_max
    else: move_amount = np.random.randint(move_min, move_max)

    last_dir = ''
    for i in range (move_amount):
        zero_pos = [[i, row.index(0)] for i, row in enumerate(state) if 0 in row][0]
        directions = []
        if (last_dir != 'L' and zero_pos[1] < col-1): directions.append('R')
        if (last_dir != 'R' and zero_pos[1] > 0): directions.append('L')
        if (last_dir != 'D' and zero_pos[0] > 0): directions.append('U')
        if (last_dir != 'U' and zero_pos[0] < row-1): directions.append('D')
        direction = random.choice(directions)
        last_dir = direction
        state = move(state, direction)

    return state

col = 4
row = 4
with open('input.txt', 'w') as f:
    f.write(str(row)+' '+str(col)+'\n')
    state = new_state(col, row, 10, 10)
    for row in state:
        line = ''
        for i, cell in enumerate(row):
            if (i+1 == col): line += str(cell) + '\n'
            else: line += str(cell) + ' '
        f.write(line)
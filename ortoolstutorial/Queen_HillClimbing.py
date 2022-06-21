import random
from copy import deepcopy, copy
import math 
random.seed()

class QueenProblem:
    queens = []
    queens_num = 8

    def __init__(self, n):
        self.queens_num = n

    def getState(self):
        return self.queens

    def isGoal(self):
        return self.heuristic() == 0

    def heuristic(self):
        conflicts = 0
        for (x, y) in self.queens:
            hasConflict = False
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if (di != 0 or dj != 0) and not hasConflict:
                        i, j = x, y
                        condition = self.getCondition(di, dj, i, j)
                        while condition:
                            i += di
                            j += dj
                            if (i, j) in self.queens and (i, j) != (x, y):
                                conflicts += 1
                                hasConflict = True
                                break
                            condition = self.getCondition(di, dj, i, j)
        return conflicts
    
    # used in heuristic function
    def getCondition(self, di, dj, i, j):
        if (di, dj) == (-1, -1): return i != 0 and j != 0
        elif (di, dj) == (-1, 0): return i != 0
        elif (di, dj) == (-1, 1): return i != 0 and j != self.queens_num - 1
        elif (di, dj) == (0, -1): return j != 0
        elif (di, dj) == (0, 1): return j != self.queens_num - 1
        elif (di, dj) == (1, -1): return i != self.queens_num - 1 and j != 0
        elif (di, dj) == (1, 0): return i != self.queens_num - 1
        elif (di, dj) == (1, 1): return i != self.queens_num - 1 and j != self.queens_num - 1
    
    def getSuccessors(self):
        successorsForEachQueens = []

        for queen in self.queens:
            successors = []
            for i in range(queen[0] - 1, queen[0] + 2):
                if i != self.queens_num and i != -1:
                    for j in range(queen[1] - 1, queen[1] + 2):
                        if j != self.queens_num and j != -1:
                            successor, path = self.move(queen, (i, j))
                            h = successor.heuristic()
                            if len(successor.queens) != 0 :
                                successors.append((successor, h, path))
            successorsForEachQueens += successors
        return sorted(successorsForEachQueens, key = lambda x: x[1])
    
    def move(self, queen, state):
        i, j = state
        next = QueenProblem(self.queens_num)
        next.queens = deepcopy(self.queens)

        if((i, j) not in next.queens):
            path = [str(next.queens.index(queen)) + " in " + str(queen) + " -> " + str(state)]
            next.queens.insert(next.queens.index(queen), (i, j))
            next.queens.remove(queen)
        else:
            next.queens = []
            path = []
        return next, path
    

problem = QueenProblem(8)
# https://helloacm.com/wp-content/uploads/2020/01/8-queens.png
# Change last column from 4->5
problem.queens = [(0, 1), (1, 3), (2, 5), (3, 7), (4, 2), (5, 0), (6, 6), (7, 5)]
print(problem.getState())
initialH = problem.heuristic()
print('heuristic:', initialH)
current = (problem, initialH, [])
answer = None

while(True):
    successors = current[0].getSuccessors()
    successor = successors[0]
    if successor[1] >= current[1]:
        answer = current
        break
    current = (successor[0], successor[1], current[2] + successor[2])
    print(current[2][-1])
    print(current[0].getState())
    print('new heuristic:', current[1])

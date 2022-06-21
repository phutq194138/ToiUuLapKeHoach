import random
import copy
n = 8
edge = [[1, 2, 4, 5], [0, 3, 4, 7], [0, 3, 5], [1, 2, 6], [0, 1, 6], [0, 2], [3, 4], [1]]
k = 4

def init():
    global k
    tmp = []
    for _ in range(n):
        tmp.append(random.randint(0, k))
    return tmp

def calculate_fitness(x):
    violation = 0
    for i in range(n):
        for j in edge[i]: 
            # Neighbors of vertice i
            if x[i] == x[j]:
                violation += 1
    return violation // 2

def get_neighbours(x):
    for i in range(n):
        x_tmp = copy.deepcopy(x)
        for new_color in range(k):
            if new_color != x[i]:
                x_tmp[i] = new_color
                yield x_tmp

if __name__ == "__main__":
    x = init()
    count = 0
    while True:
        fitness = calculate_fitness(x)
        tmp = None
        min_fitness = fitness
        for y in get_neighbours(x):
            if calculate_fitness(y) < fitness:
                min_fitness = calculate_fitness(y)
                tmp = y
        if min_fitness == fitness:
            count += 1
        else:
            x = tmp
            count = 0    
        if count >= 80:
            break
  
    print("Colors of Points in Graph: {}".format(x))

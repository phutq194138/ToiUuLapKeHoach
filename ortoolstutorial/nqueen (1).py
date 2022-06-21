import random 
import copy

def initialize():
    state = list()
    for i in range(8):
        state.append([i,random.randrange(9)])
    return state

def check_eating(a,b):
    return (a[1]==b[1]) or (abs(a[0]-b[0])==abs(a[1]-b[1]))

def heuristic_function(state):
    pairs = 0
    for i in range(1,7):
        queen = state[i]
        for j in range(i+1,8):
            if check_eating(queen,state[j]):
                pairs +=1

    return pairs

def hill_climbing():
    sol = initialize()
    curr_point = heuristic_function(sol)
    iter = 1000
    curr_iter=0
    stop_search = (curr_point==0)
    while(stop_search==False):
        
        for i in range(8):
            new_state = copy.deepcopy(sol)
            for j in range(1,8):
                new_state[i][1]=(sol[i][1]+j)%8
                new_point = heuristic_function(new_state)
                if (new_point==0):
                    sol=new_state
                    return sol
                elif (new_point<curr_point):
                    sol=new_state
                    i-=1
                    break
        curr_iter+=1
        if (curr_iter>iter):
            stop_search = True
    return sol

print(hill_climbing())
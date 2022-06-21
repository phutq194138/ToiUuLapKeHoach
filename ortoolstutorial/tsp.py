f = open('tsp.txt', 'r')
n = int(f.readline().strip())
print(n)
c = []
c.append([0]*11)
for i in range(n):
	c.append([0] + [int(i) for i in f.readline().strip().split()])

from ortools.sat.python import cp_model

model = cp_model.CpModel()

x = [0]*(n+1)
x[0] = model.NewIntVar(1, n, 'x[{}]'.format(0))
x[n] = model.NewIntVar(1, n, 'x[{}]'.format(n))
for i in range(1, n):
	x[i] = model.NewIntVar(2, n, 'x[{}]'.format(i))

model.Add(x[0] == 1)
model.Add(x[n] == 1)
model.AddAllDifferent(x[1:-1])

model.Maximize(sum([c[x[i]][x[i-1]] for i in range(1, n+1)]))

solver = cp_model.CpSolver()
status = solver.Solve(model)


for i in range(n+1):
	print(solver.Value(x[i]))


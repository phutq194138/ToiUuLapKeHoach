from ortools.linear_solver import pywraplp
import sys

f = open('input/inputn=6k=2.txt', 'r')
_n, _k = f.readline().strip().split(" ")
n, k = int(_n), int(_k)
q = [0]
for j in f.readline().strip().split():
	q.append(int(j))
c = []
for i in range(2*n+1):
	c.append([int(j) for j in f.readline().strip().split()])

model = pywraplp.Solver.CreateSolver('GLOP')
INF = sys.maxsize - 1
h = int(1e6)

X = [[0]*(2*n+2*k+1)]*(2*n+k+1)
Y = [0]*(2*n+2*k+1)
Z = [[0]*(k+1)]*(2*n+2*k+1)

for i in range(1, 2*n+1):
	Y[i] = model.IntVar(0, INF, "Y[" + str(i) + "]")
	for j in range(1, k+1):
		Z[i][j] = model.IntVar(0, 1, "Z["+str(i)+","+str(j)+"]")

for i in range(1, k+1):
	I  = i+2*n
	Ik = i+2*n+k
	Y[I]  = model.IntVar(0, 0, "Y["+str(I)+"]")
	Y[Ik] = model.IntVar(0, INF, "Y["+str(Ik)+"]")
	for j in range(1, k+1):
		if i == j:
			Z[I][j]  = model.IntVar(1, 1, "Z["+str(I)+","+str(j)+"]")
			Z[Ik][j] = model.IntVar(1, 1, "Z["+str(Ik)+","+str(j)+"]")
		else:
			Z[I][j]  = model.IntVar(0, 1, "Z["+str(I)+","+str(j)+"]")
			Z[Ik][j] = model.IntVar(0, 1, "Z["+str(Ik)+","+str(j)+"]")

for i in range(1, 2*n+k+1):
	const = model.Constraint(1, 1)
	for j in range(1, 2*n+1):
		X[i][j] = model.IntVar(0, 1, "X["+str(i)+","+str(j)+"]")
		const.SetCoefficient(X[i][j], 1)
	for j in range(2*n+k+1, 2*n+2*k+1):
		X[i][j] = model.IntVar(0, 1, "X["+str(i)+","+str(j)+"]")
		const.SetCoefficient(X[i][j], 1)

# for i in range(1, 2*n+1):
# 	const = model.Constraint(1, 1)
# 	for j in range(1, 2*n+k+1):
# 		const.SetCoefficient(X[i][j], 1)

for i in range(2*n+k+1, 2*n+2*k+1):
	const = model.Constraint(1, 1)
	for j in range(1, 2*n+k+1):
		const.SetCoefficient(X[i][j], 1)

for i in range(1, 2*n+k+1):
	I = i 
	if i > 2*n:
		I = 0
	for j in range(1, 2*n+1):
		const1 = model.Constraint(-INF, h+c[I][j])
		const2 = model.Constraint(-h+c[I][j], INF)
		const1.SetCoefficient(X[i][j], h)
		const1.SetCoefficient(Y[j], 1)
		const1.SetCoefficient(Y[i], -1)
		const2.SetCoefficient(X[i][j], -h)
		const2.SetCoefficient(Y[j], 1)
		const2.SetCoefficient(Y[i], -1)
		for l in range(1, k+1):
			const3 = model.Constraint(-INF, h)
			const4 = model.Constraint(-h, INF)
			const3.SetCoefficient(X[i][j], h)
			const3.SetCoefficient(Z[i][m], 1)
			const3.SetCoefficient(Z[j][m], -1)
			const4.SetCoefficient(X[i][j], -h)
			const4.SetCoefficient(Z[i][m], 1)
			const4.SetCoefficient(Z[j][m], -1)
	for j in range(2*n+k+1, 2*n+2*k+1):
		const1 = model.Constraint(-INF, h+c[I][0])
		const2 = model.Constraint(-h+c[I][0], INF)
		const1.SetCoefficient(X[i][j], h)
		const1.SetCoefficient(Y[j], 1)
		const1.SetCoefficient(Y[i], -1)
		const2.SetCoefficient(X[i][j], -h)
		const2.SetCoefficient(Y[j], 1)
		const2.SetCoefficient(Y[i], -1)
		for l in range(1, k+1):
			const3 = model.Constraint(-INF, h)
			const4 = model.Constraint(-h, INF)
			const3.SetCoefficient(X[i][j], h)
			const3.SetCoefficient(Z[i][m], 1)
			const3.SetCoefficient(Z[j][m], -1)
			const4.SetCoefficient(X[i][j], -h)
			const4.SetCoefficient(Z[i][m], 1)
			const4.SetCoefficient(Z[j][m], -1)

for i in range(1, n+1):
	const = model.Constraint(-INF, 0)
	const.SetCoefficient(Y[i], 1)
	const.SetCoefficient(Y[i+N], 1)

for i in range(1, 2*n+2*k+1):
	const = model.Constraint(1, 1)
	for j in range(1, k+1):
		const.SetCoefficient(Z[i][j], 1)

for i in range(1, k+1):
	const = model.Constraint(0, q[i])
	for j in range(1, n+1):
		const.SetCoefficient(Z[j][j], 1)
		const1 = model.Constraint(0, 0)
		const1.SetCoefficient(Z[j][i], 1)
		const1.SetCoefficient(Z[j+n][i], -1)

distance = model.IntVar(0, sum(Y[2*n+k+1:2*n+2*k+1]), "distance")
model.Minimize(distance)

status = model.Solve()
if status == pywraplp.Solve.OPTIMAL:
	print("OK")
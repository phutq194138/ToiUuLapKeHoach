#Linear Progaming
from ortools.linear_solver import pywraplp

model = pywraplp.Solver.CreateSolver("SCIP")

inf = model.infinity()

x = model.IntVar(0, inf, 'x')
y = model.IntVar(0, inf, 'y')

model.Add(x + 2*y <= 14.0)
model.Add(3*x - y >=0)
model.Add(x - y <= 2)

model.Maximize(3*x + 4*y)

status = model.Solve()

print('f=', model.Objective().Value())
print('x=', x.solution_value())
print('y=', y.solution_value())
k = max(50, 45, 37)
print('k= %d' % k)
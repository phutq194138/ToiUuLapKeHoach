from ortools.sat.python import cp_model

class VarArraySolutionPrinterWithLimit(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables, limit):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0
        self.__solution_limit = limit

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()
        if self.__solution_count >= self.__solution_limit:
            print('Stop search after %i solutions' % self.__solution_limit)
            self.StopSearch()

    def solution_count(self):
        return self.__solution_count

model = cp_model.CpModel()

x = [0] * 10
for i in range(10):
	x[i] = model.NewIntVar(5, 100, 'x[{}]'.format(i))

model.Add(sum(x) == 100)
model.AddAllDifferent(x)

solver = cp_model.CpSolver()
status = solver.Solve(model)

solution_printer = VarArraySolutionPrinterWithLimit(x, 5000)
# Enumerate all solutions.
solver.parameters.enumerate_all_solutions = True
# Solve.
status = solver.Solve(model, solution_printer)
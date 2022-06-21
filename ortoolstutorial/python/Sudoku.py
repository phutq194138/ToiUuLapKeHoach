from VarIntLS import VarIntLS
from LocalSearchManager import LocalSearchManager
from NotEqual import NotEqual
from ConstraintSystem import ConstraintSystem
import random as rd

class SwapMove:
	def __init__(self,i,j1,j2):
		self.i = i
		self.j1 = j1
		self.j2 = j2

		
mgr = LocalSearchManager()
x = [[VarIntLS(mgr,1,9,j+1,'x[' + str(i) + ',' + str(j) + ']') for i in range(9)] for j in range(9)]

def printSolution():
	for i in range(9):
		info = ''
		for j in range(9):
			info = info + str(x[i][j].getValue()) + ' '
		print(info + '\n')

printSolution()
		
constraints = []
for i in range(9):
	for j1 in range(8):
		for j2 in range(j1+1,9):
			cr = NotEqual(x[i][j1],x[i][j2],'not-equal[r' + str(i) + ',' + str(j1) + ',' + str(j2) + ']')
			constraints.append(cr)
			cc = NotEqual(x[j1][i], x[j2][i],'not-equal[' + str(j1) + ',' + str(j2) + ',c' + str(i) + ']')
			constraints.append(cc)
			
for I in range(3):
	for J in range(3):
		for i1 in range(3):
			for j1 in range(3):
				for i2 in range(3):
					for j2 in range(3):
						if i1 < i2 or i1 == i2 and j1 < j2:
							c = NotEqual(x[3*I+i1][3*J+j1],x[3*I+i2][3*J+j2],'not-equal[' + str(I) + ',' + str(J) + ':(' + str(i1) + ',' + str(j1) + '),(' + str(i2) + ',' + str(j2) + ')]')
							constraints.append(c)
							
S = ConstraintSystem(constraints)

mgr.close()

print('variables = ',len(mgr.getVariables()))
print('invariants = ',len(mgr.getInvariants()))

#X1.setValuePropagate(4)
print('init violations = ',S.violations())
for i in range(9):
	for j in range(9):
		x[i][j].setValuePropagate(j+1)
		#print('violations = ',S.violations())

for iter in range(1000000):
	minD = 100000
	cand = []
	for i in range(9):
		for j1 in range(8):
			for j2 in range(j1+1,9):
				d = S.getSwapDelta(x[i][j1],x[i][j2])
				if d < minD:
					cand = []
					cand.append(SwapMove(i,j1,j2))
					minD = d
				elif d == minD:
					cand.append(SwapMove(i,j1,j2))
	i = rd.randint(0,len(cand)-1)
	m = cand[i]
	x[m.i][m.j1].swapValuePropagate(x[m.i][m.j2])
	print(iter,': swap ',i,',',j1,',',j2,' violations = ',S.violations())
	if S.violations() == 0:
		break
		
printSolution()
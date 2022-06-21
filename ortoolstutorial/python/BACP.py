from VarIntLS import VarIntLS
from LocalSearchManager import LocalSearchManager
from NotEqual import NotEqual
from NotEqualFunction import NotEqualFunction
from LessOrEqualFunctionConst import LessOrEqualFunctionConst
from ConditionalSum import ConditionalSum
from ConstraintSystem import ConstraintSystem
from PlusVarConst import PlusVarConst

import random as rd

def printSolution():
	for i in range(m):
		info = 'b[' + str(i) + ']: '
		for j in range(n):
			if x[j].getValue() == i:
				info = info + str(j) + ',w(' + str(w[j]) + ') '
		info = info + ' f = ' + str(f[i].getValue())
		print(info + '\n')
	return
	
w = [2,7,2,4,4,3,5,13,5]# b[0] = {1,3,4}, b[1] = {2,7}, b[2] = {0,5,6,8}
Q = [15,15,15]
n = len(w)
m = len(Q)

mgr = LocalSearchManager()
x = [VarIntLS(mgr,0,m-1,0,'x[' + str(i) + ']') for i in range(n)]
constraints = []

f = [ConditionalSum(x,w,i,'ConditionalSum[' + str(i) + ']') for i in range(m)]		
for i in range(m):
	c = LessOrEqualFunctionConst(f[i],Q[i],'LessOrEqualFunctionConst[' + str(i) + ']')
	constraints.append(c)
	
CS = ConstraintSystem(constraints)
mgr.close()

class Move:
	def __init__(self,i,v):
		self.i = i
		self.v = v
def initSolution():
	for i in range(n):
		v = rd.randint(x[i].getMinValue(), x[i].getMaxValue())
		x[i].setValuePropagate(v)

initSolution()
		
cur = CS.violations()
print('init, CS = ',cur)
for i in range(m):
	print('init f[' + str(i) + '] = ',f[i].getValue())

best = CS.violations()
nic = 0
maxStable = 50
	
for iter in range(100000):
	cand = []
	minD = 1000000
	for i in range(n):
		for v in range(x[i].getMinValue(),x[i].getMaxValue() + 1):
			d = CS.getAssignDelta(x[i],v)
			#print(iter,': assignDelta(',i,',',v,') = ',d)
			if d < minD:
				cand = []
				cand.append(Move(i,v))
				minD = d
			elif d == minD:
				cand.append(Move(i,v))

	idx = rd.randint(0,len(cand)-1)
	print(iter,': cand = ',len(cand),' idx = ',idx)
	move = cand[idx]
	x[move.i].setValuePropagate(move.v)
	print(iter,': assign x[',move.i,'] = ',move.v,' violations = ',CS.violations())
	for i in range(m):
		print(iter,': f[' + str(i) + '] = ',f[i].getValue())
	#print(' x = ',[x[i].getValue() for i in range(n)])
	if CS.violations() == 0:
		break
	if cur + minD != CS.violations():
		print('BUG, cur = ',cur,' delta = ',minD,' CS = ',CS.violations())
		break
	
	if CS.violations() < best:
		best = CS.violations()
		nic = 0
	else:
		nic += 1
		if nic >= maxStable:
			initSolution()
			nic = 0
	
	cur = CS.violations()	
	
printSolution()	
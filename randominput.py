# f = open('Model.csv', mode='a+', encoding='utf-8')

# f.write('1,111,MH370\n')
# f.write('2,123,Boing777\n')
# f.write('3,112,KH113\n')

import random

def output(a):
	f = open('input/inputn=10.5.txt', mode='a+', encoding='utf-8')
	s = len(a)
	for i in range(len(a)):
		string = ''
		for j in a[i]:
			string = string + str(j) + ' '
		f.write(string + '\n')
	f.close()

n = 10

b = [[random.randint(1, 99) for i in range(2*n+1)] for i in range(2*n+1)]
for i in range(2*n+1):
	for j in range(2*n+1):
		if i == j:
			b[i][j] = 0

output(b)


f = open('tsp.txt', 'r')
n = int(f.readline().strip())
print(n)
c = []
c.append([0]*11)
for i in range(n):
	c.append([0] + [int(i) for i in f.readline().strip().split()])

print(c[1][2])
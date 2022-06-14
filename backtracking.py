f = open('input/inputn=8k=2.txt', 'r')
_l = f.readline().strip().split()
n, k = int(_l[0]), int(_l[1])

q = [0]
for i in f.readline().strip().split():
	q.append(int(i))

c = []
for i in range(2*n+1):
	c.append([int(j) for j in f.readline().strip().split()])

f.close()

c_min = 9999999
for i in range(2*n+1):
	for j in range(2*n+1):
		if i != j:
			if c[i][j] < c_min:
				c_min = c[i][j]

p, y, z, t = [0]*(k+1), [0]*(k+1), [0]*(k+1), [0]*(k+1)
#p[i] số khách hiện có trên xe i
#y[i] số khách mà xe i cần đón
#z[i] số khách mà xe i đã chở đến điểm cuối
#t[i] số khách mà xe i đã đón

x = [0]*(2*n+k+1)
#vị trí các điểm

d = 0#Quãng đường hiện tại

d_min = 999999999 #Quãng đường nhỏ nhất

e = 1
#xe hiện tại đang xét

v = [False]*(2*n+2)
#mảng đánh dấu các điểm đã đi

b = [[False]*(2*n+k+1)]*(k+1)
#b[i][j] xư thứ i đã đón khách j

r = []
#lưu các điểm đường đi bé nhất

s = 0

def solveX():
	global d_min, r
	if d < d_min:
		r = [i for i in x]
		d_min = d
		print("update_min=", d_min)
		print("route:", x)

def check(a, i):
	if i == 0:
		if z[e] == y[e]:
			return True
		else:
			return False
	if v[i]:
		return False
	if i <= n:
		if p[e] == q[e]:
			return False
		if t[e] == y[e]:
			return False
	if i > n:
		if v[i-n] == False:
			return False
		if b[e][i-n] == False:
			return False
	return True

def TRY_X(a):
	global d, e
	for i in range(2*n+1):
		if check(a, i):
			x[a] = i 
			d += c[x[a-1]][i]
			if i != 0:
				v[i] = True
			if i == 0:
				e += 1
			else:
				if i <= n:
					p[e] += 1
					t[e] += 1
					b[e][i] = True
				else:
					p[e] -= 1
					z[e] += 1
			if a == 2*n + k:
				solveX()
			else:
				if True and (d + (2*n+k-a)*c_min) < d_min:
					TRY_X(a+1)
			if i != 0:
				v[i] = False
			if i == 0:
				e -= 1
			else:
				if i <= n:
					p[e] -= 1
					t[e] -= 1
					b[e][i] = False
				else:
					p[e] += 1
					z[e] -= 1
			d -= c[x[a-1]][i]

def solveY():
	y[k] = n - s
	#print(y[1:])
	TRY_X(1)

#chia n người vào k xe
def TRY_Y(a):
	global s
	if k == 1:
		solveY()
		return
	for i in range(n+1):
		if n - s - i >= 0:
			y[a] = i
			s = s + i 
			if a == k-1:
				solveY()
			else:
				if n - s > 0:
					TRY_Y(a+1)
			s = s - i

def printSolution():
	print("Distance min=", d_min)
	print("Route:")
	i, j, l = 0, 1, 1
	while j < len(r):
		if r[j] == 0:
			h = r[i:j+1]
			print("Vehicle "+str(l)+":", sep=" ")
			print(*h, sep=" -> ")
			l += 1
			i = j
		j += 1

TRY_Y(1)
printSolution()
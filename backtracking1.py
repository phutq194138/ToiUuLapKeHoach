#input
f = open("input/inputn=10.1.txt", 'r')
line = f.readline()
_n, _q = line.strip().split()
n, q = int(_n), int(_q)
c = []
for i in range(2*n+1):
	c.append([int(j) for j in f.readline().strip().split()])
#tim cmin
c_min = 99999
for i in range(2*n+1):
	for j in range(2*n+1):
		if i != j:
			if c[i][j] < c_min:
				c_min = c[i][j]

d_min = 99999999 # qd nho nhhat
d = 0 #tong quang duong
p = 0 #so khach tren xe
v = [False]*(2*n+1) # mang danh dau
x = [0]*(2*n+1) #lua duong di

def check(k, i):
	global n, q, p
	if v[i]:
		return False
	if i <= n:
		if p == q:
			return False
	if i > n:
		if v[i-n] == False:
			return False
	return True

def solve():
	global d, d_min, p, v, n, q, c_min
	d += c[x[2*n]][0]
	if d < d_min:
		d_min = d 
		print("Update min=", d_min)
	d -= c[x[2*n]][0]

def TRY(k):
	global d, p, v, n, q
	for i in range(1, 2*n+1):
		if check(k, i):
			x[k] = i
			v[i] = True
			d += c[x[k-1]][i]
			if i <= n:
				p += 1
			else:
				p -= 1

			if k == 2*n:
				solve()
			elif True and d + (2*n - k)*c_min < d_min:
				TRY(k+1)

			if i <= n:
				p -= 1
			else:
				p += 1
			v[i] = False
			d -= c[x[k-1]][i]

TRY(1)
print(d_min)

def composites():
	m=int(input())
	n=[]
	o=0
	for i in range(1,n//2+1):
		if g%i==0:
			l.append(i)
	l.append(g)
	for i in l:
		print(i)
try:
	composites()
except:
	print('invalid')

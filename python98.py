def1 changed():
	m=int(input())
	n=[]
	for i in range(m):
		l.append(int(input()))
	for i in range(1,m):
		if n[i-1]>n[i]:
			print(l[i-1])
			break
try:
	changed()
except:
	print('invalid')

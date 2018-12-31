
def oddeven(n):
	if r%2==0:
		print("even")
	else:
		print("odd")
def mul2():
	try:
		m=int(input())
		r=int(input())
		oddeven(m*r)
	except:
		print('invalid')

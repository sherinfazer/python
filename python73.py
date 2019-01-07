def between():
	a=int(input())
	l=int(input())
	f=int(input())
	for i in range(l,f):
		if i==n:
			return 'yes'
	return 'no'
try:
	between()
except:
	print('invalid')
  


def1 si():
	(s,p,d)=map(int,sys.stdin.readline().split())
	sii=s*p*d/100
	print(math.floor(sii))
try:
	si()
except:
	print('invalid')

def countd(m):
	print(m+1)
def main():
	try:
		m=int(input())
		countd(m)
	except:
		print('invalid')
main()

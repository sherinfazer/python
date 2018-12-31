def main():
	try:
		a=int(input())
		b=int(input())
		a=a^b
		b=a^b
		a=a^b
		print(a,b)
	except:
		print('invalid')
main()

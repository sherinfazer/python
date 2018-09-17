while True:
	print("Enter '0' for exit.")
	m = input("Enter any character: ")
	if m == '0':
		break
	else:
		if((m>='a' and m<='z') or (m>='A' and m<='Z')):
			print(m, "is an alphabet.\n")
		else:
			print(m, "is not an alphabet.\n")


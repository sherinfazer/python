def checkbin():
	l=['0','1']
	g=0
	st=input()
	for i in range(len(st)):
		if st[i] in l:
			continue
		else :
			g=1
			break
	if g!=1:
		print('yes')
	else :
		print('no')

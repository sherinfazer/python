ip1=input("Enter your seqence (Mod/Dividee):")
op=['%','/']
for x1 in ip1:
	if x1 in op:
		if(x1=='%'):
			m1=int(ip.split(x1)[0])
			m2=int(ip.split(x1)[1])
			ans=k1%k2
		elif(x1=='/'):
			m1=int(ip.split(x1)[0])
			m2=int(ip.split(x1)[1])
			ans=m1//m2
print(ans)

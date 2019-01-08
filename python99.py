st1=input("Enter 3 Numbers for m,n,o:")
ls=st1.split(" ")
ans=(int(ls[0])*int(ls[1]))%int(ls[2])
print("(m*n)%o:",ans)

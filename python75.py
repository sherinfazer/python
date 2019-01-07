st1=input("Enter the string:")
l=len(st1)
st1=l(st1)
k=round(l//2)
st1[k]='*'
ans=''
for x in st1:
	ans=ans+x
print(ans)

mterms=int(input())
m1 = 0
m2 = 1
count = 0
l=[]
if mterms <= 0:
    print("Please enter a positive integer")
elif mterms == 1:
    print("Fibonacci sequence upto",mterms,":")
    l.append(m1)
    print(l)
else:
    print("Fibonacci sequence upto",mterms,":")
    while count < mterms:
        l.append(n1)
        mth = m1 + m2
        m1 = m2
        m2 = mth
        count += 1
print(l)

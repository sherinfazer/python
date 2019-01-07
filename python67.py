import math
m2=int(input("Enter Value"))
if m2<10: print("10")
else:
    l2=len(str(m2))
    m2+=5
    m2=m2/(10**(l2-1))
    print(math.floor(m2)*(10**(l2-1)))

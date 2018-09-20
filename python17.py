def power(m, n):
    if n==0:
        return 1
    if n%2==0:
        return power(m, n/2)*power(m, n/2)
    return x*power(m, n/2)*power(m, n/2)
 
def order(m):
    n = 0
    while (m!=0):
        n = n+1
        m = m/10
    return n
def isArmstrong (m):
    n = order(m)
    temp = m
    sum1 = 0
    while (temp!=0):
        r = temp%10
        sum1 = sum1 + power(r, n)
        temp = temp/10
    return (sum1 == m)
m = 153
print(isArmstrong(m))
m = 1253
print(isArmstrong(m))

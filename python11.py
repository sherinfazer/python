d power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=h(input("Enter base: "))
exp=h(input("Enter exponential value: "))
print("Result:",power(base,exp))

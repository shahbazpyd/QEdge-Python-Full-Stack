n1=3
n2=3
n3=4
e=1
for r in range(1,n1+1):
    for s in range(1, n2+1):
        print(" ", end="")
    for v in range(1,e+1):
        print("*",end="")          
    print()
    n2=n2-1
    e=e+2 
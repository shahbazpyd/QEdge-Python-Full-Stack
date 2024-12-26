def check(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count=count+1

    if count>0:
        print("composite")
    else:
        print("prime")
        
        
n=int(input("enter a number"))
check(n)
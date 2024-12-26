def check(a,b):
    a=a+b
    b=a-b
    a=a-b
    print("a=",a)
    print("b=",b)
    
a=int(input("enter first number"))
b=int(input("enter second number"))
print("befor swaping")
print("a=",a)
print("b=",b)
print("after swapping")
check(a,b)
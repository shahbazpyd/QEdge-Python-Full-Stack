def check(s):
    r=s
    t=s[::-1]
    if r==t:
        print("palindrm")
    else:
        print("not plindrom")
        
s=input("enter string to know plindrom")
check(s)
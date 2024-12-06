# def cube(a, function):
#     sq=function(a)
#     return sq*a

# res=cube(10, lambda x:x*x)
# print(res)


# print("begin")
# myfun=lambda p:p*p
# res=myfun(10)
# print(res)
# print("end")


# x= list(filter(lambda p: p%2==0, [10, 11, 12, 13, 14, 15]))
# print(x)

# y= list(filter(lambda p: p%3==0, [10, 11, 12, 13, 14, 15]))
# print(y)

x= list(map(lambda p: p%2==0, [10, 11, 12, 13, 14, 15]))
print(x)

y= list(map(lambda p: p*p, [10, 11, 12, 13, 14, 15]))
print(y)
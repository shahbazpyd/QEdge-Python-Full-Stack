# concepts: creation, element access, modify element, search element, extera operations
# Nested List, creation, access element, List Comprehensions
# creation
# print("==============creation================")
# x= list()
# print(x)
# print(type(x))
# print(len(x))
# print("-------------creation------------------")

# y=[]
# print(y)
# print(type(y))
# print(len(y))
# print("-------------creation------------------")

# z=[10,20,30,40]
# print(z)
# print(type(z))
# print(len(z))

# print("---------------creation----------------")
# p=[100,200,100,200,100,300]
# print(p)
# print(type(p))
# print(len(p))

# print("--------------creation-----------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# print(type(q))
# print(len(q))

# print("=============element access=================")
# #element access
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# print(q[2])
# print(q[-2])

# print("--------------element access-----------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# i=0
# while i<len(q):
#     print(q[i])
#     i+=1
            
# print("-------------element access------------------")  
# q=[100, 123.123,True,"list",3+4j]
# print(q)  
# for i in q:
#     print(i)
    
# print("-------------element access------------------") 
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# a,b,c,d,e=q
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
    
# modify element
# print("================modify element====================")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# q[2]=False
# print(q)

# print("-------------modify element------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# q.append("shahbaz")
# print(q)

# print("-------------modify element------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# q.extend("shahbaz")
# print(q)

# print("-------------modify element------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# q.insert(3,"list2")
# print(q)

# print("-------------modify element------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# q.append([100,200,300])
# print(q)

# print("-------------modify element------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# q.extend([100,200,300])
# print(q)

# print("-------------modify element------------------")
# q=[100, 123.123,True,"list",3+4j,100]
# print(q)
# q.remove(100)
# print(q)

# print("-------------modify element------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# q.pop()
# print(q)

# print("-------------modify element------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# q.pop(2)
# print(q)


# print("-------------modify element------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# q.clear()
# print(q)
# q.pop()
# print(q)


# print("-------------modify element------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# i=0
# while i<len(q):
#     if i==2:
#         q[i]=True
#     print(q[i])
#     i+=1
    
# print("-------------modify element------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# for i in range(len(q)):
#     if i==2:
#         q[i]=False
#     print(q[i])
    

# search element
# print("==================search element================")
# x=[10,20,30,40,50,60]
# print(x)
# i= int(input("enter search element"))
# if i in x:
#     print("element found")
# else:
#     print("element not found")
    
    
# print("-------------------search element------------------------------")
# x=[10,20,30,40,50,60]
# print(x)
# i= int(input("enter search element"))
# for p in x:
#     if p==i:
#         print("element found")
#         break
# else:
#     print("element not found")
    

# print("-----------------search element--------------------------------")
# x=[10,20,30,40,50,60]
# print(x)
# i= int(input("enter search element"))
# for p in range(len(x)):
#     if x[p]==i:
#         print("element found")
#         break
# else:
#     print("element not found")
    
    

# print("-----------------search element--------------------------------")
# x=[10,20,30,40,50,60]
# print(x)
# i= int(input("enter search element"))
# j=0
# while j<len(x):
#     if x[j]==i:
#         print("element found")
#         break 
#     j+=1
# else:
#     print("element not found")
    
    
# extera operations
# print("-------------extera operations------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# r= q.copy()
# print(r)

# print("-------------extera operations------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# q.reverse()
# print(q)

# print("-------------extera operations------------------")
# s=[20,30,10,50,20,40]
# print(s)
# s.sort()
# print(s)

# print("-------------extera operations------------------")
# q=[100, 123.123,True,"list",3+4j]
# print(q)
# s.sort(reverse=True)
# print(s)   


# # Nested List
# print("============Nested List=================")
# # creation
# print("-------------creation-------------------")
# a=list(list())
# print(a)

# print("-------------creation-------------------")
# b=[[]]
# print(a)


# print("-------------creation-------------------")
# x=[[10,20,30],[40,50,60],[70,80,90]]
# print(x)

# print("-------------access element-------------------")
# x=[[10,20,30],[40,50,60],[70,80,90]]
# print(x[0])
# print(x[1])
# print(x[2])
# print(x[0][0])
# print(x[0][1])
# print(x[0][2])
# print(x[1][0])
# print(x[1][1])
# print(x[1][2])
# print(x[2][0])
# print(x[2][1])
# print(x[2][2])

# print("-------------access element-------------------")
# x=[[10,20,30],[40,50,60],[70,80,90]]
# print(x)
# for i in x:
#     for j in i:
#         print(j)


# print("-------------access element-------------------")
# x=[[10,20,30],[40,50,60],[70,80,90]]
# print(x)
# for i in x:
#     for j in i:
#         print(j,end=" ")
#     print()


# print("-------------access element-------------------")
# x=[[10,20,30],[40,50,60],[70,80,90]]
# i=0
# while i<len(x):
#     j=0
#     while j<len(x[i]):
#         print(x[i][j],end=" ")
#         j+=1
#     print()
#     i+=1

# print("-------------access element-------------------")
# x=[[10,20,30],[40,50,60],[70,80,90]]
# print(x)
# for p,q,r in x:
#     print(p,q,r)

    
# print("-------------access element-------------------")
# data=[[1001,"mobile",20000.00],[1002, "mouse",1000.00],[1003,"book",2000.00]]
# print(data)
# tot_cost=0
# for p in data:
#     print(p)
#     tot_cost+=p[2]
# print("total cost",tot_cost)

# print("-------------access element-------------------")
# data=[[1001,"mobile",20000.00],[1002, "mouse",1000.00],[1003,"book",2000.00]]
# print(data)
# tot_cost=0
# for p,q,r in data:
#     print(p,q,r)
#     tot_cost+=r
# print("total cost",tot_cost)

 
# List Comprehensions:  
# print("==================List Comprehensions===================")
# x=[p for p in range(1,11)]
# print(x)

# y=[q*q for q in range(10,20) if q%2==0]
# print(y)

# z=[r*2 for r in range(20,30) if r%2!=0]
# print(z)

# print("---------------List Comprehensions-----------------")
# data="lokesh python java aws devops"
# print(data)
# words=data.split()
# print(words)
# res=[len(w) for w in words]
# print(res)


# print("---------------List Comprehensions-----------------")
# data="lokesh python java aws devops"
# print(data)
# words=data.split()
# print(words)
# res=[[w.upper(),w.lower(),len(w)] for w in words]
# print(res)
# # concepts: creation, element access, modify element, search element, extera-operations
# # Nested dict, creation, access element, dict Comprehensions


# # creation
# print("===============creation================")
# print("-------------creation------------------")
# x= dict()
# print(x)
# print(type(x))
# print(len(x))


# print("-------------creation------------------")
# y={}
# print(y)
# print(type(y))
# print(len(y))


# print("-------------creation------------------")
# z={"java":80, "python":90, "hadoop":70}
# print(z)
# print(type(z))
# print(len(z))


# print("-------------creation------------------")
# print("---------------hatrogenus keys and values----------------")
# p={100:"True", "java":3+4j, False:99}
# print(p)
# print(type(p))
# print(len(p))


# print("-------------creation------------------")
# print("--------------duplicate values----------------")
# q={"java":70, "spring":80, "hadoop":70}
# print(q)
# print(type(q))
# print(len(q))


# print("-------------creation------------------")
# print("-------------duplicate keys------------------")
# r={"java":70, "spring":80, "hadoop":70, "java":80}
# print(r)
# print(type(r))
# print(len(r))


# print("===============element access==============")
# print("----------------value access---------------")
# x={"java":80, "spring":90, "hadoop":70}
# print(x)
# print(x["java"])
# print(x["spring"])
# print(x["hadoop"])


# print("-------------element access------------------")
# x={"java":80, "spring":90, "hadoop":70}
# print(x)
# for k in x:
#     print(k,x[k])


# print("-------------element access------------------")
# x={"java":80, "spring":90, "hadoop":70}
# print(x)
# p=x.items()
# print(p)
# print(type(p))
# for k,v in p:
#     print(k,v) 

 
    
# print("-------------key access------------------")
# x={"java":80, "spring":90, "hadoop":70}
# print(x)
# p=x.keys()
# print(p)
# print(type(p))
# for k in p:
#     print(k,x[k])       
    
    
print("---------------value access------------------")
x={"java":80, "spring":90, "hadoop":70}
print(x)
p=x.values()
print(p)
print(type(p))
for v in p:
    print(v)


# print("================modify element===================")
# x={"java":80, "spring":90, "hadoop":70}
# print(x)
# x["python"]=85
# x["hadoop"]=75
# print(x)

# print("----------------------modify element methods-----------------------")
# x={"java":80, "python":90, "hadoop":70, "aws":80}
# print(x)
# x.update({"spring":85})
# x.update({"hadoop":75})
# print(x)


# print("----------------------modify element methods-----------------------")
# x={"java":80, "python":90, "hadoop":70, "aws":80}
# print(x)
# y=x.copy()
# print(y)
# p=x.pop("hadoop")
# print(x)
# print(p)
# q=x.popitem()
# print(x)
# print(q)


# print("----------------------modify element methods-----------------------")
# x={"java":80, "python":90, "hadoop":70, "aws":80}
# print(x)
# y=x.copy()
# print(y)
# x.clear()
# print(x)


# print("----------------------modify element methods-----------------------")
# x={"java":80, "python":90, "hadoop":70, "aws":80}
# print(x)
# y=x.copy()
# print(y)
# del x
# print(x)


# # print(id(x))
# # print(id(y))

# print("================search element===================")
# print("-----------------search keys---------------------")
# x={"java":"spring","python":"django","hadoop":"pig"}
# print(x)
# k=input("enter search key")
# if k in x:
# # if k in x.keys():
#     print("key found")
# else:
#     print("key not found")
    
    
# print("-----------------search values------------------")
# x={"java":"spring","python":"django","hadoop":"pig"}
# print(x)
# v=input("enter search value")
# if v in x.values():
#     print("value found")
# else:
#     print("value not found")


# print("-----------------search values------------------")
# x={"java":"spring","python":"django","hadoop":"pig"}
# print(x)
# v=input("enter search value")
# for k in x:
#     if x[k]==v:
#         print("value found")
# else:
#     print("value not found")
    


# print("=================Nested dict=====================")
# print("-----------------creation------------------------")
# x=dict(dict())
# print(x)

# print("-----------------creation------------------------")
# y={}
# print(y)

# print("-----------------creation------------------------")
# x={"java":{"sprint":90, "struct":80,"jsf":40},
#    "python":{"django":90, "flask":80, "fastapi":70},
#    "hadoop":{"hive":80, "pig":80, "spark":90}}
# print(x)


# print("-----------------access key------------------------")
# x={"java":{"sprint":90, "struct":80,"jsf":40},
#    "python":{"django":90, "flask":80, "fastapi":70},
#    "hadoop":{"hive":80, "pig":80, "spark":90}}
# print(x)
# print(x.keys())
# print(type(x.keys()))
# k=list(x.keys())
# print(k)
# print(k[0],k[1],k[2])
# print(f"{k[0],k[1],k[2]}")
# print(f"{k[0]},{k[1]},{k[2]}")



# print("-----------------access value------------------------")
# x={"java":{"sprint":90, "struct":80,"jsf":40},
#    "python":{"django":90, "flask":80, "fastapi":70},
#    "hadoop":{"hive":80, "pig":80, "spark":90}}
# print(x)
# k=list(x.keys())
# print(k)
# print(x[k[0]])
# print(x[k[1]])
# print(x[k[2]])
# print(f"{x[k[0]],x[k[1]],x[k[2]]}")

# print(f'{k[0]}:{x[k[0]]}')
# print(f'{k[1]}:{x[k[1]]}')
# print(f'{k[2]}:{x[k[2]]}')

# print(k[0],":",x["java"])
# print(k[1],":",x["python"])
# print(k[2],":",x["hadoop"])


# print("-----------------access element------------------------")
# x={"java":{"sprint":90, "struct":80,"jsf":40},
#    "python":{"django":90, "flask":80, "fastapi":70},
#    "hadoop":{"hive":80, "pig":80, "spark":90}}
# print(x)
# print(x["java"]["sprint"])
# print(x["java"]["struct"])
# print(x["java"]["jsf"])
# print(x["python"]["django"])
# print(x["python"]["flask"])
# print(x["python"]["fastapi"])
# print(x["hadoop"]["hive"])
# print(x["hadoop"]["pig"])
# print(x["hadoop"]["spark"])



# print("-----------------access element------------------------")
# x={"java":{"sprint":90, "struct":80,"jsf":40},
#    "python":{"django":90, "flask":80, "fastapi":70},
#    "hadoop":{"hive":80, "pig":80, "spark":90}}
# print(x)






# for key, value in x.items():
#     print(key)

# import json
# fiobj=open("mydata.json")
# data= json.load(fiobj)
# print(data)
# print(type(data))
# fiobj.close()


#  find the name of john's children
# import json
# fiobj=open("mydata.json")
# data= json.load(fiobj)
# print(data)
# print(type(data))
# fiobj.close()
# for p in data:
#     if "children" in p:
#         print(data["children"])


# what is john's second car name
import json
fiobj=open("mydata.json")
data= json.load(fiobj)
print(data)
print(type(data))
fiobj.close()
for p in data:
    if "cars" in p:
        print(data["cars"][1]["model"])
        break
    
    
# do john have pets
import json
fiobj=open("mydata.json")
data= json.load(fiobj)
if data["pets"]==None:
    print("no")
else:
    print("yes")
fiobj.close()




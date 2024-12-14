import pickle


# fiobj=open("myfile.txt", "x")
# print(fiobj)
# fiobj.close()


# fiobj=open("myfile.txt", "w")
# print(fiobj)
# print("file is opened")
# fiobj.write("Python Django\n java spring\n hadoop hive\n")
# fiobj.close()
# print("file closed")


# fiobj=open("myfile.txt", "a")
# print(fiobj)
# print("file is opened")
# # fiobj.write("Python Django\n java spring\n hadoop hive\n")
# result = fiobj.write("devops aws\n odoo fastapi\n")
# fiobj.close()
# print("file closed")
# print("result", result)


# fiobj=open("myfile.txt")
# print(fiobj)
# print("file is opened")
# data = fiobj.read()
# fiobj.close()
# print(data)
# print(type(data))
# print("file closed")



# fiobj=open("myfile.txt")
# print(fiobj)
# print(fiobj.tell())
# fiobj.seek(20)
# print(fiobj.tell())
# data=fiobj.read()
# print(data)
# print(type(data))
# print(fiobj.tell())
# fiobj.close()
# print("file closed")


# fiobj=open("myfile.txt")
# print(fiobj)
# print("file is opened")
# data= fiobj.readlines()
# print(data)
# print(type(data))
# for p in data:
#     print(p, end="")
# fiobj.close()
# print("file is closed")




fiobj=open("myfile1.txt", "w")
print(fiobj)
print("file is opened")
data= [[7788, "scott", 3000.00], [7902, "blak", 4000.00], [7369, "miler", 3500.00]]
print(data)
pickle.dump(data, fiobj)
fiobj.close()
print("file is closed")


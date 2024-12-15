# requirement is, count all the rooms according to user choice
import json
fiobj=open("F5_Week1.json")
data= json.load(fiobj)
print(data)
print(type(data))
fiobj.close()
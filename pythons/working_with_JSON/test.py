import json
data= {
    "name":"John",
    "age":30,
    "married":True,
    "divorced":False,
    "children":("Ann", "Bill"),
    "pets":None,
    "cars":[{"model":"BMW230", "mpg":27.5}, {"model":"FordEdge", "mpg":24.1}],
}

fiobj=open("mydata.json", "w")
json.dump(data, fiobj)
fiobj.close()

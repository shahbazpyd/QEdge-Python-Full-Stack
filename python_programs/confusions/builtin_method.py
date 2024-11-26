# doc = str(help(str))
# print(doc)

# data = "lokesh python django java hadoop aws"
# print(data)
# words = data.split()
# print(type(words))
# print(words)
# print(len(words))

data= "7788, scot, 3000.00 7902, black, 4000.00 7369, shahbaj, 5000.00"
word= data.split(" ")
print(word)
print(len(word))
for w in word:
    x= w.split(",")
    for p in x:
        print(p)
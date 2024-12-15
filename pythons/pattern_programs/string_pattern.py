# string_pattern
# s=abcd
# expected output=a ab abc abcd b bc bcd c cd d
s="abcd"  
# j=0
# while j<len(s):
#     k=j
#     while k<len(s):
#         print(s[j:k+1], end=" ")
#         k=k+1
#     j=j+1


r=range(0,len(s))
for i in r:
    for j in r:
        print(s[i:j+1], end=" ")
    print()
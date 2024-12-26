class A:
    def m1(self):
        print("this is  from A")
        
        
class B(A):#single inheritance
    def m2(self):
        print("this is from B")
        
        
class C(A):#Hierarchical inheritance
    def m3(self):
        print("this is from C")
        
class D(B):#Multilevel inheritance
    def m4(self):
        print("this is from D")
        
class E(D,C):#mutiple inheritance  
    def m5(self):
        print("this is from E")
        
           
print(E.__mro__)
e1=E()
e1.m1()
e1.m2()
e1.m3()
e1.m4()
e1.m5()






















        
# class Animal:
#     def __init__(self):
#         print("Animal created")

# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Mammal created")

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Fish created")

# class Bat(Mammal):
#     def __init__(self):
#         super().__init__()
#         print("Bat created")

# class Dolphin(Mammal, Fish):  # Hybrid Inheritance 
#     def __init__(self):
#         super().__init__() 
#         print("Dolphin created")
        
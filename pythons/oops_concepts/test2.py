# class Test:
#     """_summary_
#     """
#     a=1000
#     b=2000
#     def display(self):
#         print(Test.a)
#         print(Test.b)
# t1=Test()
# t1.display()
# print(Test.a)
# print(Test.b)



# class Test:
#     """_summary_
#     """
#     a=1000
#     b=2000
#     def display(self):
#         print(Test.a)
#         print(Test.b)
        
#     def modify(self):
#         Test.a = Test.a+100
#         Test.b = Test.b+100
        
# t1=Test()
# t1.display()
# t1.modify()
# t1.display()

# t2=Test()
# t2.display()





# class Test:
#     """_summary_
#     """
#     def insert(self):
#         self.a=1000
#         self.b=2000
        
#     def display(self):
#         print(self.a)
#         print(self.b)
        
# t1=Test()
# t1.insert()
# t1.display()
# print(t1.a)
# print(t1.b)

# t2=Test()
# # t2.insert()
# t2.display()
# print(t2.a)
# print(t2.b)




class Test:
    """_summary_
    """
    def insert(self):
        self.a=1000
        self.b=2000
        
    def display(self):
        print(self.a)
        print(self.b)
        
    def modify(self):
        self.a=self.a+100
        self.b=self.b-100
        
t1=Test()
t1.insert()
t1.display()
t1.modify()
t1.display()


t2=Test()
t2.insert()
t2.display()
t2.modify()
t2.display()


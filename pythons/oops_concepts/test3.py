# class Test:
#     """
#     """
#     def __init__(self):
#         print("construtor")
        
#     def display(self):
#         print("welcome from display")
        
# t1=Test()
# t1.display()
# t2=Test()
# t2.display()




class Test:
    """
    """
    def __init__(self):
        self.a=1000
        self.b=2000
        
    def display(self):
        print(self.a)
        print(self.b)
        
t1=Test()
print(t1)
t1.display()
t2=Test()
print(t2)
t2.display()
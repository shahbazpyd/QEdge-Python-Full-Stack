class Test:
    """sample class to test object
    """
    def display(self):
        print("wellcom from Test")
        
print(Test.__doc__)
t1=Test()
print(t1)
t1.display()



class Test2:
    """Test 2
    """
    def display(self):
        print("welcome from Test2")
        

t2=Test2()
t2.display()
class Product:
    """
    """
    def __init__(self, pid, pname, pcost, pmfd, pexp):
        self.pid=pid
        self.pname=pname
        self.pcost=pcost
        self.pmfd=pmfd
        self.pexp=pexp
        
    def display(self):
        print(self.pid,self.pname,self.pcost,self.pmfd,self.pexp)
        
p1=Product(1004, "colgate",100, "19 dec 2024" ,"10 dec 2025" )
p2=Product(1003, "milk", 50, "19 dec 2024","24 dec 2024")
p3=Product(1001, "curd", 40, "19 dec 2024","26 dec 2024")
p4=Product(1002, "Biscuit", 60, "19 dec 2024", "5 mar 2025")


x=[p1,p2,p3, p4]
for i in x:
    i.display()
    
    
x.sort(key= lambda c: c.pid)
for p in x:
    p.display() 
   
    
x.sort(key= lambda c: c.pname, reverse=True)
for p in x:
    p.display()   

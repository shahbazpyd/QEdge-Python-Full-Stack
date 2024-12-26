class Queu:
    def __init__(self):
        self.items=[]
        
        
    def isEmpty(self):
        return self.items==[]
    
    def enque(self,item):
        self.items.append(item)
        print(item,"enqued")
        self.display()
        
    def deque(self):
        if not self.isEmpty():
            i=self.items.pop(0)
            print(i,"item poped")
            self.display()
        else:
            print("Queu is empty")
    
        
    def size(self):
        print(len(self.items))
        
    def display(self):
        print(self.items)
        
        
queu=Queu()
while True:
    choice=int(input("enter your choice\n 1 enque\n 2 deqeu\n 3 display\n 4 size\n 5 Exit\n"))
    if choice==1:
        item=int(input("enter item"))
        queu.enque(item)
    elif choice==2:
        queu.deque()
        
    elif choice==3:
        queu.display()
    
    elif choice==4:
        queu.size()
        
    elif choice==5:
        break
    
    else:
        print("enter valid choice")

        
        
        
    
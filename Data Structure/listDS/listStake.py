class Stack:
    def __init__(self):
        self.items=[]
        
        
    def isEmpty(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)
        print(item,"pushed")
        
    def pop(self):
        if not self.isEmpty():
            i=self.items.pop()
            print(i,"item poped")
        else:
            print("steck is empty")
    
        
    def size(self):
        print(len(self.items))
        
    def display(self):
        print(self.items)
        
        
stk=Stack()
while True:
    choice=int(input("enter your choice\n 1 push\n 2 pop\n 3 display\n 4 size\n 5 Exit\n"))
    if choice==1:
        item=int(input("enter item"))
        stk.push(item)
    elif choice==2:
        stk.pop()
        
    elif choice==3:
        stk.display()
    
    elif choice==4:
        stk.size()
        
    elif choice==5:
        break

        
        
        
    
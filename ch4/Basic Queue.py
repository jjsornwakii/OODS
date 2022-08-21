class Queue():
    count = 0
    def __init__(self,items = None):
        items = []      ### ขาดบ่ได้
        self.items = items
        
    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

inp = input("Enter Input : ").split(',')

Q = Queue()

for i in inp:
    if i[0] == 'E':
        temp = i.strip("E ")
        Q.enQueue(temp)
        Q.count+=1
        print("Add",temp,"index is",Q.size()-1)

    elif i[0] == 'D':
        
        if Q.size()>0:
            temp = Q.deQueue()
            print("Pop",temp,"size in queue is",Q.size())
        
        else:
            Q.count=-1
            print(Q.count)
        


       
if not Q.isEmpty():
    print("Number in Queue is : ",Q.items)

else:
    print("Empty")

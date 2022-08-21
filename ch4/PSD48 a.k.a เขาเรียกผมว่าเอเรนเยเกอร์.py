class Queue():
    count = 0
    ESsize = 0
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

    def insert(self,val,index):
        q.items.insert(index, val)

    

inp = input("Enter Input : ").split(',')
q = Queue()

for i in inp:
    if 'ES' in i :
        temp = i.strip('ES ')
        q.items.insert(q.ESsize, temp)
        q.ESsize +=1

    elif 'EN' in i:
        temp = i.strip('EN ')
        
        q.enQueue(temp)

    elif 'D' in i:
        if q.size()>0:
            print(q.deQueue())
        else:
            print("Empty")


    
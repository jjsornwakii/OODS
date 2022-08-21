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

    def insert(self,val,index):
        q.items.insert(index, val)

q = Queue()
inp = input("Enter code,hint : ").split(',')

s = ord(inp[1])-ord(inp[0][0])

for i in inp[0]:
    q.enQueue(chr(ord(i)+s))
    print(q.items)


'''
for i in range(len(inp[0])-1,-1,-1):
    print(i)'''

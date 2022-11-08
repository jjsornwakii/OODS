class node:
    def __init__(self,data,next = None):
        self.data = data

        if next == None:
            self.next = None
        else:
            self.next = next

class list:

    def __init__(self):
        self.head = None

    def append(self,data):
        p = node(data)             
        
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            
            t.next = p

        

    



l = list()


print(" *** Locomotive ***")
inp = [int(n) for n in input("Enter Input : ").split()]

for i in inp:
    l.append(i)


print("Before : ",end='')
h = l.head

while h != None:
    if h is l.head:
        print(h.data,end='')
    else:
        print(" <-",
        h.data, end='')
    
    h = h.next

h = l.head
while h != None:
    if h.data == 0:
        h.data = l.head
    h = h.next


print("After : ",end='')
while h != None:
    if h is l.head:
        print(h.data,end='')
    else:
        print(" <-",
        h.data, end='')
    
    h = h.next



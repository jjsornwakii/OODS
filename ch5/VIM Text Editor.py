class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        #Code Here
        p = Node(item)

        if self.head == None:
            self.head = p

        else:
            t = self.head
            while t.next != None:
                t = t.next
            h = t
            t.next = p
            t = t.next
            t.previous = h
            self.tail = t


    def size(self):
        #Code Here
        h = self.head
        c = 0
        if h == None:
            return 0
        else:
            while h != None:
                c+=1
                h = h.next
            return c

    def insert(self, pos, item):
        #Code Here
        p = Node(item)
        t = self.head
        c = 0
        while c!=pos:
            c+=1
            t=t.next

        t1 = t
        t0 = t.previous
        
        if t0 != None:
            t0.next = p
            p.previous = t0
        
        else:
            l.head = p
            p.previous = None
            
        p.next = t1
        t1.previous = p
        


    def pop(self, pos):
        #Code Here
        h = self.head
        prev = None
        c = 0

        if pos < 0:
            pos = self.size()+pos
            
        if self.head != None and pos < self.size():
            while h != None and c < pos :
                prev = h
                h = h.next
                c+=1

            if prev == None:
                self.head = h.next
            else:
                prev.next = h.next

    def findIndex(self,val):
        
        t = self.head
        c = 0
        while t.value!= val:
            c+=1
            t=t.next
        return c


inp = input("Enter Input : ").split(',')
l = LinkedList()
l.append('|')
for i in range(len(inp)):
    if inp[i][:1]=='I':
        t = l.head
        while t.value != '|':
            t = t.next
        
        l.insert(l.findIndex('|'), inp[i][2:])
        

    elif inp[i][:1]=='L':
        t = l.head
        
        while t.value != '|':
            t = t.next

        t1 = t.previous
        t2 = t
        t3 = t.next

        h = None
        if t1 !=None:
            if t1.previous != None:
                h = t1.previous
            
            if h!=None:
                    h.next =  t2
                    t2.previous = h
                    t2.next = t1
                    t1.previous = t2

                    if t3 != None:
                        t3.previous = t1
                    t1.next = t3

            else:
                    l.head = t2
                    t2.previous = None
                    t2.next = t1
                    t1.previous = t2
                    t2.next = t1
                    
                    if t3 != None:
                        t3.previous = t1
                    t1.next = t3
            

                
    elif inp[i][:1]=='R':
        t = l.head

        while t.value != '|':
            t = t.next

        t0 = t.previous
        t1 = t
        t2 = t.next
        

        if t2 != None:

            if t0 == None:
                t3 = t2.next
                t2.previous = None
                t2.next = t1
                t1.previous = t2
                l.head = t2

                if t3 != None:
                    t3.previous = t1

                t1.next = t3
                    
            else:
                t3 = t2.next
                t0.next = t2
                t2.previous = t0
                t2.next = t1
                t1.previous = t2
                
                if t3 != None:
                    t3.previous = t1
                    t1.next = t3

                t1.next = t3

    elif inp[i][:1]=='B':
        t = l.head

        while t.value != '|':
            t = t.next
        
        t1 = t
        t0 = t1.previous
        t2 = t1.next

        if t0 != None:
            
            if t0.previous !=None:
                tp = t0.previous
                tp.next = t1
                t1.previous = tp
            
            else:
                l.head = t1
                t1.previous = None

    elif inp[i][:1]=='D':
        t = l.head

        while t.value != '|':
            t = t.next
        
        t1 = t
        t0 = t1.previous
        t2 = t1.next

        if t2 != None:

            if t2.next != None:
                tn = t2.next
                tn.previous = t1
                t1.next = tn

            else:
                t1.next = None
                l.tail = t1

p = l.head
while p != None:
    print(p.value,"",end='')
    p = p.next

print()
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

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


    def addHead(self, item):
        #Code Here
        p = Node(item)

        if self.head == None:
            self.tail = p
            self.head = p
        
        else:
            p.next = self.head
            h = self.head
            h.previous = p
            self.head = p
            
        h = self.head
        while h.next!=None:
            h=h.next
        self.tail = h

    def insert(self, pos, item):
        #Code Here
        p = Node(item)
        if pos < 0:
            pos = self.size()-1 + pos

            if pos > self.size()-1:
                pos = self.size()-1

        elif pos > self.size()-1:
            pos = self.size()-1

        h = self.head
        c = 0

        if pos == 0 or self.size()==0:
            self.addHead(item)

        elif pos == self.size()-1:
            p = Node(item)

            p.previous = self.tail
            h = p.previous
            h.next = p
            h = h.next
            self.tail = p
            h.next = None

        else:
            p = Node(item)
            
            h = self.head
            while h != None:
                if c == pos:
                    prev = h.previous
                    prev.next = p
                    p.previous = prev
                    h.previous = p
                    p.next = h
                    break
                c+=1
                h = h.next

        

    def search(self, item):
        #Code Here
        h = self.head
        while h.next != None:
            
            if int(h.value) == item:
                return str("Found ")
            h = h.next
        return str("Not Found ")


    def index(self, item):
        #Code Here
        h = self.head
        c = 0
        while h.next != None:
            if h.value == item:
                return c
            c+=1
            h = h.next
        return -1

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

    def pop(self, pos):
        #Code Here
        h = self.head
        prev = None
        c = 0

        if pos > self.size()-1:
            pos = self.size()-1
        
        if pos < 0:
            pos = self.size()-pos

        while h != None and c < pos :
            prev = h
            h = h.next
            c+=1

        if prev == None:
            self.head = h.next
        else:
            prev.next = h.next




L = LinkedList()
inp = input('Enter Input : ').split()

for i in inp:
    L.append(i)

h = L.head
while h != None:
    print(h.value,"",end="")
    h = h.next

L.insert(2,777)
print()
h = L.head
while h != None:
    print(h.value,"",end="")
    h = h.next

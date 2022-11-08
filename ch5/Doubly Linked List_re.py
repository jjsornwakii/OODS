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
        if pos < 0:
            pos = self.size() + pos

        h = self.head
        c = 0

        if pos <= 0 or self.size()==0 or self.head == None:
            self.addHead(item)

        elif pos >= self.size():
            p = Node(item)
            t = self.tail
            t.next = p
            p.previous = t
            p.next = None
            self.tail = p

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

    def index(self, item):
        #Code Here
        h = self.head
        c = 0
        while h != None:
            if h.value == item:
                return c
            c+=1
            h = h.next
        return -1

    def search(self, item):
        #Code Here
        h = self.head
        while h != None:
            
            if str(h.value) == str(item):
                return str("Found")
            h = h.next
        return str("Not Found")

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

            return "Success"
        else:
            return "Out of Range"
        

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
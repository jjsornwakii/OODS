class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class Linkedlist:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def append(self, item):
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

    def getMax(self):
        h = self.head
            
        max = 0
        while h != None:
            if h.value < 0:
                if max < h.value*-1:
                    max = h.value*-1
            else:
                if max < h.value:
                    max = h.value
            h = h.next
        return max

def getMaxDigit(n):
    if n <0:
        n = n *(-1)
    i = 0
    while n > 0 :
        n = n // 10
        i += 1
    return i

def getDigit(n,pos):
    if n <0:
        n = n *(-1)
    for i in range(pos-1):
        n = n // 10
    return n % 10

def radix_sort(l):


    h = l.head
    max_bit = getMaxDigit(l.getMax())
    indexList = [None,None,None,None,None,None,None,None,None,None]
    countRound = 0
    
    for i in range(1,max_bit+1):
        countRound+=1
        h = l.head
        
        while h != None:
            num = h.value
            index = getDigit(num, i)
        
            if indexList[index] == None:
                indexList[index]=h
                h = h.next
                l.head = h
                indexList[index].next = None
                
            else:
                temp = indexList[index]
                while temp.next != None:
                    temp = temp.next
                temp.next = h
                h = h.next
                temp = temp.next
                l.head = h
                temp.next = None
                
                
            h = l.head
            
        


        print("------------------------------------------------------------")
        print("Round :",countRound)
        for k in range(10):
            print(k,": ", end='')
            t = indexList[k]
            while t != None:
                if t.value != None:
                    print(t.value,"",end='')
                
                t = t.next
            print()
        
        ### ต่อสาย
        first = True
        tempLinkedList = Linkedlist()
        for j in range(10):
            t = indexList[j]
            if t != None:

                if first:
                    tempLinkedList.head = t
                    first = False
                else:
                    temp = tempLinkedList.head
                    while temp.next != None:
                        ###print("T:",temp.value)
                        temp = temp.next
                    temp.next = t
                    temp = temp.next
                    while temp.next != None:
                        ###print("T:",temp.value)
                        temp = temp.next
                    temp.next = None
                    
            h = tempLinkedList.head      
            l.head = tempLinkedList.head

        for g in range(10):
            indexList[g] = None
        h = tempLinkedList.head            
        
    return h,countRound
        
inp = [int(i) for i in input("Enter Input : ").split()]
L = Linkedlist()
for i in inp:
    L.append(i)

beforeSorted = "Before Radix Sort : "
first = True
h = L.head
while h != None:
    if first:
        beforeSorted += str(h.value)
        first = False
    else: 
        beforeSorted += " -> "+str(h.value)
    h = h.next

h,c = radix_sort(L)

print("------------------------------------------------------------")
print(c,"Time(s)")
print(beforeSorted)
first = True
print("After  Radix Sort : ",end='')
while h != None:
    if first:
        print(h.value,end='')
        first = False
    else:
        print(" -> "+str(h.value),end='')
    h = h.next








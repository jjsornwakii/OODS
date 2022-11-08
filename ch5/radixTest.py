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
            t.next = None
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
    
    max_bit = getMaxDigit(l.getMax())
    indexList = [None,None,None,None,None,None,None,None,None,None]
    countRound = 0


    for i in range(1,max_bit+1):
        countRound+=1
        ##############################
        #list บวก
        h = l.head
        pos = Linkedlist()
        while h != None:
            if h.value >= 0:
                pos.append(h.value)
            h = h.next

        # list ลบ
        h = l.head
        neg = Linkedlist()
        while h != None:
            if h.value < 0:
                neg.append(h.value)
            h = h.next
        

        temp1 = neg.head 
        temp2 = pos.head 
        
        ##############################
        
        while temp1 != None:
            
            index = getDigit(temp1.value, i)
            
            if indexList[index] == None:
                indexList[index] = temp1
                indexList[index].head = indexList[index]
                indexList[index].previous = None
                temp1 = temp1.next
                indexList[index].next = None
                indexList[index].tail = indexList[index]
                
            else:
                
                t = indexList[index]
                
                while t.next != None:
                    t = t.next
                c = t
                t.next = temp1
                temp1 = temp1.next
                t = t.next
                t.previous = c
                indexList[index].tail = t
                t.next = None

        ### Back up
        tempPos = Linkedlist()
        tempNeg = Linkedlist()

        for j in range(9,-1,-1):
            t = indexList[j]
            if t!=None:
                
                while t != None:
                    if t.value < 0:
                        tempNeg.append(t.value)
                    t = t.next

        
        

        while temp2 != None:
            
            index = getDigit(temp2.value, i)
            
            if indexList[index] == None:
                indexList[index] = temp2
                temp2 = temp2.next
                indexList[index].next = None
                
            else:
                
                t = indexList[index]
                
                while t.next != None:
                    t = t.next
                
                c = t
                t.next = temp2
                temp2 = temp2.next
                t = t.next
                t.previous = c
                t.next = None

        
        for j in range(10):
            t = indexList[j]
            if t!= None:
                
                
                while t != None:
                    if t.value >= 0:
                        tempPos.append(t.value)
                    t=t.next

        ##### print ออกมาดู



        ##########  
        
        
        
        print("------------------------------------------------------------")
        
        print("Round :",countRound)
        for j in range(10):
            print(j,": ",end='')
            t = indexList[j]
            while t != None:
                
                print(t.value,"",end='')
                t = t.next
                
            print()

        ### ต่อ Linked List ของแต่ละ indexLinkList เข้าด้วยกัน

        

        mainTemp = Linkedlist()
        t = tempNeg.head
        while t!=None:
            mainTemp.append(t.value)
            t=t.next

        t = tempPos.head
        while t!=None:
            
            mainTemp.append(t.value)
            t=t.next
        

        l.head = mainTemp.head
        indexList = [None,None,None,None,None,None,None,None,None,None]
    return l.head,countRound

    
        
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








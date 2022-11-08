
class node:
    def __init__(self,data,next = None ):
        self.data = data
        if next == None:
            self.next = None

        else:
            self.next = next
        ### Code Here ###

    def __str__(self):
        ### Code Here ###
        return True

def createList(l=[]):
    ### Code Here ###
    head = None
    for i in range(len(l)):
        p = node(l[i])
        if head == None:
            head = p
            head.next = None
        else:
            t = head
            while t.next != None:
                t = t.next
            t.next = p
            t=t.next
            t.next = None

    return head

def printList(H):
    ### Code Here ###
    t = H
    while t != None:
        print(t.data,"",end='')
        t = t.next
    print()

def mergeOrderesList(p,q):
    ### Code Here ###
    temp1 = p
    temp2 = q

    while temp1.next != None:
        temp1=temp1.next
    temp1.next = temp2


    #### Sorting ####
    cur = p
    index = None
    if p == None:
        return p
    else:
        while cur != None:
            index = cur.next
            while index != None:
                if cur.data > index.data:
                    temp = cur.data
                    cur.data = index.data
                    index.data = temp
                index = index.next
            cur = cur.next

    return p
    

#################### FIX comand ####################   
# input only a number save in L1,L2
inp = [str(x) for x in input("Enter 2 Lists : ").split() ]
L1 = [int(i) for i in inp[0].split(",")]
L2 = [int(i) for i in inp[1].split(",")]

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)
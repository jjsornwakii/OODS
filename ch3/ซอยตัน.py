class Stack:

    def __init__(self,items = None):
        items = []
        self.items = items

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
Soi1 = Stack()
Soi2 = Stack()
depComp = False
depDontHave = False
depEmpty = False
arrComp = False
arrFull = False
arrAlr = False

S = s.split(',')

m,n = int(m),int(n)

for i in S:
    if(Soi1.size() < m):
        if i != '0':
            Soi1.push(int(i))
        else:
            depEmpty = True
        
if o == 'arrive':
    if(Soi1.size() < m):
        if n not in Soi1.items:
            Soi1.push(n)
            arrComp = True

        else:
            arrAlr = True
    
    else:
        arrFull = True

elif o == 'depart':
    while not Soi1.isEmpty():
        temp = Soi1.pop()
        if temp != n:
            Soi2.push(temp)

        else:
            depComp = True
            break

        depDontHave = True
        depComp = False
    
    while not Soi2.isEmpty():
        Soi1.push(Soi2.pop())

if o == 'arrive':
    if arrComp:
        print("car",n,"arrive! : Add Car",n)

    elif arrFull:
        print("car",n,"cannot arrive : Soi Full")

    else:
        print("car",n,"already in soi")

elif o == 'depart':

    if depEmpty:
        print("car",n,"cannot depart : Soi Empty")

    elif depComp:
        print("car",n,"depart ! : Car",n,"was remove")

    elif depDontHave:
        print("car",n,"cannot depart : Dont Have Car",n)



print(Soi1.items)

### Enter Your Code Here ###
class Stack():
    def __init__(self, items=None):
        items = []
        self.items = items

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


inp = input('Enter Input : ').split()

S = Stack()
checkCon = True
count = 0
combo = 0
loop = True
temp = None

while loop == True:
    
    tempList = inp
    for i in inp:
        
        S.push(i)
        if checkCon == True :
            if temp != i:
                
                count = 1
                temp = i
                

            elif temp == i:
                
                count += 1

            if count == 3:
                combo+=1
                count = 0
                
                S.pop()
                S.pop()
                S.pop()
                
                temp = None
                checkCon = False

    inp = []
    
    checkCon = True
    for j in S.items:
        inp.append(j)

    

    if inp == tempList:
        loop = False

    else:
        S.items = []
    

print(S.size())

if S.isEmpty():
    print("Empty")

while not S.isEmpty():
    print(S.pop(), end='')
    if S.size() == 0 :
        print()


if combo >1:  
        print("Combo :",combo,"! ! !")


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

Act = ['Eat','Game','Learn','Movie']
Loc = ['Res.','ClassR.','SuperM.','Home']

inp = input("Enter Input : ").split(',')
inp3 = []
inp4 = []
lis3 = []
lis4 = []
score = 0
myQ = Queue()
yourQ = Queue()
inp2 = None
for i in inp:
    inp2 = (i.split(' '))
    myQ.enQueue(inp2[0])
    yourQ.enQueue(inp2[1])

print("My   Queue = ",end='')
for i in range(len(myQ.items)):
    print(myQ.items[i],end='')
    if i != len(myQ.items)-1:
        print(", ",end='')
print()
print("Your Queue = ",end='')
for i in range(len(yourQ.items)):
    print(yourQ.items[i],end='')
    if i != len(yourQ.items)-1:
        print(", ",end='')
print()

print("My   Activity:Location = ",end='')
for i in range(len(myQ.items)):
    inp3 = list(map(int,myQ.items[i].split(':')))
    lis3.append(inp3[0])
    lis3.append(inp3[1])
    print(Act[inp3[0]]+":"+Loc[inp3[1]],end='')
    if i != len(myQ.items)-1:
        print(", ",end='')
print()
print("Your Activity:Location = ",end='')
for i in range(len(yourQ.items)):
    inp4 = list(map(int,yourQ.items[i].split(':')))
    lis4.append(inp4[0])
    lis4.append(inp4[1])
    print(Act[inp4[0]]+":"+Loc[inp4[1]],end='')
    if i != len(yourQ.items)-1:
        print(", ",end='')

for i in range(0,len(lis3),2):
    
    if lis3[i] == lis4[i] and lis3[i+1] == lis4[i+1]:
        score+=4
    elif lis3[i] != lis4[i] and lis3[i+1] == lis4[i+1]:
        score+=2
    elif lis3[i] == lis4[i] and lis3[i+1] != lis4[i+1]:
        score+=1
    else:
        score-=5
print()
if score >=7:
    print("Yes! You're my love! : ",end='')

elif score >0:
    print("Umm.. It's complicated relationship! : ",end='')

else:
    print("No! We're just friends. : ",end='')

print("Score is",str(score)+".")

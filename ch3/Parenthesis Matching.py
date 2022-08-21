class Stack():
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

lis = input("Enter expresion : ")
stack = Stack()
remain_close = False
pair = {'(' : ')' , '[' : ']' , '{' : '}'}
for i in lis:
    
    if i in '[{(':
        stack.push(i)
    
    elif i in ']})' and not stack.isEmpty():
        temp = stack.pop()
        
        if pair[temp] != i:
            print(lis,"Unmatch open-close")
            exit()

    elif i in ']})' and stack.isEmpty():
        remain_close = True

if not stack.isEmpty()and remain_close == False:
    print(lis,"open paren excess  ",stack.size(),":","("*stack.size())

elif remain_close:
    print(lis,"close paren excess")

else:
    print(lis, "MATCH")
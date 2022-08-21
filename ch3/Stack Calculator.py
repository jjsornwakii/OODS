class StackCalc():

    def __init__(self,items = None):
        items = []
        self.items = items
        self.val = 0

    def getValue(self):
        if len(self.items)>0:
            return int(self.items[len(self.items)-1])
        else:
            return 0

    def peek(self):
        return self.items[-1]

    def run(self,instructions):
        self.items = []
        for i in instructions:
            
            if i == '+':
                self.val = int(self.items.pop()) + int(self.items.pop())
                self.items.append(self.val)

            elif i == '-':
                self.val = int(self.items.pop()) - int(self.items.pop())
                self.items.append(self.val)

            elif i == '*':
                self.val = int(self.items.pop()) * int(self.items.pop())
                self.items.append(self.val)

            elif i == '/':
                self.val = int(self.items.pop()) / int(self.items.pop())
                self.items.append(self.val)

            elif i == 'DUP':
                self.items.append(self.items[-1])

            elif i == 'POP':
                self.items.pop()

            elif i == 'PSH':
                self.items.append(self.items.peek())

            elif i.isnumeric():
                self.items.append(i)

            else:
                print("Invalid instruction:",i)
                exit()

            
    
print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()

machine.run(arg)
print(machine.getValue())
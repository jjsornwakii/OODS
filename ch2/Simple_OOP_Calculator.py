class Calculator :

    ### Enter Your Code Here ###
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self):
        return self.x + self.y
        ###Enter Your Code For Add Number###

    def __sub__(self):
        return self.x - self.y
        ###Enter Your Code For Sub Number### 

    def __mul__(self):
        return self.x * self.y
        ###Enter Your Code For Mul Number###

    def __truediv__(self):
        return self.x / self.y
        ###Enter Your Code For Div Number###

x,y = input("Enter num1 num2 : ").split(",")

c = Calculator(int(x),int(y))

print(c.__add__(),c.__sub__(),c.__mul__(),c.__truediv__(),sep = "\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class AVL:

    def __init__(self):
        self.root = None

    def insert(self,node,data):
        if node == None:
            return Node(data)
        
        if data < node.data:
            node.left = self.insert(node.left,data)
            
        if data >= node.data:
            node.right = self.insert(node.right,data)
            
        balance = self.height(node.left) - self.height(node.right)
        print(balance)
        if balance > 1 and data < node.left.data: #left left
            return self.rightRotate(node)
        
        elif balance < -1 and data >= node.right.data: #right right
            return self.leftRotate(node)
        
        elif balance >= 1 and data >= node.left.data: #left right
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        
        elif balance <= -1 and data < node.right.data: #right left
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        
    
        
        
        return node

    def height(self,node):
        
        if node == None:
            return 0
        
        height_left = self.height(node.left)
        height_right = self.height(node.right)
        
        if height_left > height_right:
            return height_left + 1
        else:
            return height_right + 1

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y
 
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        return y
    
    def inorder_cv(self,root):
        if root!=None:
            self.inorder_cv(root.right)
            
            
            t1 = root.left
            t2 = root.right
            if t1 == None and t2 != None :
                root.right.data -= t2.data
            elif t1 != None and t2 == None:
                root.left.data -= t1.data
            
            elif t1 != None and t2 != None :
                min = 0
                if t1.data >= t2.data:
                    min = t2.data
                else:
                    min = t1.data
                    
                root.right.data -= min
                root.left.data -= min
            
            self.inorder_cv(root.left)
                
            
    def sumTree(self,root):
        if (root == None):
            return 0
        return (root.data + self.sumTree(root.left) + self.sumTree(root.right))
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            
            self.inorder(root.right)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

avl = AVL()
inp = (input("Enter Input : ").split("/"))
inp[0] = int(inp[0])
inp[1] = list(map(int,inp[1].split()))
inp[1] = inp[1]

if int(inp[0]/2+1) == int(len(inp[1]) ) and  inp[0]>=3:
    

    for i in inp[1]:
        avl.root = avl.insert(avl.root, i)
    
    sum = avl.sumTree(avl.root)
    
    avl.inorder(avl.root)
    ### ทำปีกซ้าย
    avl.inorder_cv(avl.root.left)
    ### ทำปีกขวา
    avl.inorder_cv(avl.root.right)
    ### ทำ root
    r = avl.root
    
    if r.left.data > r.right.data:
        r.left.data -= r.right.data
        r.right.data = 0
    else:
        r.right.data -= r.left.data
        r.left.data = 0
    
    avl.inorder(avl.root)
    
    print(avl.sumTree(avl.root))
        
else:
    print("Incorrect Input")
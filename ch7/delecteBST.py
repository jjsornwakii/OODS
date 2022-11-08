class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None
        
    

    def insert(self, data):
        # Code Here
        p = Node(data)
        print("insert",i[2:])
        if self.root is None:
            self.root = Node(data)
            
        else:
            self.insertWithNode(self.root, data)
        
        
        return self.root
    
    def insertWithNode(self,root,data):
        if root.left is None and root.right is None:#external node
            if data > root.data:
                newNode = Node(data)
                root.right = newNode
                
            else:
                newNode = Node(data)
                root.left = newNode
                
        else: #not external
            if data > root.data:
                if root.right is not None:
                    self.insertWithNode(root.right, data)
                else: #if empty node
                    newNode = Node(data)
                    root.right = newNode
                    
            else:
                if root.left is not None:
                    self.insertWithNode(root.left, data)
                else:
                    newNode = Node(data)
                    root.left = newNode
        
        
    def delete(self,root, data):
        #code here
        
        if root is None:
            print("delete",data)
            print("Error! Not Found DATA")
            return root
        
        
        
        # เข้าไป left subtree 
        if data < root.data:
            
            root.left = self.delete(root.left, data)
            return root
            
        # เข้าไป right subtree
        elif(data > root.data):
            root.right = self.delete(root.right, data)
            return root
        
        print("delete",data)
        
        # ถ้าไม่มีใบเลย
        if root.left is None and root.right is None:
            
            if root.data == self.root.data:
                self.root = None
            
            return None

        # ถ้ามีใบซักหนึ่งใบ
        if root.left is None:
            
            if root.data == self.root.data:
                self.root = root.right
            
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            
            if root.data == self.root.data:
                self.root = root.left
            
            temp = root.left
            root = None
            return temp
        
        
        
        # ถ้ามีทั้งสองใบ
        succParent = root
        
        # หาnode สืบทอด
        succ = root.right 
        
        while succ.left != None:
            succParent = succ
            succ = succ.left
            
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
            
        
        root.data = succ.data
                
        return root
        

    def minValueNode(node):
        current = node
    
        # loop หา node ซ้ายสุด
        while(current.left is not None):
            current = current.left
    
        return current
        
def inorder(root):
    if root is not None:
        inorder(root.left)
        inorder(root.right)  
              
              
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
#code here
for i in data:
    
    if i[0] == 'i':
        tree.insert(i[2:])
        printTree90(tree.root)
        
    elif i[0] == 'd':
        n = tree.delete(tree.root,i[2:])
        
        inorder(n)
        printTree90(tree.root)
        
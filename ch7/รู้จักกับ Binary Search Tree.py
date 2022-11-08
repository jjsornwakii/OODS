class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        p = Node(data)
        
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
                     
                
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
    

T.printTree(root)
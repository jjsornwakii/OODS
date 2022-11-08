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
        
        if self.root == None:
            self.root = Node(data)
            
        else:
            cur = self.root
            
            while True:
                
                if data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left
                        
                elif data > cur.data:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
                else:
                    break
                
        return self.root
    
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
BST = BinarySearchTree()

inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    BST.insert(i)
    
BST.printTree(BST.root)

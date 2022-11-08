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

    def insert(self, val):  
        
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
        return self.root

    def delete(self,r, data):
        
        if self.root.left == None and self.root.right == None and self.root.data == data:
            self.root = None
        elif self.root.left == None and self.root.data == data:
            self.root = self.root.right
        elif self.root.right == None and self.root.data == data:
            self.root = self.root.left

        if r is None:
            print("Error! Not Found DATA")
            return
        if r.data != data:
            if r.data > data:
                r.left = self.delete(r.left,data)
            else:
                r.right = self.delete(r.right,data)
        else:
            if r.left is None: #1child with left none
                r = r.right
                return r
            elif r.right is None: #1child with right none
                r = r.left
                return r
            else: 
                cur = r.right #inorder successor
                while cur.left != None: 
                    cur = cur.left 
                r.data = cur.data
                r.right = self.delete(r.right,cur.data) 
        return r

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
    command = i.split(" ")
    if command[0] == 'i':
        print("insert "+(command[1]))
        tree.insert(int(command[1]))
        printTree90(tree.root)
    elif command[0] == 'd':
        print("delete "+(command[1]))
        tree.delete(tree.root,int(command[1]))
        printTree90(tree.root)
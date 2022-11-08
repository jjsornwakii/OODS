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
                     
    def checkpos(self,root,pos):
        
        # หาเลข pos ว่าอยู่ไหน
        
        if root == None:
            return root
        
        # เข้าไป left subtree 
        if pos < root.data:
            root.left = self.checkpos(root.left, pos)
            
        # เข้าไป right subtree
        elif(pos > root.data):
            root.right = self.checkpos(root.right, pos)
            
        # จนเจอ
        c = 0
        if(pos == root.data):
            cl = True
            cr = True
            if pos != self.root.data:
            
                if root.left is None:
                    cl = False
                    
                if root.right is None:
                    cr = False
                    
                if cr or cl : 
                    c = 1
                    #print("Inner")
            
                else:
                    c = 2
                    #print("Leaf")
                
            else:
                c =3
                #print("Root")
            
        if c == 0:
            print("Not exist")
        elif c == 1:
            print("Inner")
        elif c == 2:
            print("Leaf")
        else:
            print("Root")
        
        exit()
            
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(T.root,inp[0])
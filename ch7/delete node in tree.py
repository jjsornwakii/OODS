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
        if self.root == None:
            self.root = Node(val)
        else:
            cur = self.root
            while True:
                if val < cur.data:
                    if cur.left == None:
                        cur.left = Node(val)
                        break
                    else:
                        cur = cur.left
                elif val > cur.data:
                    if cur.right == None:
                        cur.right = Node(val)
                        break
                    else:
                        cur = cur.right
                else:
                    break
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
        print("insert",i[2:])
        tree.insert(i[2:])
        printTree90(tree.root)
        
    elif i[0] == 'd':
        print("delete "+(i[2:]))
        n = tree.delete(tree.root,i[2:])
        
        printTree90(tree.root)
        
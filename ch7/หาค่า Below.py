class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    
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
            
            
def find_less_than(root, max, l=None):
    if l == None:
        l = []
    if root.left:
        find_less_than(root.left, max, l)
    if root.data < max:
        l.append(root.data)
    if root.right:
      find_less_than(root.right, max, l)
    return l

T = BST()
inp = input('Enter Input : ').split('|')
inp1 = [int(i) for i in inp[0].split()]
inp2 = int(inp[1])

for i in inp1:
    root = T.insert(i)
T.printTree(root)

print("--------------------------------------------------")
l = find_less_than(root, inp2)
print('Below',inp2,': ',end='')
if len(l) != 0:
    print(*l)

else:
    print("Not have")
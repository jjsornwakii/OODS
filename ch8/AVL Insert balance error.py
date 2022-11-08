class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVL:
    
    def __init__(self): 
        self.root = None

    def insert(self, root, key):
     
        # ทำ BST ปกติ
        if root == None:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        # อัพเดทความสูงของ Node บรรพบุรุษ
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
 
        # เช็คว่า Balance ไหม
        balance = self.getBalance(root)
 
        # ถ้า Tree ไม่ Balance เช็ค Case
        # Case 1 - Left Left
        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # หมุน
        y.left = z
        z.right = T2

        # อัพเดทความสูง
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
 
        # คืนค่า root 
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # หมุน
        y.right = z
        z.left = T3
 
        # อัพเดทความสูง
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
 
        # คืนค่า root 
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

 
    
inp = [int (x) for x in input('Enter Input : ').split()]
tree = AVL()

for i in inp:
    tree.root = tree.insert(tree.root, i)
    print('Insert : (',i,')')
    tree.printTree(tree.root)
    print('--------------------------------------------------')
    
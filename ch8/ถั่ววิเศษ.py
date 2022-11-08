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
        t = ''
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                ### ถ้าลูก น้อยกว่าพ่อ ไปกิ่งซ่าย
                if data < cur.data:
                    t = str(t)+'L'
                    if cur.left == None:
                        cur.left = Node(data)
                        
                        break
                    else:
                        ### ถ้ากิ่งไม่ว่าง ก็ไปซ้ายเลื่อยๆ
                        cur = cur.left
                    
                ### ถ้าลูก มากกว่าพ่อ ไปกิ่งขวา
                elif data > cur.data:
                    t = str(t)+'R'
                    if cur.right == None:
                        cur.right = Node(data)
                        
                        break
                    else:
                        ### ถ้ากิ่งไม่ว่าง ก็ไปขวาเลื่อยๆ
                        cur = cur.right
                    
                else:
                    break
        t = str(t) + '*'
        print(t)
        return self.root
    
    def show(self,node, level = 0):
        if node != None:
            self.show(node.right, level + 1)
            print('     ' * level, node)
            self.show(node.left, level + 1)


inp = [int (x) for x in input('Enter Input : ').split()]

BTS = BinarySearchTree()

for i in inp:
    BTS.insert(i)


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key 

def insertBst(root, key): 
    if root is None:
        return Node(key)
    
    else :
        if root.key == key :
            return root 
        elif root.key < key :
            root.right = insertBst(root.right, key)
        elif root.key > key :
            root.left = insertBst(root.left, key)
    return root  

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)       

def minValueNode(root):
    temp = root
    while(temp.left != None):
        temp = temp.left
    return temp

def deleteBst(r, key):
    if r is None:
        return r
    if r.key > key :
        r.left=deleteBst(r.left, key)
    elif r.key < key :
        r.right = deleteBst(r.right, key)
    else: 
        if r.right and r.left is None:
            return None
        elif r.left is None:
            temp = r.right 
            r = None
            return temp
        elif r.right is None:
            temp = r.left 
            r = None
            return temp
        
        temp = minValueNode(r.right)
        r.key = temp.key 
    return r 
            
        
        
        

r= Node(50)
insertBst(r,30)
insertBst(r,20)
insertBst(r,40)
insertBst(r,60)
insertBst(r,70)
insertBst(r,80)
inorder(r)
deleteBst(r,40)
print(' ')
inorder(r)


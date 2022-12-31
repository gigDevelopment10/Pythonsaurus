# Insert operation in a Binary Search Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key= key

def insertBST(root, key):
    if root is None:
        return Node(key)
    
    else:
        if root.key == key :
            return root 
        elif root.key < key:
            root.right = insertBST(root.right, key)
        elif root.key > key:
            root.left = insertBST(root.left, key)
      
    return root           
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,  end =" ")
        inorder(root.right)
       
#driver code 
r = Node(50)
r = insertBST(r, 30)
r = insertBST(r, 20)
r = insertBST(r, 40)
r = insertBST(r, 70)
r = insertBST(r, 60)
r = insertBST(r, 80)

# print 
inorder(r)
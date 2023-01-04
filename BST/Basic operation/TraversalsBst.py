class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key 
        
def insertBST(root,key):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root
        elif root.key < key:
            root.right = insertBST(root.right, key)
        elif root.key > key:
            root.left = insertBST(root.left, key)
    return root

def inorder(root):
    #
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

def postorder(root):
    #LRN
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')
        
def preorder(root):
    #NLR
    if root:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)
        
r = Node(7)
insertBST(r,2)
insertBST(r,9)
insertBST(r,0)
insertBST(r,4)
inorder(r)
print(' ')
postorder(r)
print(' ')
preorder(r)
            
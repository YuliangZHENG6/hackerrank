# python 3

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

##### METHOD 1
def checkBST(root):
    return checkInorder(root, [-1])
    

def checkInorder(root, prev):
    result = True
    if root.left:
        result &= checkInorder(root.left, prev)
    if prev[0] >= root.data:
        return False
    prev[0] = root.data
    if root.right:
        result &= checkInorder(root.right, prev)
    return result
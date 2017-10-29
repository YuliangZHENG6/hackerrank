# python 3

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    return checkBST(root, -1, 10000)

def checkBST(root, min, max):
    if not root:
        return True
    if root.data <= min or root.data >= max:
        return False
    return checkBST(root.left, min, root.data) and checkBST(root.right, root.data, max)
    


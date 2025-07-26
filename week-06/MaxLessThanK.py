class Tree:
  #constructor
  def __init__(self, initval=None):
    self.value = initval
    if self.value:
      self.left = Tree()
      self.right = Tree()
    else:
      self.left = self.right = None
    return
  
  #Only empty node has value None
  def isempty(self):
    return(self.value == None)
  
  #Leaf nodes have both children empty
  def isleaf(self):
    return(self.value != None and self.left.isempty() and self.right.isempty())
  
#insert element to BST
def insertToBST(root, x):
  # Tree should have atleast one element.
  temp = root
  while (not temp.isempty()):
    if (x < temp.value):
      temp = temp.left
    else:
      temp = temp.right

  temp.value = x
  temp.left = Tree()
  temp.right = Tree()

def isLeaf(node:Tree):
    return node.value==None 

def maxLessThan(root, K):
    # print(K)
    smallest:bool = True
    temp=root
    val=None
    while(not isLeaf(temp)):
        # print(f"temp value={temp.value}, & K={K}")
        prev=temp
        if (temp.value and temp.value == K):
            return K
        elif (K <= temp.value):
            # print(f"going Left of : {temp.value}")
            temp = temp.left
        else:
            # print(f"going Right of : {temp.value}")
            val=temp.value
            temp = temp.right
            
            smallest = False

    if (smallest):
      return val
    return val
class AVLTree:
    # Constructor:
    def __init__(self,initval=None):
        self.value = initval
        if self.value:
            self.left = AVLTree()
            self.right = AVLTree()
            self.height = 1
        else:
            self.left = None
            self.right = None
            self.height = 0
        return

    def isempty(self):
        return (self.value == None)

    def isleaf(self):
        return (self.value != None and self.left.isempty() and self.right.isempty())

    def leftrotate(self):
        v = self.value
        vr = self.right.value
        tl = self.left
        trl = self.right.left
        trr = self.right.right
        newleft = AVLTree(v)
        newleft.left = tl
        newleft.right = trl
        self.value = vr
        self.right = trr
        self.left = newleft
        return
    def rightrotate(self):
        v = self.value
        vl = self.left.value
        tll = self.left.left
        tlr = self.left.right
        tr = self.right
        newright = AVLTree(v)
        newright.left = tlr
        newright.right = tr
        self.right = newright
        self.value = vl
        self.left = tll
        return

    def insert(self,val:int):

        if self.isempty():
            self.value=val
            self.left=AVLTree()
            self.right=AVLTree()

        else:
            temp = self
            prev = temp

            while(temp.value is not None):
                # temp.height+=1
                prev=temp
                if temp.value>val:
                    temp=temp.left

                else:
                    temp=temp.right
            temp.value=int(val)
            temp.left=AVLTree()
            temp.right=AVLTree()
            # leftrotate()




    def inorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.inorder()+ [self.value]+ self.right.inorder())
    def preorder(self):
        if self.isempty():
            return([])
        else:
            return([self.value] + self.left.preorder()+  self.right.preorder())
    def postorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.postorder()+ self.right.postorder() + [self.value])

A = AVLTree()
nodes = eval(input())
for i in nodes:
    A.insert(i)

print(A.inorder())
print(A.preorder())
print(A.postorder())

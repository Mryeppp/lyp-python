#BiTree
class BiTreeNode():
    def __init__(self,data=None,lchild=None,rchild=None) -> None:
        self.data =data;
        self.lchild = lchild
        self.rchild = rchild
class BiTree():
    def __init__(self,root=None) -> None:
        self.root = root 
    def createBiTree(self,root) -> None:
        data = input("->")
        if data == "#":
            root = None
        else:
            root.data = data
            root.lchild=BiTreeNode()
            self.createBiTree(root.lchild)
            root.rchild=BiTreeNode()
            self.createBiTree(root.rchild)
    def preOrder(self,root):
        if root is not None:
            self.VisitBTNode(root)
            self.preOrder(root.lchild)
            self.preOrder(root.rchild)
    def inOrder(self,root):
        if root is not None:
            self.inOrder(root.lchild)
            self.VisitBTNode(root)
            self.inOrder(root.rchild)
    def postOrder(self,root):
        if root is not None:
            self.postOrder(root.lchild)
            self.postOrder(root.rchild)
            self.VisitBTNode(root)
    def VisitBTNode(self,BiTreeNode):
        if BiTreeNode.data is not None:
            print(BiTreeNode.data,end=" ")
            
    def order(self,root):
        pass
        
            

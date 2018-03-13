# create by fanfan on 2018/3/12 0012
# 后续遍历
class TreeNode(object):
    def __init__(self,val=-1):
        self.val = val
        self.right = None
        self.left = None


class Tree(object):
    def __init__(self):
        self.root = TreeNode()
        self.myQueue = []

    def add(self,elem):
        node = TreeNode(elem)
        if self.root.val == -1:
            self.root =  node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.left == None:
                treeNode.left =node
                self.myQueue.append(treeNode.left)
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)

    def front_digui(self,root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print(root.val,end=' ')
        self.front_digui(root.left)
        self.front_digui(root.right)

    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.left)
        print(root.val,end=' ')
        self.middle_digui(root.right)

    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return

        self.later_digui(root.left)
        self.later_digui(root.right)
        print(root.val,end=' ')

    def front_stack(self,root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                print(node.val,end=' ')
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            node = node.right

    def middle_stack(self,root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            print(node.val,end=' ')
            node = node.right

    def later_stack(self,root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack = []
        myStack_output = []
        node = root
        myStack.append(node)
        while myStack:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack.pop()
            if node.left:
                myStack.append(node.left)
            if node.right:
                myStack.append(node.right)
            myStack_output.append(node)

        while myStack_output:  # 将myStack2中的元素出栈，即为后序遍历次序
            print(myStack_output.pop().val,end=" ")

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.val,end=" ")
            if node.left != None:
                myQueue.append(node.left)
            if node.right != None:
                myQueue.append(node.right)




if __name__ == '__main__':
    elems = range(10)
    tree = Tree()
    for elem in elems:
        tree.add(elem)
    print("前序遍历_递归")
    tree.front_digui(tree.root)
    print("\n中序遍历_递归")
    tree.middle_digui(tree.root)
    print("\n后序遍历_递归")
    tree.later_digui(tree.root)

    print("\n前序遍历_非递归")
    tree.front_stack(tree.root)
    print("\n中序遍历_非递归")
    tree.middle_stack(tree.root)
    print("\n后序遍历_非递归")
    tree.later_stack(tree.root)

    print("\n层次遍历")
    tree.level_queue(tree.root)
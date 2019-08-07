class Node:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current_node, val):
        if val <= current_node.val:
            if current_node.lchild:
                self.insertNode(current_node.lchild, val)
            else:
                current_node.lchild = Node(val)
        else:
            if current_node.rchild:
                self.insertNode(current_node.rchild, val)
            else:
                current_node.rchild = Node(val)

    def find(self, val):
        if self.root is None:
            return False
        else:
            return self.findNode(self.root, val)

    def findNode(self, current_node, val):
        if current_node is None:
            return False
        elif val == current_node.val:
            return True
        elif val < current_node.val:
            return self.findNode(current_node.lchild, val)
        else:
            return self.findNode(current_node.rchild, val)

    def findMinValue(self):
        if (self.root is None):
            return 0
        current_node = self.root
        while current_node.lchild is not None:
            current_node = current_node.lchild
        return current_node.val

    def findMaxValue(self):
        if self.root is None:
            return 0
        current_node = self.root
        while current_node.rchild is not None:
            current_node = current_node.rchild
        return current_node.val

    def in_order(self):
        if self.root is None:
            return
        self.in_order_node(self.root)

    def in_order_node(self, current_node):
        if current_node.val is None:
            return
        if current_node.lchild is not None:
            self.in_order_node(current_node.lchild)
        print(current_node.val)
        if current_node.rchild is not None:
            self.in_order_node(current_node.rchild)

    def pre_order(self):
        if self.root is None:
            return
        self.pre_order_node(self.root)

    def pre_order_node(self, current_node):
        if current_node.val is None:
            return
        print(current_node.val)
        if current_node.lchild is not None:
            self.pre_order_node(current_node.lchild)
        if current_node.rchild is not None:
            self.pre_order_node(current_node.rchild)

    def post_order(self):
        if self.root is None:
            return
        self.post_order_node(self.root)

    def post_order_node(self, current_node):
        if current_node.val is None:
            return
        if current_node.lchild is not None:
            self.post_order_node(current_node.lchild)
        if current_node.rchild is not None:
            self.post_order_node(current_node.rchild)
        print(current_node.val)

    def delete(self, val):
        if self.root is None:
            print("Binary search tree is empty. delete not possible")
        self.delete_node(self.root, val)

    def delete_node(self, current_node, key):
        if current_node.val is None:
            return
        # Find the node in the left subtree	if key value is less than root value
        if current_node.val > key:
            current_node.lchild = self.delete_node(current_node.lchild, key)
        # Find the node in right subtree if key value is greater than root value,
        elif current_node.val < key:
            current_node.rchild = self.delete_node(current_node.rchild, key)
        # Delete the node if root.value == key
        else:
            # deletion node is leaf node
            if not current_node.rchild and not current_node.lchild:
                return None
            # If there is no right children delete the node and new root would be root.left
            if not current_node.rchild:
                return current_node.lchild
            # If there is no left children delete the node and new root would be root.right
            if not current_node.lchild:
                return current_node.rchild
            # If both left and right children exist in the node replace its value with
            # the minmimum value in the right subtree. Now delete that minimum node
            # in the right subtree
            tmp_node = current_node.rchild
            min_val = tmp_node.val
            while tmp_node.lchild:
                tmp_node = tmp_node.lchild
                min_val = tmp_node.val
            # replace value
            current_node.val = min_val
            # Delete the minimum node in right subtree
            current_node.rchild = self.delete_node(current_node.rchild, current_node.val)
        return current_node


bst = BinarySearchTree()
bst.insert(5)
bst.insert(55)
bst.insert(65)
bst.insert(6)
bst.insert(7)
bst.insert(8)
bst.insert(1)

bst.delete(1)
bst.in_order()
bst.pre_order()
bst.post_order()
bst.findMinValue()
bst.findMaxValue()

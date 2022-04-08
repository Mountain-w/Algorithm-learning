class AVLNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class AVLTree:
    def __init__(self, val):
        self.root = AVLNode(val)

    def add(self, val):
        pass

    def roate_left(self, root):
        new_head = root.right
        root.right = new_head.left
        new_head.left = root
        return new_head

    def roate_right(self, root):
        new_head = root.left
        root.left = new_head.right
        new_head.right = root
        return new_head

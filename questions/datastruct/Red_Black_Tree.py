class RBTNode:
    def __init__(self, val, left=None, right=None, color=None):
        """
        :param val: the red_black_tree node value
        :param left: the red_black_tree left tree
        :param right: the red_black_tree right tree
        :param color: the red_black_tree color
        """
        self.val = val
        self.left = left
        self.right = right
        self.color = color


class RedBlackTree:
    def __init__(self, val):
        self.root = RBTNode(val, 'black')

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

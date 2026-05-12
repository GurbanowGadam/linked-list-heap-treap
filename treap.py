import random


class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, 1_000_000)
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None

    def rotate_right(self, y):
        x = y.left
        T = x.right

        x.right = y
        y.left = T

        return x

    def rotate_left(self, x):
        y = x.right
        T = y.left

        y.left = x
        x.right = T

        return y

    def insert(self, root, key):
        if root is None:
            return TreapNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)

            if root.left.priority < root.priority:
                root = self.rotate_right(root)

        else:
            root.right = self.insert(root.right, key)

            if root.right.priority < root.priority:
                root = self.rotate_left(root)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def delete(self, root, key):
        if root is None:
            return None

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            if root.left.priority < root.right.priority:
                root = self.rotate_right(root)
                root.right = self.delete(root.right, key)
            else:
                root = self.rotate_left(root)
                root.left = self.delete(root.left, key)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def search_key(self, key):
        return self.search(self.root, key) is not None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"{root.key}({root.priority})", end=" ")
            self.inorder(root.right)
## Challenge
Write a function called fizz buzz tree that takes in an argument of k-ary tree. This should then return a new k-ary tree. 

## Approach & Efficiency
I took a TDD approach with this because that would be the optimal way when writing code.
Big O:
    Space:O(n)
    Time:O(w)

## API

## White Board
![tree-fizz-buzz](fizz-buzz.png)

<!-- class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node

        def walk(root, add_node):
            if root is None:
                return
            if add_node.value < root.value:
                if root.left:
                    walk(root.left, add_node)
                else:
                    root.left = add_node
            else:
                if root.right:
                    walk(root.right, add_node)
                else:
                    root.right = add_node
        walk(self.root, node)

    def fizz_buzz(tree):
        if tree.root is None:
            return None
    
        k = KaryTree()
        def walk(root):
            if root is None:
                return None
            if root.value % 5 == 0 and root.value % 3 == 0:
                k.add('fizzbuzz')
            elif root.value % 3 == 0:
                k.add('fizz')
            elif root.value % 5 == 0:
                k.add('buzz')
            else:
                k.add(str(root.value))
    
        walk(tree.root)
        return k -->

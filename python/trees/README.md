# Trees
Node
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Binary Tree
  Create a Binary Tree class
    Define a method for each of the depth first traversals:
      pre order
      in order
      post order which returns an array of the values, ordered appropriately.

Binary Search Tree
  Create a Binary Search Tree class
    This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
  Add
    Arguments: value
    Return: nothing
    Adds a new node with that value in the correct location in the binary search tree.
  Contains
    Argument: value
  Returns: boolean indicating whether or not the value is in the tree at least once.

## Challenge
Create a node, binary tree, and binary search tree class and perform the tasks above.

## Approach & Efficiency
I took a TDD approach with this because that would be the optimal way when writing code.
Big O:
  Binary Tree:
    Space:O(w)
    Time:O(n)
  Binary Search Tree:
    Space:O(1)
    Time:O(h)

## API
pre_order - returns a list of the values in a Binary Tree via a pre order traversal.
in_order - returns a list of the values in a Binary Tree via an in order traversal.
post_order - returns a list of the values in a Binary Tree via a post order traversal.

add - Adds a value to a binary search tree
contains - Returns a boolean indicating whether or not the given value is in the tree at least once.



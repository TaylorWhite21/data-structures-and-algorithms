from trees.bt_and_bst import BinaryTree
from trees.bt_node import Node

def test_node_creation():
    node = Node('Yang')
    actual = node.value
    expected = 'Yang'
    assert actual == expected

def test_node_creation_bad():
    node = Node('Cinder')
    actual = node.value
    expected = 'Cinder'
    assert actual == expected
    
# Can successfully instantiate an empty tree
def test_bt_empty():
    bt = BinaryTree()
    assert bt
    
# Can successfully instantiate a tree with a single root node
def test_bt_empty_root_none():
    ruby = Node('Ruby')
    bt = BinaryTree(ruby)
    assert bt.root.value == 'Ruby'

def test_bt_left():
    ruby = Node('Ruby')
    weiss = Node('Weiss')
    pyrrha = Node('Pyrrha')
    bt = BinaryTree(ruby)
    ruby.left = weiss
    ruby.right = pyrrha
    
    assert ruby.left == bt.root.left

def test_bt_right():
    ruby = Node('Ruby')
    weiss = Node('Weiss')
    pyrrha = Node('Pyrrha')
    bt = BinaryTree(ruby)
    ruby.left = weiss
    ruby.right = pyrrha
    
    assert ruby.right == bt.root.right
    
# Can successfully return a collection from a preorder traversal
def test_pre_order():
    ruby = Node('Ruby')
    blake = Node('Blake')
    weiss = Node('Weiss')
    yang = Node('Yang')
    bt = BinaryTree(ruby)

    ruby.left = blake
    ruby.right = yang
    blake.left = weiss
    order_list = bt.pre_order()
    assert order_list == ['Ruby','Blake','Weiss','Yang']
    
def test_pre_order_bad():
    ruby = Node('Ruby')
    blake = Node('Blake')
    weiss = Node('Weiss')
    yang = Node('Yang')
    bt = BinaryTree(ruby)

    ruby.left = blake
    ruby.right = yang
    blake.left = weiss
    order_list = bt.pre_order()
    assert order_list != ['Ruby','Weiss','Yang','Blake']
    
# Can successfully return a collection from an inorder traversal
def test_in_order():
    pyrrha = Node('Pyrrha')
    nora = Node('Nora')
    jaune = Node('Jaune')
    qrow = Node('Qrow')
    bt = BinaryTree(pyrrha)
    
    pyrrha.left = nora
    pyrrha.right = jaune
    nora.right = qrow
    #           pyrrha
    #          /      \
    #      nora        jaune
    #         \
    #          qrow
    order_list = bt.in_order()
    assert order_list == ['Nora','Qrow','Pyrrha','Jaune']

# Can successfully return a collection from a postorder traversal
def test_post_order():
    emerald = Node('Emerald')
    winter = Node('Winter')
    salem = Node('Salem')
    cinder = Node('Cinder')
    bt = BinaryTree(emerald)
    
    emerald.left = winter
    emerald.right = salem
    salem.left = cinder
    #           Emerald
    #          /       \
    #      winter      salem
    #                  /
    #               cinder

    order_list = bt.post_order()
    assert order_list == ['Winter','Cinder','Salem','Emerald']
    

# For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_add_node_to_empty_bst():
    node = Node(21)
    bst = BinaryTree.BinarySearchTree(node)
    assert bst.root.value == 21    

def test_add_node_left_bst():
    node1 = Node(21)
    bst = BinaryTree.BinarySearchTree(node1)
    bst.add(17)
    assert bst.root.left.value == 17 

def test_add_node_right_bst():
    node1 = Node(21)
    bst = BinaryTree.BinarySearchTree(node1)
    bst.add(25)
    assert bst.root.right.value == 25
    
# Returns true	false for the contains method, given an existing or non-existing node value
def test_bst_contains_value_right():
    node1 = Node(21)
    node2 = Node(34)
    node3 = Node(17)
    node1.left = node3
    node1.right = node2
    bst = BinaryTree.BinarySearchTree(node1)
    
    assert bst.contains(34) == True
    
def test_bst_contains_value_left():
    node1 = Node(21)
    node2 = Node(34)
    node3 = Node(17)
    node1.left = node3
    node1.right = node2
    bst = BinaryTree.BinarySearchTree(node1)
    
    assert bst.contains(17) == True

def test_bst_contains_root():
    node1 = Node(21)
    node2 = Node(34)
    node3 = Node(17)
    node1.left = node3
    node1.right = node2
    bst = BinaryTree.BinarySearchTree(node1)
    
    assert bst.contains(21) == True

def test_find_max_single_node():
    node1 = Node(21)
    bt = BinaryTree(node1)
    assert bt.find_max() == 21
    
def test_bt_find_max():
    node1 = Node(21)
    node2 = Node(34)
    node3 = Node(17)
    node1.left = node3
    node1.right = node2
    bt = BinaryTree(node1)
    
    assert bt.find_max() == 34

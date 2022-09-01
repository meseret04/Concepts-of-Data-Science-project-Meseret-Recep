# README for developers

This README basically explains how the AVL Tree class works and how it can be contributed to the project. The AVL tree is a self-balancing binary search tree in which the height difference of the right and left subtrees is not more than 1.

## ABOUT ARGUMENTS

The AVL class is a nested class that contains a generic node class that initialize value, left and right child node, parent node and height.
```python
class AvlTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, val=None):
            self.val = val
            self.left = None
            self.right = None
            self.parent = None
            self.height = 1
```        

## FLOW OF CODES

The _*repr*_ _ method is used to create the tree object in a string format.
```python
    def __repr__(self):
        if self.root is None:
            return ''
        string = ''
        current_nodes = [self.root]
        current_height = self.root.height
        sep = ' '
        while True:
            current_height += -1
            if len(current_nodes) == 0:
                break
            current_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in current_nodes):
                break

            for n in current_nodes:...
            
            string += (current_row + next_row)
            current_nodes = next_nodes
            sep = ' '
        return string
```       

Two methods are created to visualize the tree. The first method visualizes trees consisting of numbers only. Normally *build* function
in the binarytress library visualizes binary trees, but to make it usable for the AVL tree, a dummy is assigned in the string to represent NONE values ​​deep in the tree created within the AVL tree object.

The second method draws graph objects using the Digraph module in Graphviz and exceptions are thrown to avoid errors caused by non-node values.

In this method, an additional argument has been added that allows to visualize the desired size of the tree, such as a word tree, which consists of many nodes.
```python
    def draw_number_tree(self):
        from binarytree import build
        txt = str(self)
        build_list = [int(s) for s in txt.split() if s.isdigit()]
        build_list = [x if x > 0 else None for x in build_list]
        return build(build_list)

    def draw_tree(self, number_of_nodes):
        txt = str(self)
        n_list = [s for s in txt.split() if s.isalnum() or '-']
        node_list = [x if x != '00' else None for x in n_list]

        from graphviz import Digraph
        d = Digraph('g', node_attr={'shape': 'record', 'height': '.1'})
        d.attr(size='14')
        for i in n_list[0:number_of_nodes]:...
        return d
```

A rotation feature is required to balance the tree after removal or insertion. In order to achieve this, a method of rebalancing the nodes, which creates the right rotation, left rotation, and rotation orders according to the status of the nodes, has been created.
```python
    def _right_rotate(self, z):...

    def _left_rotate(self, z):...

   def _rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:...
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.right and x == y.left:...
```

An insert process has been created to add nodes to the tree. For this, 3 methods have been created. The first method is the insert method, which gives the order for the insert operation. The second method is the _insert method, which determines the position of the inserted node if there is already value in the tree. The method that controls the insert operation detects whether the node added to the path requires balancing in the tree, and performs the rebalancing operation recursively depending on the condition that the height of the two subtrees, which are the condition of the AVL tree, the difference cannot be more than one.

```python
    def _inspect_insert(self, current_node, path=None):...

    def _insert(self, val, current_node):
        if val < current_node.val:
            if current_node.left is None:...
            else:
                self._insert(val, current_node.left)
        elif val > current_node.val:
            if current_node.right is None:...
            else:
                self._insert(val, current_node.right)

    def insert(self, val):...
```
Two methods have been created to add the search feature. In order to find the sought value, starting from the root of the tree, the binary query is continued down the tree to the sought value. In each query, the subtree where the value is found is determined.

In addition to the search method, the find method, which brings the node of the queried value, has been made.
```python
    def _search(self, val, current_node):
        if val == current_node.val:
            return True
        elif val < current_node.val and current_node.left is not None:
            return self._search(val, current_node.left)
        elif val > current_node.val and current_node.right is not None:
            return self._search(val, current_node.right)
        return False

    def search(self, val):...
```

4 different methods have been created for the removal process. The first of these is the remove method, which starts the removal process. If the value to be removed exists in the tree, with the help of the find method, the node of this value is found and it is directed to the removal method that will do the removal.
Two functions are defined in this method. The first one contains functions that get the number of children of the specified node with the method that returns the smallest value of the subtree where the node in question is the root. 
According to the number of children of the specified node (0, 1, or 2), the removal process was carried out depending on 3 separate cases. Lastly, as in the insert, the balancing process was performed again.

```python
    def _remove_node(self, node):

        def min_value_node(n):...

        def num_children(n):...
        node_parent = node.parent

        node_children = num_children(node)

        if node_children == 0:...
        
        if node_children == 1:...
           
        if node_children == 2:...

        if node_parent is not None:...

    def remove(self, val):
        if self.search(val):...
        else:
            print(f'"{val}" is not found in the tree')
```

## CONTRIBUTION

Those who want to contribute to the project can improve the visualizations and combine the visualization of numbers and words. Likewise, for simplification, the remove and add inspect methods can be combined.

## Coding style

### Use the following naming conventions
* '_'-separated_lowercase for method names
* '_'-separated_lowercase for variable names

### Indentation must not include tabs
* Use 2 spaces for indentation.
* Don't replace spaces to tabs.


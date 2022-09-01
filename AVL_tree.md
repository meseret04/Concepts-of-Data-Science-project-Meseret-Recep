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

            for n in current_nodes:

                if n is None:
                    current_row += '00' + sep
                    next_row += sep
                    next_nodes.extend([None, None])
                    continue

                if n.val is not None:
                    current_row += str(n.val) + sep
                else:
                    current_row += sep

                if n.left is not None:
                    next_nodes.append(n.left)
                    next_row += sep
                else:
                    next_row += sep
                    next_nodes.append(None)

                if n.right is not None:
                    next_nodes.append(n.right)
                    next_row += sep
                else:
                    next_row += sep
                    next_nodes.append(None)

            string += (current_row + next_row)
            current_nodes = next_nodes
            sep = ' '
        return string

    def _get_height(self, current_node):
        if current_node is None:
            return 0
        return current_node.height

    def _right_rotate(self, z):
        sub_root = z.parent
        y = z.left
        t = y.right
        y.right = z
        z.parent = y
        z.left = t
        if t is not None:
            t.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right
        t = y.left
        y.left = z
        z.parent = y
        z.right = t
        if t is not None:
            t.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

    def _rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)

    def _inspect_insert(self, current_node, path=None):
        if path is None:
            path = []
        if current_node.parent is None:
            return
        path = [current_node] + path

        left_height = self._get_height(current_node.parent.left)
        right_height = self._get_height(current_node.parent.right)

        if abs(left_height - right_height) > 1:
            path = [current_node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + current_node.height
        if new_height > current_node.parent.height:
            current_node.parent.height = new_height

        self._inspect_insert(current_node.parent, path)

    def _insert(self, val, current_node):
        if val < current_node.val:
            if current_node.left is None:
                current_node.left = AvlTree.Node(val)
                current_node.left.parent = current_node
                self._inspect_insert(current_node.left)
            else:
                self._insert(val, current_node.left)
        elif val > current_node.val:
            if current_node.right is None:
                current_node.right = AvlTree.Node(val)
                current_node.right.parent = current_node
                self._inspect_insert(current_node.right)
            else:
                self._insert(val, current_node.right)

    def insert(self, val):
        if self.search(val):
            return None
        elif self.root is None:
            self.root = AvlTree.Node(val)
        else:
            self._insert(val, self.root)

    def _search(self, val, current_node):
        if val == current_node.val:
            return True
        elif val < current_node.val and current_node.left is not None:
            return self._search(val, current_node.left)
        elif val > current_node.val and current_node.right is not None:
            return self._search(val, current_node.right)
        return False

    def search(self, val):
        if self.root is not None:
            return self._search(val, self.root)
        else:
            return False

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, current_node):
        if val == current_node.val:
            return current_node
        elif val < current_node.val and current_node.left is not None:
            return self._find(val, current_node.left)
        elif val > current_node.val and current_node.right is not None:
            return self._find(val, current_node.right)

    def _taller_child(self, current_node):
        left = self._get_height(current_node.left)
        right = self._get_height(current_node.right)
        return current_node.left if left >= right else current_node.right

    def _inspect_remove(self, current_node):
        if current_node is None:
            return

        left_height = self._get_height(current_node.left)
        right_height = self._get_height(current_node.right)

        if abs(left_height - right_height) > 1:
            y = self._taller_child(current_node)
            x = self._taller_child(y)
            self._rebalance_node(current_node, y, x)

        self._inspect_remove(current_node.parent)

    def _remove_node(self, node):

        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        def num_children(n):
            n_children = 0
            if n.left is not None:
                n_children += 1
            if n.right is not None:
                n_children += 1
            return n_children

        node_parent = node.parent

        node_children = num_children(node)

        if node_children == 0:

            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        if node_children == 1:

            if node.left is not None:
                child = node.left
            else:
                child = node.right

            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child

                child.parent = node_parent

        if node_children == 2:
            successor = min_value_node(node.right)
            node.val = successor.val
            self._remove_node(successor)

            return

        if node_parent is not None:
            node_parent.height = 1 + max(self._get_height(node_parent.left), self._get_height(node_parent.right))

            self._inspect_remove(node_parent)

    def remove(self, val):
        if self.search(val):
            found_value = self.find(val)
            print(f'removing "{val}"...')
            return self._remove_node(found_value)
        else:
            print(f'"{val}" is not found in the tree')

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
        for i in n_list[0:number_of_nodes]:
            try:
                d.edge(i, self.find(i).left.val)
            except:
                pass
            try:
                d.edge(i, self.find(i).right.val)
            except:
                pass
        return d

```


```python
import pandas as pd
import requests
from io import StringIO

url = "https://gitlab.com/Meseret.A/concepts-of-data-science-project-work-4/-/raw/master/20_numbers.txt"
df = pd.read_csv(StringIO(requests.get(url).text), header=None)

numbers = df[0].values.tolist()

number_tree = AvlTree()
for i in numbers:
    number_tree.insert(i)

number_tree.draw_number_tree()
```

    
![svg](output_3_0.svg)
    

## Searching on the numbers file


```python
search_list = [13, 29, 48, 58]

for i in search_list:
    print(f'{i} is in the tree:', number_tree.search(i))
```

    13 is in the tree: False
    29 is in the tree: True
    48 is in the tree: True
    58 is in the tree: False


## Inserting on the numbers file


```python
insert_list = [5, 51, 82, 98]

print(number_tree.draw_number_tree())
for i in insert_list:
    number_tree.insert(i)
    print(f'inserting {i}...')
print(number_tree.draw_number_tree())
```

    
            ___________________49____________
           /                                 \
      ____29_________                     ____60______
     /               \                   /            \
    15            ____36            ____57         ____84
      \          /      \          /      \       /      \
       16      _31       43       54       59    67       87
              /   \        \        \              \        \
             30    34       48       56             71       99
    
    inserting 5...
    inserting 51...
    inserting 82...
    inserting 98...
    
              ___________________49_______________
             /                                    \
        ____29_________                        ____60_________
       /               \                      /               \
      15            ____36               ____57            ____84___
     /  \          /      \             /      \          /         \
    5    16      _31       43         _54       59      _71         _98
                /   \        \       /   \             /   \       /   \
               30    34       48    51    56          67    82    87    99
    


## Deleting on the numbers file


```python
delete_list = [31,34,54,68]

for i in delete_list:
    number_tree.remove(i)
    print(number_tree.draw_number_tree())
```

    "31" is not found in the tree
    
              _____________49____________
             /                           \
        ____29___                     ____60_________
       /         \                   /               \
      15         _36               _57            ____84___
     /  \       /   \             /   \          /         \
    5    16    30    43         _56    59      _71         _98
                       \       /              /   \       /   \
                        48    51             67    82    87    99
    
    "34" is not found in the tree
    
              _____________49____________
             /                           \
        ____29___                     ____60_________
       /         \                   /               \
      15         _36               _57            ____84___
     /  \       /   \             /   \          /         \
    5    16    30    43         _56    59      _71         _98
                       \       /              /   \       /   \
                        48    51             67    82    87    99
    
    "54" is not found in the tree
    
              _____________49____________
             /                           \
        ____29___                     ____60_________
       /         \                   /               \
      15         _36               _57            ____84___
     /  \       /   \             /   \          /         \
    5    16    30    43         _56    59      _71         _98
                       \       /              /   \       /   \
                        48    51             67    82    87    99
    
    "68" is not found in the tree
    
              _____________49____________
             /                           \
        ____29___                     ____60_________
       /         \                   /               \
      15         _36               _57            ____84___
     /  \       /   \             /   \          /         \
    5    16    30    43         _56    59      _71         _98
                       \       /              /   \       /   \
                        48    51             67    82    87    99
    



```python
url = "https://gitlab.com/Meseret.A/concepts-of-data-science-project-work-4/-/raw/master/2795_words.txt"
df = pd.read_csv(StringIO(requests.get(url).text), header=None)

words = df[0].values.tolist()

word_tree = AvlTree()

for i in words:
    word_tree.insert(str(i))

word_tree.draw_tree(10)

```




    
![svg](output_12_0.svg)
    



## Searching on the words file


```python
search_list = ["kangaroo", "harbor", "existentialism", "wheel"]

for i in search_list:
    print(f'"{i}" is in the tree:'+(15 - len(i))*" ", word_tree.search(i))
```

    "kangaroo" is in the tree:        False
    "harbor" is in the tree:          True
    "existentialism" is in the tree:  False
    "wheel" is in the tree:           True


## Inserting on the words file


```python
insert_list = ["afternoon", "maybe", "computer", "pigment"]

for i in insert_list:
    print(f'"{i}" is in the tree:'+(15 - len(i))*" ", word_tree.search(i))
    word_tree.insert(i)
    print(f'inserting {i}...')
    print(f'"{i}" is in the tree:'+(15 - len(i))*" ", word_tree.search(i), end="\n")
    print("\n")

```

    "afternoon" is in the tree:       False
    inserting afternoon...
    "afternoon" is in the tree:       True
    
    
    "maybe" is in the tree:           False
    inserting maybe...
    "maybe" is in the tree:           True
    
    
    "computer" is in the tree:        False
    inserting computer...
    "computer" is in the tree:        True
    
    
    "pigment" is in the tree:         False
    inserting pigment...
    "pigment" is in the tree:         True
    
    


# Deleting on the words file


```python
delete_list = [ "persuade", "slippery", "drain", "shocking"]

for i in delete_list:
    if word_tree.search(i): 
        print(f'deleting "{i}"...')
        word_tree.remove(i)
        print(f'"{i}" is in the tree:'+(12 - len(i))*" ", word_tree.search(i))
    else:
        print(f'deleting "{i}"...')
        print(f'"{i}" is not found in the tree')
    print("\n")
```

    deleting "persuade"...
    removing "persuade"...
    "persuade" is in the tree:     False
    
    
    deleting "slippery"...
    removing "slippery"...
    "slippery" is in the tree:     False
    
    
    deleting "drain"...
    removing "drain"...
    "drain" is in the tree:        False
    
    
    deleting "shocking"...
    removing "shocking"...
    "shocking" is in the tree:     False
    
    


## Time Complexity
***Insertion***

The insertion of a node is going to take O(log n) time because the tree is balanced. Also, the unbalances in the insertion process get fixed after a fixed number of rotations. So, the entire process is of O(log n) time.





```python
a = AvlTree()
a.insert(3)
a.insert(5)
a.insert(6)
a.insert(9)
a.insert(12)
a.insert(10)
a.draw_number_tree()
```




    
![svg](output_20_0.svg)
    



For inserting element 14, it must be inserted as right child of 12. Therefore, we need to traverse elements (in order 9, 12, 14) to insert 14 which has worst case complexity of O(log n).

***Remove***

Due to the balancing property of AVL Tree, the removal  process takes O(log n) in both the average and the worst cases as well as search and insert methods. 


```python
a.insert(14)
a.draw_number_tree()
```




    
![svg](output_23_0.svg)
    



For remove of element 3, we have to traverse elements to find 3 (in order 9, 5, 3). So remove in binary tree has worst case complexity of O(log n).

***Search***

For searching element 3, we have to traverse elements (in order 9, 5, 3) = 3 = log n. Therefore, searching in AVL tree has worst case complexity of O(log n). Here, we create a graph to compare the time complexities of linear search (*in* operator) and AVL search using the tree of words.  


```python
import timeit
import matplotlib.pyplot as plt

words_index = [10, 20, 40, 80, 160, 320, 640, 1280, 2560]

time_in = []
nr_runs = 5
for i in words_index:
    for j in range(nr_runs):
        t = timeit.timeit(lambda: words[i] in words)
    time_in.append(t/nr_runs)

time_search = []
nr_runs = 5
for i in words_index:
    for j in range(nr_runs):
        t = timeit.timeit(lambda: word_tree.search(words[i]))
    time_search.append(t/nr_runs)


plt.plot(words_index, time_in, label='Linear search')
plt.plot(words_index, time_search, label='AVL search ')
plt.legend()
```


    
![png](output_26_1.png)
    


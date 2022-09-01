class AVL_Tree:
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
        string = '\n'
        current_nodes = [self.root]
        current_height = self.root.height
        sep = ' ' * (2 ** (current_height - 1))
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
                    current_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.val is not None:
                    buf = ' ' * int(((5 - len(str(n.val))) / 2))
                    current_row += '%s%s%s' % (buf, str(n.val), buf) + sep
                else:
                    current_row += ' ' * 5 + sep

                if n.left is not None:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right is not None:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            string += (current_height * '   ' + current_row + '\n' + current_height * '   ' + next_row + '\n')
            current_nodes = next_nodes
            sep = ' ' * int((len(sep) / 2))
        return string

    def getHeight(self, current_node):
        if current_node is None:
            return 0
        return current_node.height

    def rightRotate(self, z):
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
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

    def leftRotate(self, z):
        sub_root = z.parent
        y = z.right
        t2 = y.left
        y.left = z
        z.parent = y
        z.right = t2
        if t2 is not None:
            t2.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

    def rebalanceNode(self, z, y, x):
        if y == z.left and x == y.left:
            self.rightRotate(z)
        elif y == z.left and x == y.right:
            self.leftRotate(y)
            self.rightRotate(z)
        elif y == z.right and x == y.right:
            self.leftRotate(z)
        elif y == z.right and x == y.left:
            self.rightRotate(y)
            self.leftRotate(z)

    def inspect_insert(self, current_node, path=None):
        if path is None:
            path = []
        if current_node.parent is None:
            return
        path = [current_node] + path

        left_height = self.getHeight(current_node.parent.left)
        right_height = self.getHeight(current_node.parent.right)

        if abs(left_height - right_height) > 1:
            path = [current_node.parent] + path
            self.rebalanceNode(path[0], path[1], path[2])
            return

        new_height = 1 + current_node.height
        if new_height > current_node.parent.height:
            current_node.parent.height = new_height

        self.inspect_insert(current_node.parent, path)

    def _insert(self, val, current_node):
        if val < current_node.val:
            if current_node.left is None:
                current_node.left = AVL_Tree.Node(val)
                current_node.left.parent = current_node
                self.inspect_insert(current_node.left)
            else:
                self._insert(val, current_node.left)
        elif val > current_node.val:
            if current_node.right is None:
                current_node.right = AVL_Tree.Node(val)
                current_node.right.parent = current_node
                self.inspect_insert(current_node.right)
            else:
                self._insert(val, current_node.right)

    def insert(self, val):
        if self.root is None:
            self.root = AVL_Tree.Node(val)
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
            print("Value is found")
            return current_node
        elif val < current_node.val and current_node.left is not None:
            return self._find(val, current_node.left)
        elif val > current_node.val and current_node.right is not None:
            return self._find(val, current_node.right)

    def taller_child(self, current_node):
        left = self.getHeight(current_node.left)
        right = self.getHeight(current_node.right)
        return current_node.left if left >= right else current_node.right

    def inspect_remove(self, current_node):
        if current_node is None:
            return

        left_height = self.getHeight(current_node.left)
        right_height = self.getHeight(current_node.right)

        if abs(left_height - right_height) > 1:
            y = self.taller_child(current_node)
            x = self.taller_child(y)
            self.rebalanceNode(current_node, y, x)

        self.inspect_remove(current_node.parent)

    def removeNode(self, node):

        found_value = self.find(node.val)

        if node == None or found_value == None:
            print("Node to be deleted not found in the tree!")
            return None

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
            self.removeNode(successor)

            return

        if node_parent is not None:
            node_parent.height = 1 + max(self.getHeight(node_parent.left), self.getHeight(node_parent.right))

            self.inspect_remove(node_parent)

    def remove(self, value):
        found_value = self.find(value)

        return self.removeNode(found_value)


a = AVL_Tree()

a.insert(10)
a.insert(22)
a.insert(8)
a.insert(16)
a.insert(13)
a.insert(112)
a.insert(56)
a.insert(67)
a.insert(23)

print(a)

a.remove(56)

print(a)
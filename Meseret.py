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



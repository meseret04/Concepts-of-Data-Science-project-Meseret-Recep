def search(self, value):
    if self.root != None:
        return self._search(value, self.root)
    else:
        return False


def _search(self, value, current_node):
    if value == current_node.value:
        return True
    elif value < current_node.value and current_node.left_child != None:
        return self._search(value, current_node.left_child)
    elif value > current_node.value and current_node.right_child != None:
        return self._search(value, current_node.right_child)
    return False

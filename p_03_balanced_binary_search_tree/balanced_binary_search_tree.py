import random


class Node:
    def __init__(self, data, p_ref = None, l_ref = None, r_ref = None, bf = 0, height = 0):
        self.data = data        # data
        self.p_ref = p_ref      # parent ref
        self.l_ref = l_ref      # left ref
        self.r_ref = r_ref      # right ref
        self.bf = bf            # bf new node standard 0
        self.height = height

    # display and display_aux copied from: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.r_ref is None and self.l_ref is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.r_ref is None:
            lines, n, p, x = self.l_ref._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line,
                    second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.l_ref is None:
            lines, n, p, x = self.r_ref._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line,
                    second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.l_ref._display_aux()
        right, m, q, y = self.r_ref._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (
                    m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (
                    m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in
                                             zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def __repr__(self):
        return f"{self.data},bf = {self.bf} --> L({self.l_ref}), R({self.r_ref})"


class AVLTree:
    def __init__(self) -> None:
        self.root = None

    # insert
    def insert_data(self, data) -> None:
        new_node = Node(data)
        self.insert(new_node)

    def insert(self, node) -> None:
        if self.root is None:
            self.root = node
            node.p_ref = self
        else:
            parent = self._find_insert_parent_recursive(self.root, node)
            node.p_ref = parent
            if node.data < parent.data:
                parent.l_ref = node
            elif node.data > parent.data:
                parent.r_ref = node
        self._bf_height(node)

    def _find_insert_parent_recursive(self, evaluate_node, new_node) -> Node:
        if new_node.data <= evaluate_node.data: # go left subtree
            if evaluate_node.l_ref is None:
                return evaluate_node
            return self._find_insert_parent_recursive(evaluate_node.l_ref, new_node)
        if new_node.data > evaluate_node.data: # go right subtree
            if evaluate_node.r_ref is None:
                return evaluate_node
            return self._find_insert_parent_recursive(evaluate_node.r_ref, new_node)
        raise Exception("Error occurred at _find_insert_parent_recursive")

    # search
    def search(self, data) -> Node:
        return self._search_recursive(self.root,data)

    def _search_recursive(self, node, data):
        if node.data == data:
            return node
        if data < node.data and node.l_ref is not None:
            return self._search_recursive(node.l_ref, data)
        if data > node.data and node.r_ref is not None:
            return self._search_recursive(node.r_ref, data)
        return None

    # delete
    def delete_by_data(self, data) -> None:
        node = self.search(data)
        if node.data == data:
            self.delete(node)

    def delete(self, node):
        parent_node = node.p_ref
        left_subtree = node.l_ref
        right_subtree = node.r_ref
        l_or_r_child = self._l_or_r_child(parent_node, node)
        # scenario 1: no children
        if left_subtree is None and right_subtree is None:
            if l_or_r_child == 0:
                self.root = None
            elif l_or_r_child == -1:
                parent_node.l_ref = None
            else:
                parent_node.r_ref = None
        # scenario 2: 1 child
        elif left_subtree is None:
            if l_or_r_child == 0:
                self.root = right_subtree
                right_subtree.p_ref = self
            elif l_or_r_child == -1:
                parent_node.l_ref = right_subtree
            else:
                parent_node.r_ref = right_subtree
        elif right_subtree is None:
            if l_or_r_child == 0:
                self.root = left_subtree
                left_subtree.p_ref = self
            elif l_or_r_child == -1:
                parent_node.l_ref = left_subtree
            else:
                parent_node.r_ref = left_subtree
        # scenario 3: 2 children
        else:
            previous_help_ref = None
            if node.bf <= 0: # if left heavy or both subtrees are equal
                # find most right child of left subtree
                help_ref = node.l_ref
                while help_ref is not None:
                    previous_help_ref = help_ref
                    if help_ref.r_ref is not None:
                        help_ref = help_ref.r_ref
                        break
                    if help_ref.l_ref is not None:
                        help_ref = help_ref.l_ref
                        break
                    help_ref = None
            else: # if right heavy
                # find most left child of right subtree
                help_ref = node.r_ref
                previous_help_ref = None
                while help_ref is not None:
                    previous_help_ref = help_ref
                    if help_ref.l_ref is not None:
                        help_ref = help_ref.l_ref
                        break
                    if help_ref.r_ref is not None:
                        help_ref = help_ref.r_ref
                        break
                    help_ref = None
            self._remove_ref_to(previous_help_ref.p_ref, previous_help_ref)
            previous_help_ref.p_ref = parent_node
            if l_or_r_child == 0:
                self.root = previous_help_ref
            elif l_or_r_child < 0:
                parent_node.l_ref = previous_help_ref
            else:
                parent_node.r_ref = previous_help_ref

    def _remove_ref_to(self, parent_node, node):
        l_or_r = self._l_or_r_child(parent_node, node)
        if l_or_r == 0:
            self.root = None
        elif l_or_r < 0:
            parent_node.l_ref = None
        else:
            parent_node.r_ref = None

    # balance factor and height
    def _bf(self, node) -> None:
        left_subtree = 0 if node.l_ref is None else node.l_ref.height + 1
        right_subtree = 0 if node.r_ref is None else node.r_ref.height + 1
        # determine height of current node
        node.height = max(left_subtree, right_subtree)
        # balance_factor
        node.bf = right_subtree - left_subtree

    def _bf_height(self, node) -> None:
        self._bf(node)
        if node.bf < -1:
            self._rebalance(node.l_ref)
        if node.bf > 1:
            self._rebalance(node.r_ref)
        # if parent height is not correct, recursive
        if node.p_ref is not self:
            self._bf_height(node.p_ref)

    # rebalance -> rr, ll, rl, lr
    def _rebalance(self, node):
        parent_node = node.p_ref
        l_or_r_child = self._l_or_r_child(parent_node, node)
        # ll -> Z is a left child of its parent X and BF(Z) <= 0
        if l_or_r_child == -1 and node.bf <= 0:
            self._rotate_right(parent_node, node)
        # rr -> Z is a right child of its parent X and BF(Z) >= 0
        elif l_or_r_child == 1 and node.bf >= 0:
            self._rotate_left(parent_node, node)
        # lr -> Z is a left child of its parent X and BF(Z) > 0
        elif l_or_r_child == -1 and node.bf > 0:
            self._rotate_lr(parent_node, node)
            self._bf(node)
            self._bf(parent_node)
        # rl -> Z is a right child of its parent X and BF(Z) < 0
        elif l_or_r_child == 1 and node.bf < 0:
            self._rotate_rl(parent_node, node)
            self._bf(node)
            self._bf(parent_node)
        else:
            raise Exception("Error occurred at _rebalance")
        self._bf_height(parent_node)

    def _l_or_r_child(self, parent, node):
        if parent is self:
            return 0
        if parent.l_ref is not None and parent.l_ref == node:
            return -1
        elif parent.r_ref is not None and parent.r_ref == node:
            return 1
        else:
            raise Exception("Error occurred at _l_or_r_child, is not a child of parent")

    def _rotate_left(self, parent_node, node):
        grandparent = parent_node.p_ref
        parent = parent_node
        # connect left subtree node to right ref parent
        parent.r_ref = node.l_ref
        if node.l_ref is not None:
            node.l_ref.p_ref = parent
        l_or_r = self._l_or_r_child(grandparent, parent)
        # connect node to grandparent
        node.p_ref = grandparent
        if l_or_r == 0:
            self.root = node
        elif l_or_r < 0:
            grandparent.l_ref = node
        else:
            grandparent.r_ref = node
        # connect parent to left ref of node
        node.l_ref = parent
        parent.p_ref = node

    def _rotate_right(self, parent_node, node):
        grandparent = parent_node.p_ref
        parent = parent_node
        # connect right subtree node to left ref parent
        parent.l_ref = node.r_ref
        if node.r_ref is not None:
            node.r_ref.p_ref = parent
        l_or_r = self._l_or_r_child(grandparent, parent)
        # connect node to grandparent
        node.p_ref = grandparent
        if l_or_r == 0:
            self.root = node
        elif l_or_r < 0:
            grandparent.l_ref = node
        else:
            grandparent.r_ref = node
        # connect parent to right ref of node
        node.r_ref = parent
        parent.p_ref = node

    def _rotate_lr(self, parent_node, node) -> None:
        self._rotate_left(node, node.r_ref)
        self._rotate_right(parent_node, parent_node.l_ref)

    def _rotate_rl(self, parent_node, node) -> None:
        self._rotate_right(node, node.l_ref)
        self._rotate_left(parent_node, parent_node.r_ref)

    def __repr__(self) -> str:
        return "root: " + self.root.__repr__()

    def print_tree(self) -> None:
        if self.root is not None:
            self.root.display()
        else:
            print("empty tree")


if __name__ == "__main__":
    tree = AVLTree()
    for i in range(50):
        tree.insert_data(random.randint(0,100))
        tree.print_tree()
        print(tree)
    tree.insert_data(61)
    tree.delete_by_data(61)

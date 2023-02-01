import random


class Node:
    def __init__(self, data=None, n_ref=None):
        self.data = data
        self.n_ref = n_ref

    def __repr__(self) -> str:
        return f"{self.data} -> {self.n_ref}"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def get_head(self) -> Node:
        return self.head

    def push(self, data) -> None:
        self.push_node(Node(data))

    def push_node(self, node: Node) -> None:
        if self.empty():
            self.head = node
        else:
            last_node = self._search_previous_node(None)
            last_node.n_ref = node

    def unshift(self, data) -> None:
        self.unshift_node(Node(data))

    # shift is better -> constant time
    def unshift_node(self, node: Node) -> None:
        previous_head = self.head
        self.head = node
        node.n_ref = previous_head

    def delete(self, data) -> None:
        node = self.search(data)
        self.delete_node(node)

    def delete_node(self, node: Node) -> None:
        if node is not self.head:
            previous_node = self._search_previous_node(node)
            previous_node.n_ref = node.n_ref
        else:
            self.head = node.n_ref

    def search(self, data) -> Node:
        help_ref = self.head
        while help_ref is not None:
            if help_ref.data == data:
                break
            help_ref = help_ref.n_ref
        return help_ref

    def _search_previous_node(self, node) -> Node:
        help_ref = self.head
        while help_ref is not None:
            if node is None and help_ref.n_ref is None:
                break
            if node is not None and help_ref.n_ref == node:
                break
            help_ref = help_ref.n_ref
        return help_ref

    def empty(self):
        return True if self.head is None else False

    def __repr__(self) -> str:
        return f"HEAD: {self.head}"


if __name__ == "__main__":
    print("SSL Under Test\n"
          "=================================================================")
    sll = SinglyLinkedList()
    for i in range(10):
        sll.push(random.randint(0,100))
    sll.unshift("a")
    sll.unshift("b")
    print(sll)
    sll.delete("b")
    print(sll)
    sll.unshift("e")
    sll.delete("a")
    print(sll)
    sll.push("g")
    print(f"{sll.search('g')}\n{sll.search('e')}")
class Node:
    def __init__(self) -> None:
        self.data = None
        self.prev = None
        self.next = None

    def __repr__(self) -> str:
        if isinstance(self.data, str):
            return f"Node('{self.data}')"

        return f"Node({self.data})"


class Program:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = self.head
        self.pointer = self.head

    def add(self) -> None:
        new_node = Node()

        if self.pointer.next is None:
            self.pointer.next = new_node
            new_node.prev = self.pointer
            self.tail = new_node
        else:
            new_node.next = self.pointer.next
            new_node.prev = self.pointer
            self.pointer.next.prev = new_node
            self.pointer.next = new_node

        self.pointer = new_node

    def bulk_add(self, amount: int) -> None:
        for _ in range(amount):
            self.add()

    def remove(self) -> None:
        if self.pointer is self.head:
            self.head = self.pointer.next
            self.pointer = self.head
            self.pointer.prev = None
        elif self.pointer is self.tail:
            self.tail = self.pointer.prev
            self.pointer = self.tail
            self.pointer.next = None
        else:
            self.pointer.prev.next = self.pointer.next
            self.pointer.next.prev = self.pointer.prev
            self.pointer = self.pointer.next

    def move(self, amount: int) -> None:
        if amount > 0:
            for _ in range(amount):
                if self.pointer.next is None:
                    raise IndexError(f"Index out of range: MOV {amount}")
                self.pointer = self.pointer.next
        else:
            for _ in range(abs(amount)):
                if self.pointer.prev is None:
                    raise IndexError(f"Index out of range: MOV {amount}")
                self.pointer = self.pointer.prev

    def jump(self, index: int) -> None:
        node = self.head

        for _ in range(index):
            if node is None:
                raise IndexError(f"Index out of range: JMP *{index}")
            node = node.next

        self.pointer = node

    def set(self, data: object) -> None:
        self.pointer.data = data

    def get(self, index: int | str = None) -> object:
        if index is None:
            return self.pointer.data

        original_pointer = self.pointer  # Save current pointer to go back

        # Temporarily move to the index pointer and get it's data
        self.jump(index)
        data = self.pointer.data

        self.pointer = original_pointer  # Go back to the original pointer
        return data

    def copy(self, index: int) -> None:
        self.pointer.data = self.get(index)

    def __iter__(self) -> Node:
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(repr(node))
            node = node.next

        return f"LinkedList([{', '.join(nodes)}])"

    def __str__(self) -> str:
        node = self.head
        nodes = []

        while node is not None:
            if self.pointer is node:
                nodes.append(f"[{str(node.data)}]")
            else:
                nodes.append(str(node.data))
            node = node.next

        return " -> ".join(nodes)


if __name__ == "__main__":
    program = Program()

    program.bulk_add(10)


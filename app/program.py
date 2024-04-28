class Node:
    def __init__(self, data: object) -> None:
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self) -> str:
        if isinstance(self.data, str):
            return f"Node('{self.data}')"

        return f"Node({self.data})"


class Program:
    def __init__(self, nodes: list = None) -> None:
        # Initialize the linked list
        self.head = None
        self.tail = None

        # Add the nodes to the linked list from eval(rpr())
        if nodes is not None:
            for node in nodes:
                self.add(node.data)

        # Initialize the linked list with a None node and select as pointer
        self.add(None)
        self.pointer = self.head

    def add(self, data: object) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def add_here(self, data: object) -> None:
        new_node = Node(data)

        if self.pointer is self.head:
            self.head = new_node
            new_node.next = self.pointer
            self.pointer.prev = new_node
            self.pointer = new_node
        else:
            new_node.prev = self.pointer.prev
            new_node.next = self.pointer
            self.pointer.prev.next = new_node
            self.pointer.prev = new_node
            self.pointer = new_node

    def bulk(self, amount: int) -> None:
        for _ in range(amount):
            self.add(None)

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
                    raise IndexError("Index out of range")
                self.pointer = self.pointer.next
        else:
            for _ in range(abs(amount)):
                if self.pointer.prev is None:
                    raise IndexError("Index out of range")
                self.pointer = self.pointer.prev

    def jump(self, location: int | str) -> None:
        # Go to end
        if location == "/":
            self.pointer = self.tail

        # Go to index
        elif isinstance(location, int):
            node = self.head

            for _ in range(location):
                if node is None:
                    raise IndexError("Index out of range")
                node = node.next

            self.pointer = node

        # Go next or prev
        elif "+" in location or "-" in location:
            operand = location[0]
            amount = location[1:]

            if len(amount) == 0:
                amount = 1
            elif not amount.isdigit():
                raise SyntaxError(f"Invalid move command: {location}")

            node = self.pointer

            for _ in range(int(amount)):
                if operand == "+":
                    node = node.next
                else:
                    node = node.prev

                if node is None:
                    raise IndexError("Index out of range")

            self.pointer = node

        # Not recognized
        else:
            raise SyntaxError(f"Unrecognized move command: {location}")

    def set(self, data: object) -> None:
        self.pointer.data = data

    def get(self, location: int | str = None) -> object:
        if location is None:
            return self.pointer.data

        original_pointer = self.pointer  # Save current pointer to go back

        # Temporarily move to the location pointer and get it's data
        self.jump(location)
        data = self.pointer.data

        self.pointer = original_pointer  # Go back to the original pointer
        return data

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
    pass

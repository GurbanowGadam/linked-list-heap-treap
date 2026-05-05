class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def push_back(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def insert(self, position, value):
        if position < 0 or position > self.size:
            print("Invalid position")
            return

        if position == 0:
            self.push_front(value)
            return

        if position == self.size:
            self.push_back(value)
            return

        new_node = Node(value)
        current = self.head

        for _ in range(position):
            current = current.next

        previous_node = current.prev

        previous_node.next = new_node
        new_node.prev = previous_node

        new_node.next = current
        current.prev = new_node

        self.size += 1

    def search(self, value):
        current = self.head
        position = 0

        while current is not None:
            if current.value == value:
                return position

            current = current.next
            position += 1

        return -1

    def delete(self, value):
        current = self.head

        while current is not None:
            if current.value == value:

                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None

                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None

                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.size -= 1
                return True

            current = current.next

        return False

    def display_forward(self):
        current = self.head

        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next

        print("None")

    def display_backward(self):
        current = self.tail

        while current is not None:
            print(current.value, end=" <-> ")
            current = current.prev

        print("None")
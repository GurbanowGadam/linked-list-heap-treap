from binary_heap import BinaryHeap
from doubly_linked_list import DoublyLinkedList
from treap import Treap


def list_values_forward(linked_list):
    values = []
    current = linked_list.head

    while current is not None:
        values.append(current.value)
        current = current.next

    return values


def list_values_backward(linked_list):
    values = []
    current = linked_list.tail

    while current is not None:
        values.append(current.value)
        current = current.prev

    return values


def is_min_heap(values):
    for index, value in enumerate(values):
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(values) and value > values[left]:
            return False

        if right < len(values) and value > values[right]:
            return False

    return True


def check_treap_properties(node, minimum=None, maximum=None):
    if node is None:
        return True

    if minimum is not None and node.key < minimum:
        return False

    if maximum is not None and node.key >= maximum:
        return False

    if node.left is not None and node.left.priority < node.priority:
        return False

    if node.right is not None and node.right.priority < node.priority:
        return False

    return (
        check_treap_properties(node.left, minimum, node.key)
        and check_treap_properties(node.right, node.key, maximum)
    )


def test_doubly_linked_list():
    linked_list = DoublyLinkedList()

    linked_list.push_back(10)
    linked_list.push_back(20)
    linked_list.push_front(5)
    linked_list.insert(2, 15)

    assert list_values_forward(linked_list) == [5, 10, 15, 20]
    assert list_values_backward(linked_list) == [20, 15, 10, 5]
    assert linked_list.search(15) == 2
    assert linked_list.search(100) == -1
    assert linked_list.delete(5) is True
    assert linked_list.delete(20) is True
    assert linked_list.delete(100) is False
    assert list_values_forward(linked_list) == [10, 15]
    assert linked_list.size == 2


def test_binary_heap():
    heap = BinaryHeap()

    for value in [20, 10, 30, 5, 15]:
        heap.insert(value)

    assert is_min_heap(heap.heap)
    assert heap.search(15) is True
    assert heap.search(100) is False
    assert heap.extract_min() == 5
    assert is_min_heap(heap.heap)
    assert heap.delete(20) is True
    assert is_min_heap(heap.heap)
    assert heap.delete(30) is True
    assert is_min_heap(heap.heap)
    assert heap.delete(999) is False

    extracted = []
    while heap.heap:
        extracted.append(heap.extract_min())

    assert extracted == sorted(extracted)


def test_treap():
    treap = Treap()
    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        treap.insert_key(value)

    assert treap.to_sorted_list() == sorted(values)
    assert treap.search_key(40) is True
    assert treap.search_key(100) is False
    assert check_treap_properties(treap.root) is True

    treap.delete_key(30)

    assert treap.search_key(30) is False
    assert treap.to_sorted_list() == [20, 40, 50, 60, 70, 80]
    assert check_treap_properties(treap.root) is True


def main():
    test_doubly_linked_list()
    test_binary_heap()
    test_treap()
    print("All structure tests passed.")


if __name__ == "__main__":
    main()

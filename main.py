from doubly_linked_list import DoublyLinkedList
from binary_heap import BinaryHeap
from treap import Treap


def test_doubly_linked_list():
    print("\n--- Doubly Linked List Demo ---")

    dll = DoublyLinkedList()

    dll.push_back(10)
    dll.push_back(20)
    dll.push_front(5)
    dll.insert(2, 15)

    print("After insertions:")
    dll.display_forward()

    print("Search 15:", dll.search(15))
    print("Search 100:", dll.search(100))

    dll.delete(20)

    print("After deleting 20:")
    dll.display_forward()

    print("Backward display:")
    dll.display_backward()


def test_binary_heap():
    print("\n--- Binary Heap Demo ---")

    heap = BinaryHeap()

    heap.insert(20)
    heap.insert(10)
    heap.insert(30)
    heap.insert(5)
    heap.insert(15)

    print("After insertions:")
    heap.display()

    print("Search 15:", heap.search(15))
    print("Search 100:", heap.search(100))

    print("Extract min:", heap.extract_min())

    print("After extract_min:")
    heap.display()

    heap.delete(20)

    print("After deleting 20:")
    heap.display()


def test_treap():
    print("\n--- Treap Demo ---")

    treap = Treap()

    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        treap.insert_key(value)

    print("Inorder after insertions:")
    treap.inorder(treap.root)
    print()

    print("Search 40:", treap.search_key(40))
    print("Search 100:", treap.search_key(100))

    treap.delete_key(30)

    print("Inorder after deleting 30:")
    treap.inorder(treap.root)
    print()


def main():
    while True:
        print("\n===== Data Structures Project =====")
        print("1. Test Doubly Linked List")
        print("2. Test Binary Heap")
        print("3. Test Treap")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            test_doubly_linked_list()
        elif choice == "2":
            test_binary_heap()
        elif choice == "3":
            test_treap()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
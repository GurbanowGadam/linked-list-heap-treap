# Data Structures Project

This project implements three data structures in Python:

- List: doubly linked list, simple version
- Heap: binary min-heap, simple version
- Tree: Treap, advanced version

The Treap is an advanced randomized binary search tree. It combines the BST property for keys with the heap property for randomly generated priorities.

## How to Run

```bash
python3 main.py
```

The program displays an interactive menu:

- `1` runs the doubly linked list demo
- `2` runs the binary heap demo
- `3` runs the Treap demo
- `0` exits the program

For simple automatic checks:

```bash
python3 test_structures.py
```

## Doubly Linked List

File: `doubly_linked_list.py`

The doubly linked list uses nodes that store:

- `value`: the value stored in the node
- `prev`: reference to the previous node
- `next`: reference to the next node

The `DoublyLinkedList` class stores references to:

- `head`: the first node
- `tail`: the last node
- `size`: the number of elements

Implemented operations:

- `push_front(value)`: inserts a value at the beginning of the list
- `push_back(value)`: inserts a value at the end of the list
- `insert(position, value)`: inserts a value at a given position
- `search(value)`: searches for a value and returns its position or `-1`
- `delete(value)`: deletes the first occurrence of a value and returns `True` or `False`
- `display_forward()`: prints the list from beginning to end
- `display_backward()`: prints the list from end to beginning

Time complexities:

- Insert at beginning: `O(1)`
- Insert at end: `O(1)`
- Insert at position: `O(n)`
- Search: `O(n)`
- Delete by value: `O(n)`

## Binary Heap

File: `binary_heap.py`

The binary heap is implemented as a min-heap using an array. For an element at index `i`:

- the parent is at `(i - 1) // 2`
- the left child is at `2 * i + 1`
- the right child is at `2 * i + 2`

The min-heap property requires every parent to be smaller than or equal to its children.

Implemented operations:

- `insert(value)`: adds the value at the end and restores the heap using `heapify_up`
- `search(value)`: checks whether a value exists in the heap
- `delete(value)`: deletes the first occurrence of a value and restores the heap
- `extract_min()`: removes and returns the minimum value, which is the heap root
- `display()`: prints the internal array

Time complexities:

- Insert: `O(log n)`
- Search: `O(n)`
- Delete by value: `O(n)` to find the element and `O(log n)` to restore the heap
- Extract minimum: `O(log n)`

## Treap

File: `treap.py`

A Treap is a randomized binary search tree. Each node stores:

- `key`: the key used for the BST property
- `priority`: the randomized priority used for the min-heap property
- `left`: the left subtree
- `right`: the right subtree

Properties:

- For keys, it follows the BST rule: smaller keys go to the left, greater or equal keys go to the right.
- For priorities, it follows the min-heap rule: a node's priority is smaller than or equal to the priorities of its children.

Rotations used:

- `rotate_left(x)`: lifts the right child of node `x`
- `rotate_right(y)`: lifts the left child of node `y`

Implemented operations:

- `insert_key(key)`: inserts a key into the Treap
- `search_key(key)`: searches for a key and returns `True` or `False`
- `delete_key(key)`: deletes a key if it exists
- `inorder(root)`: prints the keys in increasing order
- `to_sorted_list()`: returns the keys as a sorted list

Average time complexities:

- Insert: `O(log n)`
- Search: `O(log n)`
- Delete: `O(log n)`

The worst-case complexity can become `O(n)`, but randomized priorities greatly reduce the probability of an unbalanced tree.

## Files

- `main.py`: interactive menu and demos for all structures
- `doubly_linked_list.py`: doubly linked list implementation
- `binary_heap.py`: binary heap implementation
- `treap.py`: Treap implementation
- `test_structures.py`: simple automatic checks for the main operations


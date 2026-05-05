# Proiect Structuri de Date

Acest proiect implementeaza trei structuri de date in Python:

- Lista: lista dublu inlantuita, varianta simpla
- Heap: heap binar min-heap, varianta simpla
- Arbore: Treap, varianta avansata

Treap-ul este o structura avansata de tip arbore binar de cautare randomizat. El combina proprietatea de BST pentru chei cu proprietatea de heap pentru prioritati.

## Cum se ruleaza

```bash
python3 main.py
```

Programul afiseaza un meniu interactiv:

- `1` ruleaza demonstratia pentru lista dublu inlantuita
- `2` ruleaza demonstratia pentru heap-ul binar
- `3` ruleaza demonstratia pentru Treap
- `0` inchide programul

Pentru verificari automate simple:

```bash
python3 test_structures.py
```

## Lista dublu inlantuita

Fisier: `doubly_linked_list.py`

Lista dublu inlantuita foloseste noduri care pastreaza:

- `value`: valoarea nodului
- `prev`: legatura spre nodul anterior
- `next`: legatura spre nodul urmator

Clasa `DoublyLinkedList` pastreaza referinte catre:

- `head`: primul nod
- `tail`: ultimul nod
- `size`: numarul de elemente

Operatii implementate:

- `push_front(value)`: insereaza la inceputul listei
- `push_back(value)`: insereaza la finalul listei
- `insert(position, value)`: insereaza valoarea pe pozitia data
- `search(value)`: cauta valoarea si intoarce pozitia ei sau `-1`
- `delete(value)`: sterge prima aparitie a valorii si intoarce `True` sau `False`
- `display_forward()`: afiseaza lista de la inceput la final
- `display_backward()`: afiseaza lista de la final la inceput

Complexitati:

- Inserare la inceput: `O(1)`
- Inserare la final: `O(1)`
- Inserare pe pozitie: `O(n)`
- Cautare: `O(n)`
- Stergere dupa valoare: `O(n)`

## Heap binar

Fisier: `binary_heap.py`

Heap-ul binar este implementat ca min-heap folosind un vector. Pentru un element de pe pozitia `i`:

- parintele este la `(i - 1) // 2`
- copilul stang este la `2 * i + 1`
- copilul drept este la `2 * i + 2`

Proprietatea de min-heap cere ca fiecare parinte sa fie mai mic sau egal decat copiii sai.

Operatii implementate:

- `insert(value)`: adauga valoarea la final si reface heap-ul cu `heapify_up`
- `search(value)`: verifica daca valoarea exista in heap
- `delete(value)`: sterge prima aparitie a valorii si reface heap-ul
- `extract_min()`: scoate si intoarce minimul, adica radacina heap-ului
- `display()`: afiseaza vectorul intern

Complexitati:

- Inserare: `O(log n)`
- Cautare: `O(n)`
- Stergere dupa valoare: `O(n)` pentru gasirea elementului si `O(log n)` pentru refacerea heap-ului
- Extragere minim: `O(log n)`

## Treap

Fisier: `treap.py`

Treap-ul este un arbore binar de cautare randomizat. Fiecare nod pastreaza:

- `key`: cheia folosita pentru proprietatea de BST
- `priority`: prioritatea randomizata folosita pentru proprietatea de min-heap
- `left`: subarborele stang
- `right`: subarborele drept

Proprietati:

- Pentru chei respecta regula unui BST: cheile mai mici sunt in stanga, cheile mai mari sau egale sunt in dreapta.
- Pentru prioritati respecta regula unui min-heap: prioritatea unui nod este mai mica sau egala decat prioritatile copiilor.

Rotatii folosite:

- `rotate_left(x)`: ridica fiul drept al nodului `x`
- `rotate_right(y)`: ridica fiul stang al nodului `y`

Operatii implementate:

- `insert_key(key)`: insereaza cheia in Treap
- `search_key(key)`: cauta cheia si intoarce `True` sau `False`
- `delete_key(key)`: sterge cheia daca exista
- `inorder(root)`: afiseaza cheile in ordine crescatoare
- `to_sorted_list()`: intoarce cheile intr-o lista sortata

Complexitati medii:

- Inserare: `O(log n)`
- Cautare: `O(log n)`
- Stergere: `O(log n)`

Complexitatea poate deveni `O(n)` in cazuri nefavorabile, dar prioritatile randomizate reduc mult probabilitatea unui arbore dezechilibrat.

## Fisiere

- `main.py`: meniul interactiv si demonstratiile pentru toate structurile
- `doubly_linked_list.py`: implementarea listei dublu inlantuite
- `binary_heap.py`: implementarea heap-ului binar
- `treap.py`: implementarea Treap-ului
- `test_structures.py`: verificari automate simple pentru operatiile principale

## Barem

Proiectul corespunde variantei pentru nota 10:

- doua structuri in varianta simpla: lista dublu inlantuita si heap binar
- o structura in varianta avansata: Treap

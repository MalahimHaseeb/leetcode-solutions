# 328. Odd Even Linked List

**Difficulty:** Medium

**LeetCode:** [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

---

## Problem

Given the `head` of a singly linked list, group all nodes with odd indices together followed by the nodes with even indices.

The first node is considered odd, the second node is even, and so on.

The relative order of the nodes inside both the odd and even groups must remain unchanged.

The solution must use `O(1)` extra space and `O(n)` time.

---

## Examples

### Example 1

**Input:**

```text
1 -> 2 -> 3 -> 4 -> 5
```

**Output:**

```text
1 -> 3 -> 5 -> 2 -> 4
```

**Explanation:**

The nodes at odd indices are:

```text
1 -> 3 -> 5
```

The nodes at even indices are:

```text
2 -> 4
```

The two groups are then connected:

```text
1 -> 3 -> 5 -> 2 -> 4
```

---

### Example 2

**Input:**

```text
2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
```

**Output:**

```text
2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
```

---

## Constraints

- The number of nodes in the linked list is in the range `[0, 10^4]`.
- `-10^6 <= Node.val <= 10^6`

---

## Approach

Use two pointers to build the odd and even groups directly in the original linked list.

- `odd` points to the last node in the odd-indexed group.
- `even` points to the last node in the even-indexed group.
- `even_head` stores the first even node so it can be connected after the odd group at the end.

For each iteration:

1. Connect the current odd node to the next even node.
2. Move `odd` forward.
3. Connect the current even node to the next odd node.
4. Move `even` forward.
5. Continue while there is an even node and another node after it.
6. Finally, connect the end of the odd group to `even_head`.

This rearranges the existing links without creating any new nodes.

---

## Example Walkthrough

For:

```text
1 -> 2 -> 3 -> 4 -> 5
```

Initially:

```text
odd = 1
even = 2
even_head = 2
```

First iteration:

```text
1 -> 3
2 -> 4
```

Now:

```text
odd = 3
even = 4
```

Second iteration:

```text
3 -> 5
4 -> None
```

Now the groups are:

```text
Odd:  1 -> 3 -> 5
Even: 2 -> 4
```

Finally, connect the odd group to the even group:

```text
1 -> 3 -> 5 -> 2 -> 4
```

---

## Complexity

Let `n` be the number of nodes in the linked list.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

Each node is processed a constant number of times, and only a few pointers are used.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).

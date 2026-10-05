# 206. Reverse Linked List

**Difficulty:** Easy

**LeetCode:** [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

---

## Problem

Given the `head` of a singly linked list, reverse the list and return the reversed list.

The links between the nodes should be reversed so that the last node becomes the first node.

---

## Examples

### Example 1

**Input:**

```text
head = [1,2,3,4,5]
```

**Output:**

```text
[5,4,3,2,1]
```

**Explanation:**

The original linked list is:

```text
1 -> 2 -> 3 -> 4 -> 5
```

After reversing:

```text
5 -> 4 -> 3 -> 2 -> 1
```

---

### Example 2

**Input:**

```text
head = [1,2]
```

**Output:**

```text
[2,1]
```

---

### Example 3

**Input:**

```text
head = []
```

**Output:**

```text
[]
```

---

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

---

## Approach

Use three pointers to reverse the linked list iteratively:

- `curr` points to the current node.
- `prev` points to the previous node.
- `next_node` temporarily stores the next node before changing the current node's link.

For each node:

1. Save the next node in `next_node`.
2. Reverse the current node's pointer by setting `curr.next = prev`.
3. Move `prev` to the current node.
4. Move `curr` to the saved next node.
5. Continue until `curr` becomes `None`.

At the end, `prev` points to the new head of the reversed linked list.

---

## Example Walkthrough

For:

```text
1 -> 2 -> 3 -> 4 -> 5 -> None
```

Initially:

```text
prev = None
curr = 1
```

First iteration:

```text
1 -> None
prev = 1
curr = 2
```

Second iteration:

```text
2 -> 1 -> None
prev = 2
curr = 3
```

Continue the same process:

```text
3 -> 2 -> 1 -> None
```

Then:

```text
4 -> 3 -> 2 -> 1 -> None
```

Finally:

```text
5 -> 4 -> 3 -> 2 -> 1 -> None
```

`prev` is now the new head, so return `prev`.

---

## Complexity

Let `n` be the number of nodes in the linked list.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

Each node is visited once, and only a constant number of pointers are used.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
